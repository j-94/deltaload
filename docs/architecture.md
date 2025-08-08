# Architecture Overview

This project implements a modular delta load ETL pipeline for bookmark data.
It is composed of several pieces that work together to fetch, process, enrich,
and monitor bookmark information.

## Core Pipeline
- **`BookmarkDeltaETL`**: orchestrates extraction, transformation, and loading
  while tracking changes between runs.
- **Fetchers**: pluggable modules such as `RaindropFetcher` and `GitHubFetcher`
  pull bookmark data from different services.
- **`AIBookmarkEnricher`**: adds semantic analysis and metadata using AI
  models.

## Scheduling and Monitoring
- **`DeltaScheduler`**: runs the pipeline on a schedule, handles source
  fetching, optional AI enrichment, and report generation.
- **`delta-monitor.ts`**: collects statistics about processed bookmarks to aid
  in monitoring and reporting.

## Typical Workflow
1. Fetch bookmark sources.
2. Run the delta ETL to detect additions and updates.
3. Enrich changed bookmarks with AI-generated insights.
4. Generate daily reports and clean up old data.

For more usage examples, see the main [README](../README.md) and
[Delta Load Guide](../delta-load-guide.md).
