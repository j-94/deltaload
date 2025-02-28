"""GitHub scraper module for bookmark enrichment."""

import os
import json
import logging
import requests
from typing import Dict, Optional, Tuple
from urllib.parse import urlparse
from dotenv import load_dotenv

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
            response.raise_for_status()
            
            repo_data = response.json()
            
            # Extract relevant data
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
                'license': repo_data.get('license', {}).get('name'),
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
            'content': ''
        }
        
        try:
            api_url = f"https://api.github.com/repos/{owner}/{repo}/readme"
            logger.info(f"Fetching README from {api_url}")
            
            # Use raw content accept header
            headers = self.headers.copy()
            headers['Accept'] = 'application/vnd.github.v3.raw'
            
            response = requests.get(api_url, headers=headers, timeout=10)
            response.raise_for_status()
            
            # Return raw README content
            result.update({
                'status': 'success',
                'content': response.text
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
        
        # Combine repository description and README content
        content = ""
        if repo_data.get('description'):
            content += f"# {repo_data['name']}\n\n{repo_data['description']}\n\n"
            
        if readme_data['status'] == 'success':
            content += readme_data['content']
        else:
            logger.warning(f"Could not fetch README for {owner}/{repo}: {readme_data.get('error')}")
            content += "(README content not available)"
            
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
            'pushed_at': repo_data.get('pushed_at')
        }
        
        # Update result
        result.update({
            'status': 'success',
            'content': content,
            'created_at': repo_data.get('created_at'),
            'metadata': metadata
        })
        
        return result