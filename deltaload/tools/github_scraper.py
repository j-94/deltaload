"""GitHub scraper module for bookmark enrichment."""

import os
import json
import logging
import requests
from typing import Dict, Optional, Tuple
from urllib.parse import urlparse
from dotenv import load_dotenv
from datetime import datetime

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s.%(msecs)03d %(levelname)s: %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)
logger = logging.getLogger(__name__)

class GitHubScraper:
    """GitHub scraper for repository data and README content."""
    
    def __init__(self):
        """Initialize with GitHub API token."""
        # Load environment variables
        load_dotenv()
        
        # Get and validate environment variables
        self.github_token = os.getenv("GH_TOKEN")
        
        # Validate required tokens
        if not self.github_token:
            logger.warning("No GitHub token found. API rate limits will be severely restricted.")
            
        logger.info("Initializing GitHubScraper")
        
        self.headers = {
            'Accept': 'application/vnd.github.v3+json',
            'User-Agent': 'BookmarkEnrichment/1.0',
        }
        
        if self.github_token:
            self.headers['Authorization'] = f"token {self.github_token}"
            
    def parse_github_url(self, url: str) -> Optional[Tuple[str, str]]:
        """
        Parse a GitHub URL to extract owner and repo.
        
        Args:
            url: GitHub URL
            
        Returns:
            Tuple of (owner, repo) or None if invalid
        """
        if not url:
            return None
            
        try:
            parsed_url = urlparse(url)
            if 'github.com' not in parsed_url.netloc:
                return None
                
            path_parts = parsed_url.path.strip('/').split('/')
            if len(path_parts) < 2:
                return None
                
            return (path_parts[0], path_parts[1])
            
        except Exception as e:
            logger.error(f"Error parsing GitHub URL: {str(e)}")
            return None
            
    def fetch_repo_data(self, owner: str, repo: str) -> Dict:
        """
        Fetch repository metadata from GitHub API.
        
        Args:
            owner: Repository owner/organization
            repo: Repository name
            
        Returns:
            Dictionary with repository data
        """
        result = {
            'owner': owner,
            'repo': repo,
            'status': 'error',
            'url': f"https://github.com/{owner}/{repo}"
        }
        
        try:
            api_url = f"https://api.github.com/repos/{owner}/{repo}"
            logger.info(f"Fetching repo data from {api_url}")
            
            response = requests.get(api_url, headers=self.headers, timeout=10)
            
            # --- DEBUGGING --- 
            logger.info(f"GitHub API response status code for {owner}/{repo}: {response.status_code}")
            logger.debug(f"GitHub API response text for {owner}/{repo} (first 500 chars): {response.text[:500]}")
            # --- END DEBUGGING ---
            
            response.raise_for_status()
            
            repo_data = response.json()
            
            # --- Robustness Check ---
            # Check if repo_data is a dictionary and has essential keys. 
            # Handle cases where API returns 200 OK but no actual repo data (e.g., moved/private?)
            if not isinstance(repo_data, dict) or not repo_data.get('id'): # Check for 'id' as a key indicator of valid repo data
                logger.warning(f"Received non-standard repo data for {owner}/{repo}. Status: {response.status_code}, Data: {str(repo_data)[:500]}")
                # Treat this as a failure to fetch valid data
                result['status'] = 'error'
                result['error'] = f"Received non-standard repo data (Status: {response.status_code})"
                return result # Return early with error status
            # --- End Robustness Check ---
            
            # Extract relevant data (Now safer)
            result.update({
                'status': 'success',
                'name': repo_data.get('name'),
                'full_name': repo_data.get('full_name'),
                'description': repo_data.get('description'),
                'language': repo_data.get('language'),
                'stars': repo_data.get('stargazers_count'),
                'forks': repo_data.get('forks_count'),
                'watchers': repo_data.get('watchers_count'),
                'open_issues': repo_data.get('open_issues_count'),
                'license': (repo_data.get('license') or {}).get('name'),
                'created_at': repo_data.get('created_at'),
                'updated_at': repo_data.get('updated_at'),
                'pushed_at': repo_data.get('pushed_at')
            })
            
            return result
            
        except requests.RequestException as e:
            logger.error(f"Request error for {owner}/{repo}: {str(e)}")
            result['error'] = str(e)
            return result
        except Exception as e:
            logger.error(f"Error fetching repo data for {owner}/{repo}: {str(e)}")
            result['error'] = str(e)
            return result
            
    def fetch_readme(self, owner: str, repo: str) -> Dict:
        """
        Fetch repository README content from GitHub API.
        
        Args:
            owner: Repository owner/organization
            repo: Repository name
            
        Returns:
            Dictionary with README content
        """
        result = {
            'owner': owner,
            'repo': repo,
            'status': 'error',
            'url': f"https://github.com/{owner}/{repo}",
            'content': '',
            'path': '',
            'name': '',
            'encoding': '',
            'size': 0
        }
        
        try:
            api_url = f"https://api.github.com/repos/{owner}/{repo}/readme"
            logger.info(f"Fetching README from {api_url}")
            
            # First fetch the README metadata
            headers = self.headers.copy()
            response = requests.get(api_url, headers=headers, timeout=10)
            
            # If the API returns a 404, try to find alternate README files
            if response.status_code == 404:
                logger.warning(f"No README found at default location for {owner}/{repo}, trying alternatives")
                
                # Try common README variations by checking for their existence
                for readme_name in ['README.md', 'Readme.md', 'readme.md', 'README.txt', 'README', 'docs/README.md']:
                    alt_api_url = f"https://api.github.com/repos/{owner}/{repo}/contents/{readme_name}"
                    alt_response = requests.get(alt_api_url, headers=headers, timeout=10)
                    if alt_response.status_code == 200:
                        logger.info(f"Found alternative README at {readme_name}")
                        response = alt_response
                        break
            
            response.raise_for_status()
            readme_meta = response.json()
            
            # Capture metadata
            result['path'] = readme_meta.get('path', '')
            result['name'] = readme_meta.get('name', '')
            result['size'] = readme_meta.get('size', 0)
            result['encoding'] = readme_meta.get('encoding', '')
            
            # Now fetch the raw content
            headers['Accept'] = 'application/vnd.github.v3.raw'
            download_url = readme_meta.get('download_url') or f"https://raw.githubusercontent.com/{owner}/{repo}/master/{result['path']}"
            
            content_response = requests.get(download_url, headers=headers, timeout=10)
            content_response.raise_for_status()
            
            # Return raw README content
            result.update({
                'status': 'success',
                'content': content_response.text
            })
            
            return result
            
        except requests.RequestException as e:
            logger.error(f"Request error for README {owner}/{repo}: {str(e)}")
            result['error'] = str(e)
            return result
        except Exception as e:
            logger.error(f"Error fetching README for {owner}/{repo}: {str(e)}")
            result['error'] = str(e)
            return result
            
    def format_repo_markdown(self, repo_data: Dict, readme_content: str) -> str:
        """
        Format repository data and README as markdown.
        
        Args:
            repo_data: Repository metadata
            readme_content: README content
            
        Returns:
            Formatted markdown
        """
        # Start with repo header and metadata
        markdown = f"# [{repo_data.get('full_name', '')}]({repo_data.get('url', '')})\n\n"
        
        # Add description if available
        if repo_data.get('description'):
            markdown += f"{repo_data.get('description')}\n\n"
            
        # Add metadata table
        markdown += "| | |\n"
        markdown += "|---|---|\n"
        
        if repo_data.get('language'):
            markdown += f"| Language | {repo_data.get('language')} |\n"
            
        if repo_data.get('stars') is not None:
            markdown += f"| Stars | {repo_data.get('stars')} |\n"
            
        if repo_data.get('forks') is not None:
            markdown += f"| Forks | {repo_data.get('forks')} |\n"
            
        if repo_data.get('watchers') is not None:
            markdown += f"| Watchers | {repo_data.get('watchers')} |\n"
            
        if repo_data.get('license'):
            markdown += f"| License | {repo_data.get('license')} |\n"
            
        if repo_data.get('updated_at'):
            # Format date for better readability
            try:
                updated_date = datetime.fromisoformat(repo_data['updated_at'].replace('Z', '+00:00')).strftime('%Y-%m-%d')
                markdown += f"| Last Updated | {updated_date} |\n"
            except:
                markdown += f"| Last Updated | {repo_data.get('updated_at')} |\n"
        
        markdown += "\n"
        
        # Add README separator
        markdown += "## README\n\n"
        
        # Add README content, ensuring we don't duplicate the repo name header
        # if it's already at the start of the README
        content_lines = readme_content.split('\n')
        if content_lines and content_lines[0].startswith('# ') and repo_data.get('name', '') in content_lines[0]:
            # Skip the first line and any empty lines that follow
            i = 1
            while i < len(content_lines) and not content_lines[i].strip():
                i += 1
            readme_content = '\n'.join(content_lines[i:])
            
        markdown += readme_content
        
        return markdown
    
    def process_url(self, url: str) -> Dict:
        """
        Process a GitHub URL to extract repository data and README.
        
        Args:
            url: GitHub repository URL
            
        Returns:
            Dictionary with repository data and README content
        """
        result = {
            'url': url,
            'source': 'github',
            'status': 'error',
            'content': '',
            'github_readme': '',
            'metadata': {}
        }
        
        # Parse GitHub URL
        repo_info = self.parse_github_url(url)
        if not repo_info:
            result['error'] = 'Not a valid GitHub repository URL'
            return result
            
        owner, repo = repo_info
        
        # Fetch repository data
        repo_data = self.fetch_repo_data(owner, repo)
        if repo_data['status'] != 'success':
            result['error'] = repo_data.get('error', 'Failed to fetch repository data')
            return result
            
        # Fetch README content
        readme_data = self.fetch_readme(owner, repo)
        
        # Store the raw README content in a separate field
        if readme_data['status'] == 'success':
            result['github_readme'] = readme_data['content']
            result['readme_path'] = readme_data['path']
        else:
            logger.warning(f"Could not fetch README for {owner}/{repo}: {readme_data.get('error')}")
            result['github_readme'] = ""
            
        # Create formatted markdown content
        formatted_content = self.format_repo_markdown(repo_data, 
                                                    readme_data['content'] if readme_data['status'] == 'success' else "(README content not available)")
            
        # Build metadata
        metadata = {
            'owner': owner,
            'repo': repo,
            'language': repo_data.get('language'),
            'stars': repo_data.get('stars'),
            'forks': repo_data.get('forks'),
            'watchers': repo_data.get('watchers'),
            'open_issues': repo_data.get('open_issues'),
            'license': repo_data.get('license'),
            'created_at': repo_data.get('created_at'),
            'updated_at': repo_data.get('updated_at'),
            'pushed_at': repo_data.get('pushed_at'),
            'has_readme': readme_data['status'] == 'success',
            'readme_path': readme_data.get('path', '')
        }
        
        # Update result
        result.update({
            'status': 'success',
            'content': formatted_content,
            'created_at': repo_data.get('created_at'),
            'metadata': metadata
        })
        
        return result