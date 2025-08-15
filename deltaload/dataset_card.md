---
license: apache-2.0
tags:
- bookmarks
- twitter
- github
- raindrop
datasets:
- J94/bookmarks-dataset
language:
- en
---

# Dataset Card for Bookmarks Collection

## Dataset Description

### Dataset Summary

This dataset contains a personal collection of bookmarks from various sources including Twitter, GitHub, and Raindrop.io. It provides a comprehensive view of web content consumption patterns across different platforms, with rich metadata for each source type.

The dataset includes 11,783 bookmark records with content and metadata spanning social media posts, code repositories, articles, and other web content.

### Languages

The dataset primarily contains content in English.

## Dataset Structure

### Data Instances

Each record in the dataset represents a single bookmark with the following structure:

```json
{
  "id": 11783,
  "source": "twitter_like",
  "title": "Example Title",
  "url": "https://twitter.com/username/status/123456789",
  "content": "The actual content of the bookmark...",
  "created_at": "2025-03-28T12:25:57.718145+00:00",
  "domain": "twitter.com",
  "content_length": 301,
  "year": 2025,
  "month": 3,
  "twitter_username": "username",
  "twitter_likes": 42,
  "twitter_retweets": 7,
  "twitter_replies": 3
}
```

Different fields are available depending on the source type:

- **Twitter** bookmarks include engagement metrics and user information
- **GitHub** bookmarks include repository stars, forks, and programming language
- **Raindrop.io** bookmarks include tags and domain information

### Data Fields

#### Common Fields
- `id`: Unique identifier for the bookmark
- `source`: Source of the bookmark (twitter, github, raindrop, etc.)
- `title`: Title of the bookmark
- `url`: URL of the bookmark
- `content`: Content of the bookmark
- `created_at`: Creation date of the bookmark
- `domain`: Domain of the URL
- `content_length`: Length of the content in characters
- `year`: Year the bookmark was created
- `month`: Month the bookmark was created

#### Twitter-specific Fields
- `twitter_username`: Twitter username
- `twitter_name`: Twitter display name
- `twitter_followers`: Number of followers of the author
- `twitter_likes`: Number of likes on the tweet
- `twitter_retweets`: Number of retweets
- `twitter_replies`: Number of replies to the tweet

#### GitHub-specific Fields
- `github_repo`: GitHub repository name
- `github_stars`: Number of stars on the GitHub repository
- `github_forks`: Number of forks of the GitHub repository
- `github_owner`: Owner of the GitHub repository
- `github_language`: Primary language of the GitHub repository

#### Raindrop-specific Fields
- `raindrop_domain`: Domain saved in Raindrop.io
- `raindrop_tags`: Tags associated with the Raindrop bookmark

### Data Splits

The dataset does not have explicit splits and is provided as a single collection.

## Dataset Creation

### Curation Rationale

This dataset was created to:
1. Analyze personal content consumption patterns across different platforms
2. Enable exploration of bookmark metadata and content
3. Provide a structured dataset for recommendation systems research
4. Study information organization and retrieval strategies

### Source Data

#### Initial Data Collection and Normalization

The data was collected using the following sources:
- Twitter API for tweets and likes
- GitHub API for starred repositories
- Raindrop.io API for saved bookmarks

Data from these disparate sources was normalized into a consistent format with source-specific metadata preserved in dedicated fields.

#### Who are the source language producers?

The content comes from various creators across the web, including Twitter users, GitHub repository owners, and website authors whose content was bookmarked via Raindrop.io.

### Annotations

The dataset does not contain manual annotations beyond the metadata provided by the source APIs and the categorization by source.

## Considerations for Using the Data

### Social Impact of Dataset

This dataset represents personal information consumption patterns and can be used to study how individuals organize and consume digital content. It may provide insights into effective information management strategies.

### Discussion of Biases

The dataset reflects the personal interests and content consumption preferences of a single individual, so it contains inherent biases toward specific topics, creators, and platforms.

### Other Known Limitations

- Some fields may contain missing values depending on what was available from the source API
- Content may be truncated in some cases due to API limitations
- The dataset only includes publicly accessible content

## Additional Information

### Dataset Curators

This dataset was curated by J94.

### Licensing Information

This dataset is released under the Apache 2.0 License.

### Citation Information

If you use this dataset in your research, please cite:

```
@dataset{bookmarks_dataset,
  author    = {J94},
  title     = {Bookmarks Dataset},
  year      = {2025},
  publisher = {Hugging Face},
  howpublished = {\url{https://huggingface.co/datasets/J94/bookmarks-dataset}}
}
```

### Contributions

This dataset welcomes community contributions to improve the documentation, enhance the metadata, or add additional analysis tools.