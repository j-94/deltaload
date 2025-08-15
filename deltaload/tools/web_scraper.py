"""Web scraper module for bookmark enrichment."""

import logging
import requests
from urllib.parse import urlparse
from bs4 import BeautifulSoup
import re
import html2text
import hashlib
import os
import json
import time
from datetime import datetime
from typing import Dict, List, Optional, Union
import traceback

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s.%(msecs)03d %(levelname)s: %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)
logger = logging.getLogger(__name__)

class WebScraper:
    """Web scraper for retrieving and processing web content."""
    
    def __init__(self, cache_dir: str = './web_cache'):
        """Initialize web scraper with default settings."""
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.9',
            'Connection': 'keep-alive',
            'Upgrade-Insecure-Requests': '1',
        }
        
        # Initialize cache directory
        self.cache_dir = cache_dir
        os.makedirs(cache_dir, exist_ok=True)
        
        # Initialize HTML to Markdown converter
        self.html_to_markdown = html2text.HTML2Text()
        self.html_to_markdown.ignore_links = False
        self.html_to_markdown.ignore_images = False
        self.html_to_markdown.escape_snob = True
        self.html_to_markdown.body_width = 0  # Don't wrap text
        
        logger.info("WebScraper initialized with cache at {}".format(cache_dir))
    
    def scrape_url(self, url, force_refresh=False):
        """
        Scrape content from a web URL.
        
        Args:
            url: The URL to scrape
            force_refresh: Ignore cache and fetch fresh data
            
        Returns:
            Dictionary with scraped data
        """
        result = {
            'url': url,
            'source': 'web',
            'status': 'error',
            'content': '',
            'metadata': {},
            'scraped_at': datetime.now().isoformat()
        }
        
        try:
            logger.info(f"Scraping URL: {url}")
            
            # Check cache first
            cache_key = self._get_cache_key(url)
            if not force_refresh and self._check_cache(cache_key):
                logger.info(f"Using cached content for {url}")
                cached_data = self._load_from_cache(cache_key)
                if cached_data:
                    return cached_data
            
            # Fetch the URL
            response = requests.get(url, headers=self.headers, timeout=15)
            response.raise_for_status()
            
            # Record HTTP data
            result['status_code'] = response.status_code
            result['content_type'] = response.headers.get('Content-Type', '')
            
            # Check if it's a supported content type
            if 'text/html' not in result['content_type'] and 'application/xhtml+xml' not in result['content_type']:
                logger.warning(f"Unsupported content type: {result['content_type']}")
                result['error'] = f"Unsupported content type: {result['content_type']}"
                result['content'] = "Content type not supported for extraction"
                return result
            
            # Parse HTML
            soup = BeautifulSoup(response.text, 'html.parser')
            
            # Extract all metadata
            metadata = self._extract_all_metadata(soup, url)
            
            # Extract main content
            content_html, content_text = self._extract_content(soup, url)
            
            # Extract images with context
            images = self._extract_images(soup, url)
            
            # Create full content representation in markdown
            markdown_content = self._create_enhanced_markdown(content_html, metadata, images)
            
            # Test the markdown content and create full_text field
            full_text = markdown_content
            
            # Ensure full_text is not empty
            if not full_text.strip():
                # Fallback to plain text if markdown failed
                full_text = content_text
                logger.warning(f"Markdown generation produced empty result for {url}, using plain text instead")
            
            # Update result
            result.update({
                'status': 'success',
                'content': content_text,
                'html_content': content_html,
                'metadata': metadata,
                'markdown': markdown_content,
                'full_text': full_text,
                'domain': metadata.get('domain', ''),
                'images': images
            })
            
            # Save to cache
            self._save_to_cache(cache_key, result)
            
            return result
            
        except requests.exceptions.RequestException as e:
            logger.error(f"Request error scraping {url}: {str(e)}")
            result['error'] = str(e)
            return result
        except Exception as e:
            logger.error(f"Error scraping {url}: {str(e)}")
            logger.error(traceback.format_exc())
            result['error'] = str(e)
            return result
    
    def _extract_all_metadata(self, soup, url):
        """Extract all metadata from soup."""
        # URL info
        parsed_url = urlparse(url)
        domain = parsed_url.netloc
        
        # Basic metadata
        metadata = {
            'title': self._extract_title(soup),
            'description': self._extract_description(soup),
            'canonical_url': self._extract_canonical_url(soup) or url,
            'author': self._extract_author(soup),
            'published_date': self._extract_published_date(soup),
            'modified_date': self._extract_modified_date(soup),
            'domain': domain,
            'site_name': self._extract_site_name(soup),
            'favicon': self._extract_favicon(soup, url),
            'language': self._extract_language(soup),
            'read_time': self._estimate_read_time(soup),
            'word_count': self._count_words(soup),
            'extracted_at': datetime.now().isoformat()
        }
        
        # OpenGraph metadata
        og_meta = self._extract_opengraph_data(soup)
        if og_meta:
            metadata['opengraph'] = og_meta
            
        # Twitter card metadata
        twitter_meta = self._extract_twitter_card_data(soup)
        if twitter_meta:
            metadata['twitter_card'] = twitter_meta
            
        # JSON-LD metadata (often contains rich structured data)
        json_ld_data = self._extract_json_ld(soup)
        if json_ld_data:
            metadata['json_ld'] = json_ld_data
            
        return metadata
    
    def _extract_title(self, soup):
        """Extract title from soup."""
        title_tag = soup.find('title')
        if title_tag:
            return title_tag.text.strip()
            
        # Try OpenGraph
        og_title = soup.find('meta', property='og:title')
        if og_title:
            return og_title.get('content', '').strip()
            
        # Try header tag
        h1 = soup.find('h1')
        if h1:
            return h1.text.strip()
            
        return ''
    
    def _extract_description(self, soup):
        """Extract description from soup."""
        # Try meta description
        meta_desc = soup.find('meta', attrs={'name': 'description'})
        if meta_desc:
            return meta_desc.get('content', '').strip()
            
        # Try OpenGraph
        og_desc = soup.find('meta', property='og:description')
        if og_desc:
            return og_desc.get('content', '').strip()
            
        return ''
    
    def _extract_canonical_url(self, soup):
        """Extract canonical URL from soup."""
        canonical = soup.find('link', rel='canonical')
        if canonical:
            return canonical.get('href', '')
            
        # Try OpenGraph
        og_url = soup.find('meta', property='og:url')
        if og_url:
            return og_url.get('content', '')
            
        return None
    
    def _extract_author(self, soup):
        """Extract author from soup."""
        # Try meta author
        meta_author = soup.find('meta', attrs={'name': 'author'})
        if meta_author:
            return meta_author.get('content', '').strip()
            
        # Try schema.org
        author_elem = soup.find(itemtype="http://schema.org/Person")
        if author_elem:
            name_elem = author_elem.find(itemprop="name")
            if name_elem:
                return name_elem.text.strip()
                
        # Try article:author
        article_author = soup.find('meta', property='article:author')
        if article_author:
            return article_author.get('content', '').strip()
            
        return ''
    
    def _extract_published_date(self, soup):
        """Extract published date from soup."""
        # Try meta date
        meta_date = soup.find('meta', property='article:published_time')
        if meta_date:
            return meta_date.get('content', '')
            
        # Try time element
        time_elem = soup.find('time')
        if time_elem and time_elem.has_attr('datetime'):
            return time_elem['datetime']
            
        # Try schema.org datePublished
        date_published = soup.find(itemprop='datePublished')
        if date_published and date_published.has_attr('content'):
            return date_published['content']
            
        return ''
    
    def _extract_modified_date(self, soup):
        """Extract modified date from soup."""
        # Try meta date
        meta_date = soup.find('meta', property='article:modified_time')
        if meta_date:
            return meta_date.get('content', '')
            
        # Try schema.org dateModified
        date_modified = soup.find(itemprop='dateModified')
        if date_modified and date_modified.has_attr('content'):
            return date_modified['content']
            
        return ''
    
    def _extract_site_name(self, soup):
        """Extract site name from soup."""
        # Try OpenGraph site_name
        og_site_name = soup.find('meta', property='og:site_name')
        if og_site_name:
            return og_site_name.get('content', '').strip()
            
        return ''
    
    def _extract_favicon(self, soup, base_url):
        """Extract favicon URL from soup."""
        parsed_base = urlparse(base_url)
        base_domain = f"{parsed_base.scheme}://{parsed_base.netloc}"
        
        # Try link rel="icon"
        icon_link = soup.find('link', rel=lambda x: x and ('icon' in x.lower()))
        if icon_link and icon_link.has_attr('href'):
            href = icon_link['href']
            # Resolve relative URLs
            if href.startswith('//'):
                return f"{parsed_base.scheme}:{href}"
            elif href.startswith('/'):
                return f"{base_domain}{href}"
            elif not href.startswith(('http://', 'https://')):
                return f"{base_domain}/{href}"
            return href
            
        # Default favicon location
        return f"{base_domain}/favicon.ico"
    
    def _extract_language(self, soup):
        """Extract language from soup."""
        # Try html lang attribute
        html_tag = soup.find('html')
        if html_tag and html_tag.has_attr('lang'):
            return html_tag['lang']
            
        # Try meta content-language
        meta_lang = soup.find('meta', attrs={'http-equiv': 'content-language'})
        if meta_lang:
            return meta_lang.get('content', '')
            
        return ''
    
    def _extract_opengraph_data(self, soup):
        """Extract OpenGraph metadata."""
        og_meta = {}
        og_tags = soup.find_all('meta', property=lambda x: x and x.startswith('og:'))
        
        for tag in og_tags:
            property_name = tag.get('property', '')[3:]  # Remove 'og:' prefix
            content = tag.get('content', '')
            og_meta[property_name] = content
            
        return og_meta if og_meta else None
    
    def _extract_twitter_card_data(self, soup):
        """Extract Twitter Card metadata."""
        twitter_meta = {}
        twitter_tags = soup.find_all('meta', attrs={'name': lambda x: x and x.startswith('twitter:')})
        
        for tag in twitter_tags:
            property_name = tag.get('name', '')[8:]  # Remove 'twitter:' prefix
            content = tag.get('content', '')
            twitter_meta[property_name] = content
            
        return twitter_meta if twitter_meta else None
    
    def _extract_json_ld(self, soup):
        """Extract JSON-LD structured data."""
        json_ld_scripts = soup.find_all('script', type='application/ld+json')
        results = []
        
        for script in json_ld_scripts:
            try:
                data = json.loads(script.string)
                results.append(data)
            except (json.JSONDecodeError, AttributeError):
                pass
                
        return results if results else None
    
    def _extract_content(self, soup, url):
        """
        Extract main content from soup.
        
        Returns:
            tuple: (html_content, text_content)
        """
        # Make a copy of the soup to avoid modifying the original
        content_soup = BeautifulSoup(str(soup), 'html.parser')
        
        # Remove unwanted elements
        for element in content_soup.select('''
            script, style, nav, footer, header, aside, iframe,
            [role="banner"], [role="navigation"], [role="complementary"], [role="contentinfo"],
            .nav, .navigation, .menu, .footer, .header, .sidebar, .comments, 
            .ad, .advertisement, .banner, .social, .share, .related, 
            #comments, #sidebar, #footer, #header, #navigation
        '''):
            element.decompose()
        
        # Define strategies for content extraction in priority order
        strategies = [
            # Check for common content containers by special attribute
            (lambda s: s.find(attrs={"itemprop": "articleBody"})),
            (lambda s: s.find(attrs={"itemprop": "text"})),
            
            # Check for common content elements
            (lambda s: s.find('article')),
            (lambda s: s.find('main')),
            
            # Check for common content container IDs
            (lambda s: s.find(id=re.compile(r'content|main-content|article-content|post-content|entry-content', re.I))),
            
            # Check for common content container classes
            (lambda s: s.find(class_=re.compile(r'content|main-content|article-content|post-content|entry-content|article|post|entry', re.I))),
            
            # Check for more generic content containers
            (lambda s: s.find(class_=re.compile(r'text|body|main|container', re.I))),
        ]
        
        # Try each strategy until one succeeds
        content_elem = None
        for strategy in strategies:
            content_elem = strategy(content_soup)
            if content_elem:
                break
                
        # If no content found with the strategies, use the body
        if not content_elem:
            content_elem = content_soup.find('body')
            
        # If still no content, use the whole soup
        if not content_elem:
            content_elem = content_soup
        
        # Extract HTML and text content
        html_content = str(content_elem)
        text_content = content_elem.get_text(separator='\n\n').strip()
        
        return html_content, text_content
    
    def _extract_images(self, soup, base_url):
        """Extract images from soup."""
        images = []
        
        # Parse the base URL for relative URLs
        parsed_base = urlparse(base_url)
        base_domain = f"{parsed_base.scheme}://{parsed_base.netloc}"
        
        # Function to resolve relative URLs
        def resolve_url(url):
            if url.startswith('//'):
                return f"{parsed_base.scheme}:{url}"
            elif url.startswith('/'):
                return f"{base_domain}{url}"
            elif not url.startswith(('http://', 'https://')):
                return f"{base_domain}/{url}"
            return url
        
        # Find all image tags
        img_tags = soup.find_all('img')
        
        for img in img_tags:
            # Skip tiny images, icons, etc.
            if img.has_attr('width') and img.has_attr('height'):
                try:
                    width = int(img['width'])
                    height = int(img['height'])
                    if width < 100 or height < 100:
                        continue
                except (ValueError, TypeError):
                    pass
            
            # Get image URL
            img_url = None
            
            # Try data-src first (lazy loading)
            if img.has_attr('data-src'):
                img_url = img['data-src']
            # Try srcset
            elif img.has_attr('srcset'):
                srcset = img['srcset'].split(',')[0].strip().split(' ')[0]
                img_url = srcset
            # Then try src
            elif img.has_attr('src'):
                img_url = img['src']
            
            # Skip data URLs and empty URLs
            if not img_url or img_url.startswith('data:') or len(img_url) < 5:
                continue
                
            # Resolve relative URLs
            img_url = resolve_url(img_url)
            
            # Get alt text and figure caption if available
            alt_text = img.get('alt', '')
            caption = ""
            
            # Look for figure caption
            parent_figure = img.find_parent('figure')
            if parent_figure:
                caption_elem = parent_figure.find('figcaption')
                if caption_elem:
                    caption = caption_elem.get_text().strip()
            
            # Extract context - look for nearby headings
            context = ""
            prev_heading = img.find_previous(['h1', 'h2', 'h3', 'h4', 'h5', 'h6'])
            if prev_heading:
                context = prev_heading.get_text().strip()
            
            images.append({
                'url': img_url,
                'alt': alt_text,
                'caption': caption,
                'context': context
            })
        
        # Also look for OpenGraph image
        og_image = soup.find('meta', property='og:image')
        if og_image and og_image.has_attr('content'):
            img_url = og_image['content']
            img_url = resolve_url(img_url)
            
            # Check if already in list
            if not any(img['url'] == img_url for img in images):
                images.append({
                    'url': img_url,
                    'alt': 'OpenGraph image',
                    'caption': '',
                    'context': 'Featured Image'
                })
        
        return images
    
    def _estimate_read_time(self, soup):
        """Estimate reading time in minutes based on word count."""
        word_count = self._count_words(soup)
        # Average reading speed: 200-250 words per minute
        reading_time = word_count / 225
        return max(1, round(reading_time))
    
    def _count_words(self, soup):
        """Count words in the document."""
        text = soup.get_text(separator=' ', strip=True)
        words = text.split()
        return len(words)
    
    def _create_enhanced_markdown(self, html_content, metadata, images):
        """Create enhanced markdown content with metadata and images."""
        markdown = ""
        
        # Add title
        if metadata.get('title'):
            markdown += f"# {metadata['title']}\n\n"
        
        # Add metadata section
        markdown += "## Article Information\n\n"
        
        if metadata.get('author'):
            markdown += f"**Author:** {metadata['author']}\n\n"
            
        if metadata.get('published_date'):
            markdown += f"**Published:** {metadata['published_date']}\n\n"
            
        if metadata.get('site_name'):
            markdown += f"**Source:** {metadata['site_name']}\n\n"
        elif metadata.get('domain'):
            markdown += f"**Source:** {metadata['domain']}\n\n"
            
        if metadata.get('read_time'):
            markdown += f"**Reading time:** {metadata['read_time']} minute(s)\n\n"
            
        # Add description as summary
        if metadata.get('description'):
            markdown += f"## Summary\n\n{metadata['description']}\n\n"
        
        # Add content section
        markdown += "## Content\n\n"
        
        # Convert HTML to markdown
        content_markdown = self.html_to_markdown.handle(html_content)
        markdown += content_markdown
        
        # Add featured images section if there are images
        if images:
            markdown += "\n\n## Images\n\n"
            
            # Limit to max 5 images to keep the markdown reasonable
            for img in images[:5]:
                markdown += f"![{img['alt']}]({img['url']})\n\n"
                if img['caption']:
                    markdown += f"*{img['caption']}*\n\n"
                elif img['context']:
                    markdown += f"*Context: {img['context']}*\n\n"
        
        return markdown
    
    def _get_cache_key(self, url):
        """Generate a cache key for a URL."""
        # Create a hash of the URL to use as the filename
        url_hash = hashlib.md5(url.encode('utf-8')).hexdigest()
        return url_hash
    
    def _check_cache(self, cache_key):
        """Check if a cache file exists."""
        cache_file = os.path.join(self.cache_dir, f"{cache_key}.json")
        return os.path.exists(cache_file)
    
    def _load_from_cache(self, cache_key):
        """Load cached data."""
        cache_file = os.path.join(self.cache_dir, f"{cache_key}.json")
        try:
            with open(cache_file, 'r', encoding='utf-8') as f:
                data = json.load(f)
                return data
        except Exception as e:
            logger.error(f"Error loading from cache: {str(e)}")
            return None
    
    def _save_to_cache(self, cache_key, data):
        """Save data to cache."""
        cache_file = os.path.join(self.cache_dir, f"{cache_key}.json")
        try:
            with open(cache_file, 'w', encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=False, indent=2)
        except Exception as e:
            logger.error(f"Error saving to cache: {str(e)}")
            

# Test the scraper if run directly
if __name__ == "__main__":
    import sys
    import argparse
    
    parser = argparse.ArgumentParser(description="Scrape content from a web URL")
    parser.add_argument("url", help="URL to scrape")
    parser.add_argument("--output", "-o", help="Output file (default: stdout)")
    parser.add_argument("--force-refresh", "-f", action="store_true", help="Force refresh cached content")
    parser.add_argument("--cache-dir", "-c", default="./web_cache", help="Cache directory path")
    
    args = parser.parse_args()
    
    scraper = WebScraper(cache_dir=args.cache_dir)
    result = scraper.scrape_url(args.url, force_refresh=args.force_refresh)
    
    # Convert to JSON
    json_result = json.dumps(result, indent=2, ensure_ascii=False)
    
    # Output
    if args.output:
        with open(args.output, 'w', encoding='utf-8') as f:
            f.write(json_result)
        print(f"Results saved to {args.output}")
    else:
        print(json_result)