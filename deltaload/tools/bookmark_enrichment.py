"""Bookmark enrichment module for enhancing bookmark data with external content."""

import os
import json
import logging
import time
from typing import Dict, List, Optional, Union
from datetime import datetime
from urllib.parse import urlparse
from dotenv import load_dotenv

# Import scraper modules
from .web_scraper import WebScraper
from .twitter_thread_fetcher import TwitterThreadFetcher
from .github_scraper import GitHubScraper

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s.%(msecs)03d %(levelname)s: %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)
logger = logging.getLogger(__name__)

class BookmarkEnrichment:
    """Bookmark enrichment system to enhance bookmark data with external content."""
    
    def __init__(self, cache_dir: str = './cache'):
        """
        Initialize bookmark enrichment system.
        
        Args:
            cache_dir: Directory for caching scraped content
        """
        # Load environment variables
        load_dotenv()
        
        # Initialize cache directory
        self.cache_dir = cache_dir
        os.makedirs(cache_dir, exist_ok=True)
        
        # Initialize scrapers
        self._init_scrapers()
        
        logger.info("BookmarkEnrichment initialized")
        
    def _init_scrapers(self):
        """Initialize scrapers for different sources."""
        try:
            # Initialize Twitter thread fetcher
            self.twitter_fetcher = TwitterThreadFetcher()
            logger.info("TwitterThreadFetcher initialized successfully")
        except Exception as e:
            logger.error(f"Error initializing TwitterThreadFetcher: {str(e)}")
            self.twitter_fetcher = None
            
        try:
            # Initialize GitHub scraper
            self.github_scraper = GitHubScraper()
            logger.info("GitHubScraper initialized successfully")
        except Exception as e:
            logger.error(f"Error initializing GitHubScraper: {str(e)}")
            self.github_scraper = None
            
        # Always initialize the generic web scraper
        self.web_scraper = WebScraper()
        logger.info("WebScraper initialized successfully")
        
    def get_domain_from_url(self, url: str) -> str:
        """Extract domain from URL."""
        try:
            parsed_url = urlparse(url)
            domain = parsed_url.netloc
            return domain.lower().replace('www.', '')
        except Exception:
            return ''
            
    def determine_source(self, url: str) -> str:
        """
        Determine the source type based on URL.
        
        Args:
            url: URL to determine source
            
        Returns:
            Source type (twitter, github, etc.)
        """
        if not url:
            return 'unknown'
            
        domain = self.get_domain_from_url(url)
        
        if domain in ['twitter.com', 'x.com'] or 'twitter.com' in domain or 'x.com' in domain:
            return 'twitter'
        elif 'github.com' in domain:
            return 'github'
        else:
            return 'web'
            
    def enrich_bookmark(self, bookmark: Dict, force_refresh: bool = False) -> Dict:
        """
        Enrich a single bookmark with external content.
        
        Args:
            bookmark: Dictionary with bookmark data
            force_refresh: Force refresh even if cached data exists
            
        Returns:
            Enriched bookmark dictionary
        """
        url = bookmark.get('url')
        if not url:
            logger.warning("Bookmark missing URL, cannot enrich")
            return bookmark
            
        # --- Skip if already enriched (unless forcing refresh) --- 
        if not force_refresh:
            metadata = bookmark.get('metadata', {})
            # Handle case where metadata might be a string
            if isinstance(metadata, str):
                try:
                    # First try to parse as JSON
                    metadata = json.loads(metadata)
                except json.JSONDecodeError:
                    try:
                        # Second attempt: Try to parse as Python literal
                        # This handles cases where single quotes are used instead of double quotes
                        import ast
                        metadata = ast.literal_eval(metadata)
                    except (SyntaxError, ValueError):
                        # If all else fails, keep as empty dict
                        metadata = {}
            
            if metadata.get('enriched_at'):
                logger.info(f"Skipping already enriched bookmark ({metadata['enriched_at']}): {url}")
                return bookmark # Return unchanged
        # --- End Skip Check ---
            
        # Detect source type
        source_type = self.determine_source(url)
        logger.info(f"Processing {source_type} URL: {url}")
        
        # Check if we already have cached content and not forcing refresh
        cache_key = self._get_cache_key(url)
        if not force_refresh and self._check_cache(cache_key):
            logger.info(f"Using cached content for {url}")
            cached_data = self._load_from_cache(cache_key)
            if cached_data:
                return self._merge_bookmark_with_enrichment(bookmark, cached_data)
                
        # Process based on source type
        result = None
        
        try:
            if source_type == 'twitter' and self.twitter_fetcher:
                logger.info(f"Enriching Twitter content for {url}")
                result = self.twitter_fetcher.process_url(url)
                
            elif source_type == 'github' and self.github_scraper:
                logger.info(f"Enriching GitHub content for {url}")
                result = self.github_scraper.process_url(url)
                
            else:
                # Default to generic web scraper
                logger.info(f"Enriching web content for {url}")
                result = self.web_scraper.scrape_url(url)
                
            # Handle processing errors
            if not result or result.get('status') == 'error':
                logger.error(f"Error enriching {url}: {result.get('error') if result else 'No result'}")
                return bookmark
                
            # Cache successful result
            self._save_to_cache(cache_key, result)
            
            # Merge results into the bookmark
            return self._merge_bookmark_with_enrichment(bookmark, result)
            
        except Exception as e:
            logger.error(f"Error during enrichment of {url}: {str(e)}")
            return bookmark
            
    def enrich_bookmarks(self, bookmarks: List[Dict], force_refresh: bool = False) -> List[Dict]:
        """
        Enrich a list of bookmarks with external content.
        
        Args:
            bookmarks: List of bookmark dictionaries
            force_refresh: Force refresh even if cached data exists
            
        Returns:
            List of enriched bookmark dictionaries
        """
        enriched_bookmarks = []
        
        for i, bookmark in enumerate(bookmarks):
            logger.info(f"Processing bookmark {i+1}/{len(bookmarks)}: {bookmark.get('url', 'No URL')}")
            try:
                enriched = self.enrich_bookmark(bookmark, force_refresh)
                enriched_bookmarks.append(enriched)
                # Add a small delay to avoid overwhelming APIs
                time.sleep(0.5)
            except Exception as e:
                logger.error(f"Error processing bookmark: {str(e)}")
                enriched_bookmarks.append(bookmark)
                
        return enriched_bookmarks
                
    def _merge_bookmark_with_enrichment(self, bookmark: Dict, enrichment: Dict) -> Dict:
        """
        Merge bookmark with enrichment data.
        
        Args:
            bookmark: Original bookmark dictionary
            enrichment: Enrichment data dictionary
            
        Returns:
            Merged dictionary
        """
        result = bookmark.copy()
        
        # Only update content if it's empty or not set
        if not result.get('content') and enrichment.get('content'):
            result['content'] = enrichment['content']
            
        # Merge metadata - convert to dict if it's a string
        current_metadata = result.get('metadata', {})
        if isinstance(current_metadata, str):
            try:
                # First try to parse as JSON
                current_metadata = json.loads(current_metadata)
            except json.JSONDecodeError:
                try:
                    # Second attempt: Try to parse as Python literal
                    # This handles cases where single quotes are used instead of double quotes
                    import ast
                    current_metadata = ast.literal_eval(current_metadata)
                except (SyntaxError, ValueError):
                    # If all else fails, keep as empty dict
                    current_metadata = {}
                
        # Get enrichment metadata
        new_metadata = enrichment.get('metadata', {})
        
        # Combine metadata, preferring existing values
        combined_metadata = {**new_metadata, **current_metadata}
        
        # Add enrichment timestamp
        combined_metadata['enriched_at'] = datetime.now().isoformat()
        
        # Update metadata
        result['metadata'] = combined_metadata
        
        return result
    
    def _get_cache_key(self, url: str) -> str:
        """Generate cache key from URL."""
        parsed_url = urlparse(url)
        domain = parsed_url.netloc.replace('.', '_').replace('-', '_')
        path = parsed_url.path.replace('/', '_').replace('.', '_').replace('-', '_')
        if not path:
            path = 'index'
        return f"{domain}{path}"
        
    def _check_cache(self, cache_key: str) -> bool:
        """Check if cache exists for key."""
        cache_file = os.path.join(self.cache_dir, f"{cache_key}.json")
        return os.path.exists(cache_file)
        
    def _load_from_cache(self, cache_key: str) -> Optional[Dict]:
        """Load data from cache."""
        cache_file = os.path.join(self.cache_dir, f"{cache_key}.json")
        try:
            if os.path.exists(cache_file):
                with open(cache_file, 'r', encoding='utf-8') as f:
                    return json.load(f)
        except Exception as e:
            logger.error(f"Error loading from cache: {str(e)}")
        return None
        
    def _save_to_cache(self, cache_key: str, data: Dict):
        """Save data to cache."""
        try:
            cache_file = os.path.join(self.cache_dir, f"{cache_key}.json")
            with open(cache_file, 'w', encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=False, indent=2)
        except Exception as e:
            logger.error(f"Error saving to cache: {str(e)}")
            
    def process_jsonl_file(self, input_file: str, output_file: str, force_refresh: bool = False):
        """
        Process a JSONL file of bookmarks and save enriched results.
        
        Args:
            input_file: Path to input JSONL file
            output_file: Path to output JSONL file
            force_refresh: Force refresh even if cached data exists
        """
        bookmarks = []
        
        # Read input file
        try:
            with open(input_file, 'r', encoding='utf-8') as f:
                for line in f:
                    try:
                        bookmark = json.loads(line.strip())
                        bookmarks.append(bookmark)
                    except json.JSONDecodeError:
                        logger.error(f"Error parsing JSON line: {line}")
        except Exception as e:
            logger.error(f"Error reading input file: {str(e)}")
            return
            
        logger.info(f"Loaded {len(bookmarks)} bookmarks from {input_file}")
        
        # Enrich bookmarks
        enriched_bookmarks = self.enrich_bookmarks(bookmarks, force_refresh)
        
        # Write output file
        try:
            with open(output_file, 'w', encoding='utf-8') as f:
                for bookmark in enriched_bookmarks:
                    json.dump(bookmark, f, ensure_ascii=False)
                    f.write('\n')
            logger.info(f"Saved {len(enriched_bookmarks)} enriched bookmarks to {output_file}")
        except Exception as e:
            logger.error(f"Error writing output file: {str(e)}")
            
def main():
    """Main function for command line usage."""
    import argparse
    
    parser = argparse.ArgumentParser(description='Enrich bookmarks with external content')
    parser.add_argument('input_file', help='Input JSONL file')
    parser.add_argument('output_file', help='Output JSONL file')
    parser.add_argument('--cache-dir', default='./cache', help='Cache directory')
    parser.add_argument('--force-refresh', action='store_true', help='Force refresh cache')
    
    args = parser.parse_args()
    
    enrichment = BookmarkEnrichment(cache_dir=args.cache_dir)
    enrichment.process_jsonl_file(args.input_file, args.output_file, args.force_refresh)
    
if __name__ == '__main__':
    main()