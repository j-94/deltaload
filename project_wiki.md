# Social Media Data Collector

This project provides tools and automated processes for collecting and managing data from various online sources such as Twitter, GitHub, and Raindrop.io. It allows users to fetch Twitter threads, aggregate personal activity (likes, stars, bookmarks), and maintain an updated collection of this data.

## Twitter Thread Fetcher

The Twitter Thread Fetcher is a command-line tool designed to download entire Twitter/X threads.

**Purpose:** To fetch the complete content of a Twitter/X thread, including all replies and media.

**Usage:** The tool can be run from the command line by providing a Twitter/X URL or a specific tweet ID.

**Key Capabilities:**

*   **Content Extraction:** Retrieves the full text content of each tweet in the thread.
*   **Media URL Extraction:** Identifies and extracts URLs for images and videos embedded in the thread.
*   **Metadata Extraction:** Gathers metadata associated with the thread, such as engagement statistics (likes, retweets, replies) and author information.
*   **URL Handling:** Supports various URL formats, including those from both `twitter.com` and `x.com` domains.
*   **Command-Line Interface:** Offers a user-friendly command-line interface for easy operation.

**Script Location:** The script for this tool can be found at `tools/twitter_thread_fetcher.py`.

## Multi-Source Data Aggregation (Deltaload Pipeline)

The Multi-Source Data Aggregation feature, also known as the Deltaload Pipeline, automates the collection and aggregation of personal activity data from various online platforms.

**Purpose:** To periodically fetch and consolidate data from multiple sources, ensuring an up-to-date collection of personal online activities.

**Data Sources:**

*   **Twitter:** Fetches tweets and likes. Note: This relies on a local cache of Twitter data.
*   **GitHub:** Retrieves repositories starred by the user.
*   **Raindrop.io:** Collects bookmarks saved by the user.

**Key Mechanism:** The pipeline employs a delta loading strategy. This means it only fetches items that are new since the last time the script was run, making the process efficient and reducing redundant data collection.

**Output:** The aggregated data is stored in a JSONL file named `data-bookmark.jsonl`. Each line in this file represents a single data item (e.g., a tweet, a starred repository, a bookmark).

**API Credentials:** To access data from these platforms, the script requires API credentials. These must be configured as environment variables for the respective services (Twitter, GitHub, Raindrop.io).

**Script Location:** The script for this pipeline is located at `deltaload.py`.

## Automated Hourly Updates

This feature ensures that the aggregated data from various sources is kept up-to-date automatically.

**Purpose:** To automate the execution of the Multi-Source Data Aggregation (Deltaload Pipeline) process.

**How it Works:** The automation is achieved using GitHub Actions, which is configured to run the `deltaload.py` script. This script fetches new data from the configured sources (Twitter, GitHub, Raindrop.io).

**Schedule:** The GitHub Actions workflow is scheduled to run every hour.

**Outcome:** As a result of this automated process, the `data-bookmark.jsonl` file within the repository is automatically updated with the latest aggregated data. This ensures that the collected information is always current.

**Workflow File Location:** The configuration for this automated task can be found in the GitHub Actions workflow file located at `.github/workflows/hourly.yml`.
