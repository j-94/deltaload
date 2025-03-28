"""Web scraper module for bookmark enrichment."""

import logging
import requests
from urllib.parse import urlparse
from bs4 import BeautifulSoup
import re

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s.%(msecs)03d %(levelname)s: %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)
logger = logging.getLogger(__name__)

class WebScraper:
    """Web scraper for retrieving and processing web content."""
    
    def __init__(self):
        """Initialize web scraper with default settings."""
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.9',
            'Connection': 'keep-alive',
            'Upgrade-Insecure-Requests': '1',
        }
        logger.info("WebScraper initialized")
    
    def scrape_url(self, url):
        """
        Scrape content from a web URL.
        
        Args:
            url: The URL to scrape
            
        Returns:
            Dictionary with scraped data
        """
        result = {
            'url': url,
            'source': 'web',
            'status': 'error',
            'content': '',
            'metadata': {}
        }
        
        try:
            logger.info(f"Scraping URL: {url}")
            
            # Fetch the URL
            response = requests.get(url, headers=self.headers, timeout=10)
            response.raise_for_status()
            
            # Parse HTML
            soup = BeautifulSoup(response.text, 'html.parser')
            
            # Extract metadata
            title = self._extract_title(soup)
            description = self._extract_description(soup)
            canonical_url = self._extract_canonical_url(soup)
            author = self._extract_author(soup)
            published_date = self._extract_published_date(soup)
            
            # Extract main content
            content = self._extract_content(soup)
            
            # Extract images
            images = self._extract_images(soup, url)
            
            # Determine domain
            domain = urlparse(url).netloc
            
            # Build metadata
            metadata = {
                'title': title,
                'description': description,
                'canonical_url': canonical_url or url,
                'author': author,
                'published_date': published_date,
                'domain': domain,
                'images': images
            }
            
            # Create markdown version of the content
            markdown_content = self._convert_to_markdown(content, title, description)
            
            # Update result
            result.update({
                'status': 'success',
                'content': content,
                'metadata': metadata,
                'markdown': markdown_content,
                'domain': domain
            })
            
            return result
            
        except requests.exceptions.RequestException as e:
            logger.error(f"Request error scraping {url}: {str(e)}")
            result['error'] = str(e)
            return result
        except Exception as e:
            logger.error(f"Error scraping {url}: {str(e)}")
            result['error'] = str(e)
            return result
    
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
            
        return ''
    
    def _extract_content(self, soup):
        """Extract main content from soup."""
        # Make a copy of the soup to avoid modifying the original
        content_soup = BeautifulSoup(str(soup), 'html.parser')
        
        # Remove unwanted elements
        for element in content_soup.select('script, style, nav, footer, header, aside, iframe, [role="banner"], [role="navigation"], .nav, .footer, .header, .sidebar, .ad, .advertisement'):
            element.decompose()
        
        # Strategy 1: Look for article element
        article = content_soup.find('article')
        if article:
            return article.get_text(separator='\n\n').strip()
            
        # Strategy 2: Look for main element
        main = content_soup.find('main')
        if main:
            return main.get_text(separator='\n\n').strip()
            
        # Strategy 3: Look for common content container IDs
        for id_value in ['content', 'main-content', 'article-content', 'post-content', 'entry-content']:
            content_div = content_soup.find(id=re.compile(id_value, re.I))
            if content_div:
                return content_div.get_text(separator='\n\n').strip()
        
        # Strategy 4: Look for common content container classes
        for class_value in ['content', 'main-content', 'article-content', 'post-content', 'entry-content', 'article', 'post', 'entry']:
            content_div = content_soup.find(class_=re.compile(class_value, re.I))
            if content_div:
                return content_div.get_text(separator='\n\n').strip()
        
        # If all else fails, get the body content
        body = content_soup.find('body')
        if body:
            return body.get_text(separator='\n\n').strip()
            
        # Final fallback
        return content_soup.get_text(separator='\n\n').strip()
    
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
            # Then try src
            elif img.has_attr('src'):
                img_url = img['src']
            
            if img_url and not img_url.startswith('data:'):
                # Resolve relative URLs
                img_url = resolve_url(img_url)
                
                # Get alt text
                alt_text = img.get('alt', '')
                
                images.append({
                    'url': img_url,
                    'alt': alt_text
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
                    'alt': 'OpenGraph image'
                })
        
        return images
    
    def _convert_to_markdown(self, content, title, description):
        """Convert HTML content to markdown-like text."""
        markdown = ""
        
        if title:
            markdown += f"# {title}\n\n"
        
        if description:
            markdown += f"*{description}*\n\n"
        
        # Split content into paragraphs
        paragraphs = [p.strip() for p in content.split('\n\n') if p.strip()]
        
        for p in paragraphs:
            markdown += f"{p}\n\n"
        
        return markdown

# Test the scraper if run directly
if __name__ == "__main__":
    import sys
    import argparse
    import json
    
    parser = argparse.ArgumentParser(description="Scrape content from a web URL")
    parser.add_argument("url", help="URL to scrape")
    parser.add_argument("--output", "-o", help="Output file (default: stdout)")
    
    args = parser.parse_args()
    
    scraper = WebScraper()
    result = scraper.scrape_url(args.url)
    
    # Convert to JSON
    json_result = json.dumps(result, indent=2, ensure_ascii=False)
    
    # Output
    if args.output:
        with open(args.output, 'w', encoding='utf-8') as f:
            f.write(json_result)
        print(f"Results saved to {args.output}")
    else:
        print(json_result)