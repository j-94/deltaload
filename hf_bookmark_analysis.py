"""
HuggingFace Data Preparation Script for Bookmark Data

This script prepares bookmark data for upload to HuggingFace Data Studio by:
1. Reading the data-bookmark.jsonl file
2. Transforming it into a format suitable for HuggingFace datasets
3. Creating a metadata.json file with column information
4. Saving the data in a format ready for upload
"""

import json
import os
import pandas as pd
from pathlib import Path
import logging
import datetime

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s.%(msecs)03d %(levelname)s: %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)
logger = logging.getLogger(__name__)

def load_bookmark_data(filepath):
    """Load bookmark data from JSONL file."""
    logger.info(f"Loading bookmark data from {filepath}")
    
    bookmarks = []
    with open(filepath, 'r', encoding='utf-8') as f:
        for line in f:
            try:
                bookmarks.append(json.loads(line))
            except json.JSONDecodeError:
                logger.error(f"Error parsing line: {line[:100]}...")
    
    logger.info(f"Loaded {len(bookmarks)} bookmarks")
    return bookmarks

def parse_metadata(metadata):
    """Parse metadata string or dict to extract useful information."""
    if isinstance(metadata, str):
        try:
            metadata = json.loads(metadata)
        except json.JSONDecodeError:
            return {}
    
    if not metadata or not isinstance(metadata, dict):
        return {}
    
    return metadata

def extract_source_metadata(bookmark):
    """Extract source-specific metadata for different bookmark types."""
    source = bookmark.get('source', '')
    metadata = parse_metadata(bookmark.get('metadata', {}))
    result = {}
    
    # Twitter-specific metadata
    if source in ['twitter', 'twitter_like']:
        # Extract common Twitter fields
        if 'username' in metadata:
            result['twitter_username'] = metadata['username']
        if 'name' in metadata:
            result['twitter_name'] = metadata['name']
        if 'followers_count' in metadata:
            result['twitter_followers'] = metadata['followers_count']
        
        # Extract tweet metrics if available
        if 'favorite_count' in metadata:
            result['twitter_likes'] = metadata['favorite_count']
        if 'retweet_count' in metadata:
            result['twitter_retweets'] = metadata['retweet_count']
        if 'reply_count' in metadata:
            result['twitter_replies'] = metadata['reply_count']
            
    # GitHub-specific metadata
    elif source == 'github':
        if 'full_name' in metadata:
            result['github_repo'] = metadata['full_name']
        if 'stargazers_count' in metadata:
            result['github_stars'] = metadata['stargazers_count']
        if 'forks_count' in metadata:
            result['github_forks'] = metadata['forks_count']
        if 'owner' in metadata and isinstance(metadata['owner'], dict):
            result['github_owner'] = metadata['owner'].get('login')
        if 'language' in metadata:
            result['github_language'] = metadata['language']
            
    # Raindrop.io-specific metadata
    elif source == 'raindrop':
        if 'domain' in metadata:
            result['raindrop_domain'] = metadata['domain']
        if 'tags' in metadata and isinstance(metadata['tags'], list):
            result['raindrop_tags'] = metadata['tags']
            
    return result

def transform_for_huggingface(bookmarks):
    """Transform bookmark data into a format suitable for HuggingFace datasets."""
    logger.info("Transforming data for HuggingFace format")
    
    records = []
    for bookmark in bookmarks:
        # Extract basic information
        record = {
            "id": bookmark.get('id'),
            "source": bookmark.get('source', ''),
            "title": bookmark.get('title', ''),
            "url": bookmark.get('url', ''),
            "content": bookmark.get('content', ''),
            "created_at": bookmark.get('created_at', ''),
        }
        
        # Extract and flatten useful metadata
        source_metadata = extract_source_metadata(bookmark)
        record.update(source_metadata)
        
        # Extract top-level domain for analysis
        if record['url']:
            try:
                from urllib.parse import urlparse
                domain = urlparse(record['url']).netloc
                record['domain'] = domain
            except Exception:
                record['domain'] = ''
        
        # Add content length as a feature
        record['content_length'] = len(record['content']) if record['content'] else 0
        
        # Convert dates to standard format if possible
        if record['created_at']:
            try:
                if isinstance(record['created_at'], str):
                    dt = pd.to_datetime(record['created_at'])
                    record['created_at'] = dt.isoformat()
                    record['year'] = dt.year
                    record['month'] = dt.month
            except Exception:
                # Keep original if parsing fails
                pass
        
        records.append(record)
    
    logger.info(f"Transformed {len(records)} bookmarks")
    return records

def create_huggingface_dataset(records, output_dir):
    """Create dataset files in HuggingFace format."""
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)
    
    # Convert to DataFrame for easier manipulation
    df = pd.DataFrame(records)
    
    # Sort by creation date for better browsing
    if 'created_at' in df.columns:
        df = df.sort_values("created_at", ascending=False)
    
    # Save as JSONL (the format HuggingFace accepts)
    data_path = output_path / "data.jsonl"
    with open(data_path, 'w', encoding='utf-8') as f:
        for record in df.to_dict(orient='records'):
            # Convert any non-serializable objects to strings
            clean_record = {}
            for k, v in record.items():
                if isinstance(v, (str, int, float, bool, type(None))):
                    clean_record[k] = v
                elif isinstance(v, list):
                    # Handle lists of strings
                    try:
                        clean_record[k] = [str(item) if not isinstance(item, (str, int, float, bool, type(None))) else item for item in v]
                    except Exception:
                        clean_record[k] = str(v)
                else:
                    clean_record[k] = str(v)
                    
            json.dump(clean_record, f, ensure_ascii=False)
            f.write('\n')
    
    # Create a metadata.json file
    metadata = {
        "dataset_info": {
            "description": "Bookmarks collected from various sources including Twitter, GitHub, and Raindrop.io",
            "citation": "",
            "homepage": "",
            "license": "",
            "features": {
                "id": {"dtype": "int64", "description": "Unique identifier for the bookmark"},
                "source": {"dtype": "string", "description": "Source of the bookmark (twitter, github, raindrop, etc.)"},
                "title": {"dtype": "string", "description": "Title of the bookmark"},
                "url": {"dtype": "string", "description": "URL of the bookmark"},
                "content": {"dtype": "string", "description": "Content of the bookmark"},
                "created_at": {"dtype": "string", "description": "Creation date of the bookmark"},
                "domain": {"dtype": "string", "description": "Domain of the URL"},
                "content_length": {"dtype": "int64", "description": "Length of the content in characters"},
                "year": {"dtype": "int64", "description": "Year the bookmark was created"},
                "month": {"dtype": "int64", "description": "Month the bookmark was created"},
                
                # Twitter-specific fields
                "twitter_username": {"dtype": "string", "description": "Twitter username"},
                "twitter_name": {"dtype": "string", "description": "Twitter display name"},
                "twitter_followers": {"dtype": "int64", "description": "Number of Twitter followers"},
                "twitter_likes": {"dtype": "int64", "description": "Number of likes on the tweet"},
                "twitter_retweets": {"dtype": "int64", "description": "Number of retweets"},
                "twitter_replies": {"dtype": "int64", "description": "Number of replies to the tweet"},
                
                # GitHub-specific fields
                "github_repo": {"dtype": "string", "description": "GitHub repository name"},
                "github_stars": {"dtype": "int64", "description": "Number of stars on the GitHub repository"},
                "github_forks": {"dtype": "int64", "description": "Number of forks of the GitHub repository"},
                "github_owner": {"dtype": "string", "description": "Owner of the GitHub repository"},
                "github_language": {"dtype": "string", "description": "Primary language of the GitHub repository"},
                
                # Raindrop-specific fields
                "raindrop_domain": {"dtype": "string", "description": "Domain saved in Raindrop.io"},
                "raindrop_tags": {
                    "dtype": "list", 
                    "description": "Tags associated with the Raindrop bookmark",
                    "sequence": {"dtype": "string"}
                }
            }
        }
    }
    
    metadata_path = output_path / "metadata.json"
    with open(metadata_path, 'w', encoding='utf-8') as f:
        json.dump(metadata, f, indent=2, ensure_ascii=False)
    
    # Create a README.md file
    readme = f"""# Bookmark Dataset

A collection of {len(df)} bookmarks from various sources including Twitter, GitHub, and Raindrop.io.

## Dataset Description

This dataset contains bookmarks collected from various sources. Each record includes:

- Basic bookmark information (ID, title, URL, content)
- Source-specific metadata (Twitter metrics, GitHub repository info, etc.)
- Temporal information (creation date, year, month)
- Content analysis features (domain, content length)

## Source Distribution

```
{df['source'].value_counts().to_string()}
```

## Top Domains

```
{df['domain'].value_counts().head(10).to_string()}
```

## Usage

This dataset can be used for:

- Analyzing bookmark patterns and trends
- Understanding content consumption across different platforms
- Training recommendation systems
- Studying information organization

## Data Format

The dataset is provided in JSONL format with fields for common attributes and source-specific metadata.

Generated on: {datetime.datetime.now().strftime('%Y-%m-%d')}
"""
    
    readme_path = output_path / "README.md"
    with open(readme_path, 'w', encoding='utf-8') as f:
        f.write(readme)
    
    logger.info(f"Created HuggingFace dataset files in {output_path}")
    logger.info(f"  - data.jsonl: {len(df)} records")
    logger.info(f"  - metadata.json: Dataset schema")
    logger.info(f"  - README.md: Dataset documentation")
    
    return {
        "data_path": str(data_path),
        "record_count": len(df),
        "output_dir": str(output_path)
    }

def main():
    """Main execution function."""
    # Input and output paths
    bookmark_data_path = "/Users/imac/Desktop/ETL/deltaload/data-bookmark.jsonl"
    output_dir = "/Users/imac/Desktop/ETL/deltaload/hf_bookmarks_dataset"
    
    # Create timestamp for the output
    timestamp = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
    output_dir = f"{output_dir}_{timestamp}"
    
    # Load and transform the data
    bookmarks = load_bookmark_data(bookmark_data_path)
    records = transform_for_huggingface(bookmarks)
    
    # Create the HuggingFace dataset
    result = create_huggingface_dataset(records, output_dir)
    
    logger.info("\nDataset ready for upload to HuggingFace!")
    logger.info(f"To upload, run:")
    logger.info(f"  1. Install the Hugging Face CLI: pip install huggingface_hub")
    logger.info(f"  2. Login to HuggingFace: huggingface-cli login")
    logger.info(f"  3. Create a new dataset on HuggingFace and push your data:")
    logger.info(f"     huggingface-cli upload-folder {result['output_dir']} your-username/bookmarks-dataset")
    
    # Create a python analysis script in the output directory
    analysis_script = """
import json
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path
import seaborn as sns

# Set style
plt.style.use('ggplot')
sns.set(style="whitegrid")

# Load the data
data_path = Path("data.jsonl")
bookmarks = []
with open(data_path, 'r', encoding='utf-8') as f:
    for line in f:
        bookmarks.append(json.loads(line))

# Convert to DataFrame
df = pd.DataFrame(bookmarks)

print(f"Loaded {len(df)} bookmarks")

# Basic statistics
print("\\nSource Distribution:")
source_counts = df['source'].value_counts()
print(source_counts)

print("\\nTop Domains:")
domain_counts = df['domain'].value_counts().head(20)
print(domain_counts)

# Create output directory for plots
plots_dir = Path("plots")
plots_dir.mkdir(exist_ok=True)

# Source distribution pie chart
plt.figure(figsize=(10, 7))
source_counts.plot.pie(autopct='%1.1f%%', textprops={'fontsize': 10})
plt.title('Bookmark Sources', fontsize=14)
plt.ylabel('')
plt.savefig(plots_dir / 'source_distribution.png', bbox_inches='tight')
plt.close()
print("Created source distribution chart: plots/source_distribution.png")

# Top domains bar chart
plt.figure(figsize=(12, 8))
domain_counts.head(15).plot.barh()
plt.title('Top 15 Domains', fontsize=14)
plt.xlabel('Count')
plt.ylabel('Domain')
plt.tight_layout()
plt.savefig(plots_dir / 'top_domains.png', bbox_inches='tight')
plt.close()
print("Created top domains chart: plots/top_domains.png")

# Bookmarks by month (if date data is available)
if 'created_at' in df.columns:
    try:
        # Convert to datetime if not already
        if not pd.api.types.is_datetime64_any_dtype(df['created_at']):
            df['created_at'] = pd.to_datetime(df['created_at'], errors='coerce')
        
        # Extract year and month
        df['year_month'] = df['created_at'].dt.to_period('M')
        
        # Count bookmarks by month
        monthly_counts = df.groupby('year_month').size()
        
        plt.figure(figsize=(14, 8))
        monthly_counts.plot.bar()
        plt.title('Bookmarks by Month', fontsize=14)
        plt.xlabel('Month')
        plt.ylabel('Count')
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.savefig(plots_dir / 'bookmarks_by_month.png', bbox_inches='tight')
        plt.close()
        print("Created bookmarks by month chart: plots/bookmarks_by_month.png")
        
        # Bookmarks by source over time
        source_time = pd.crosstab(df['year_month'], df['source'])
        
        plt.figure(figsize=(14, 8))
        source_time.plot.area(alpha=0.6)
        plt.title('Bookmarks by Source Over Time', fontsize=14)
        plt.xlabel('Month')
        plt.ylabel('Count')
        plt.legend(title='Source')
        plt.tight_layout()
        plt.savefig(plots_dir / 'sources_over_time.png', bbox_inches='tight')
        plt.close()
        print("Created sources over time chart: plots/sources_over_time.png")
    except Exception as e:
        print(f"Error creating time-based charts: {e}")

# Content length distribution
if 'content_length' in df.columns:
    plt.figure(figsize=(12, 8))
    sns.histplot(df['content_length'].clip(upper=5000), bins=50)
    plt.title('Content Length Distribution (clipped at 5000 chars)', fontsize=14)
    plt.xlabel('Content Length (characters)')
    plt.ylabel('Count')
    plt.tight_layout()
    plt.savefig(plots_dir / 'content_length.png', bbox_inches='tight')
    plt.close()
    print("Created content length distribution: plots/content_length.png")

# Twitter-specific analysis
twitter_df = df[df['source'].isin(['twitter', 'twitter_like'])].copy()
if len(twitter_df) > 0 and 'twitter_followers' in twitter_df.columns:
    try:
        # Clean up numeric columns
        for col in ['twitter_followers', 'twitter_likes', 'twitter_retweets', 'twitter_replies']:
            if col in twitter_df.columns:
                twitter_df[col] = pd.to_numeric(twitter_df[col], errors='coerce')
        
        # Followers vs. engagement scatter plot
        if 'twitter_likes' in twitter_df.columns and twitter_df['twitter_likes'].notna().any():
            plt.figure(figsize=(12, 8))
            plt.scatter(twitter_df['twitter_followers'], twitter_df['twitter_likes'], alpha=0.5)
            plt.xscale('log')
            plt.yscale('log')
            plt.title('Twitter: Followers vs. Likes', fontsize=14)
            plt.xlabel('Followers (log scale)')
            plt.ylabel('Likes (log scale)')
            plt.tight_layout()
            plt.savefig(plots_dir / 'twitter_followers_vs_likes.png', bbox_inches='tight')
            plt.close()
            print("Created Twitter followers vs. likes chart: plots/twitter_followers_vs_likes.png")
    except Exception as e:
        print(f"Error creating Twitter charts: {e}")

# GitHub-specific analysis
github_df = df[df['source'] == 'github'].copy()
if len(github_df) > 0 and 'github_stars' in github_df.columns:
    try:
        # Clean up numeric columns
        for col in ['github_stars', 'github_forks']:
            if col in github_df.columns:
                github_df[col] = pd.to_numeric(github_df[col], errors='coerce')
        
        # Stars distribution
        if 'github_stars' in github_df.columns and github_df['github_stars'].notna().any():
            plt.figure(figsize=(12, 8))
            sns.histplot(github_df['github_stars'].clip(upper=10000), bins=50)
            plt.title('GitHub: Stars Distribution (clipped at 10000)', fontsize=14)
            plt.xlabel('Stars')
            plt.ylabel('Count')
            plt.tight_layout()
            plt.savefig(plots_dir / 'github_stars.png', bbox_inches='tight')
            plt.close()
            print("Created GitHub stars distribution: plots/github_stars.png")
            
        # Top languages pie chart
        if 'github_language' in github_df.columns:
            lang_counts = github_df['github_language'].value_counts().head(10)
            plt.figure(figsize=(12, 8))
            lang_counts.plot.pie(autopct='%1.1f%%', textprops={'fontsize': 10})
            plt.title('Top GitHub Languages', fontsize=14)
            plt.ylabel('')
            plt.tight_layout()
            plt.savefig(plots_dir / 'github_languages.png', bbox_inches='tight')
            plt.close()
            print("Created GitHub languages chart: plots/github_languages.png")
    except Exception as e:
        print(f"Error creating GitHub charts: {e}")

print("\\nAnalysis complete. Check the 'plots' directory for visualizations.")
"""
    
    analysis_path = Path(output_dir) / "analyze_bookmarks.py"
    with open(analysis_path, 'w', encoding='utf-8') as f:
        f.write(analysis_script)
    
    logger.info(f"Created analysis script at {analysis_path}")
    
    return result

if __name__ == "__main__":
    main()