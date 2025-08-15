#!/usr/bin/env python3
"""
Comprehensive ETL Pipeline for Deltaload

This script orchestrates the entire ETL process:
1. Runs deltaload to fetch latest data
2. Enriches bookmarks as necessary
3. Performs quality checks on the dataset
4. Updates documentation with runtime stats
5. Prepares PR content
"""

import os
import sys
import json
import logging
import argparse
import subprocess
from datetime import datetime
from pathlib import Path
import concurrent.futures
from typing import Dict, List, Optional, Tuple

# Add project root to path to ensure modules are importable
sys.path.insert(0, str(Path(__file__).parent.parent))

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s.%(msecs)03d %(levelname)s: %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    handlers=[
        logging.FileHandler("pipeline/logs/etl_pipeline.log"),
        logging.StreamHandler(sys.stdout)
    ]
)
logger = logging.getLogger(__name__)

# Path Configuration
BASE_DIR = Path(__file__).parent.parent
DATA_PATH = BASE_DIR / "data-bookmark.jsonl"
TWITTER_PROCESSED_PATH = BASE_DIR / "data-bookmark-twitter-processed.jsonl"
ENRICHED_DATA_PATH = BASE_DIR / "data-bookmark-enriched.jsonl"
FINAL_DATA_PATH = BASE_DIR / "data-bookmark-final.jsonl"
STATS_PATH = BASE_DIR / "pipeline/stats.json"
README_PATH = BASE_DIR / "README.md"
PR_README_PATH = BASE_DIR / "PR_README.md"

class ETLPipeline:
    """Main ETL Pipeline orchestrator."""
    
    def __init__(self, args):
        """Initialize pipeline with command-line arguments."""
        self.args = args
        self.stats = {
            "start_time": datetime.now().isoformat(),
            "pipeline_version": "1.0.0",
            "steps": {}
        }
        
    def run(self):
        """Run the full ETL pipeline."""
        try:
            logger.info("Starting ETL Pipeline")
            
            # 1. Run Deltaload
            if not self.args.skip_deltaload:
                self.run_deltaload()
            else:
                logger.info("Skipping Deltaload step as requested")
                
            # 2. Process Twitter Data
            if not self.args.skip_twitter_processing:
                self.process_twitter_data()
            else:
                logger.info("Skipping Twitter processing as requested")
                
            # 3. Enrich Data
            if not self.args.skip_enrichment:
                self.enrich_data()
            else:
                logger.info("Skipping enrichment step as requested")
                
            # 4. Perform Quality Checks
            if not self.args.skip_quality_check:
                self.perform_quality_checks()
            else:
                logger.info("Skipping quality checks as requested")
                
            # 5. Finalize Dataset
            self.finalize_dataset()
            
            # 6. Enhance with Full Text
            if not self.args.skip_full_text_enhancement:
                self.enhance_with_full_text()
            else:
                logger.info("Skipping full text enhancement as requested")
            
            # 7. Update Documentation
            if not self.args.skip_docs:
                self.update_documentation()
            else:
                logger.info("Skipping documentation update as requested")
                
            # 8. Save Stats
            self.stats["end_time"] = datetime.now().isoformat()
            self.save_stats()
                
            logger.info("ETL Pipeline completed successfully")
            return True
            
        except Exception as e:
            logger.error(f"ETL Pipeline failed: {str(e)}")
            import traceback
            logger.error(traceback.format_exc())
            self.stats["status"] = "failed"
            self.stats["error"] = str(e)
            self.stats["end_time"] = datetime.now().isoformat()
            self.save_stats()
            return False
            
    def run_deltaload(self):
        """Run the deltaload script to fetch latest data."""
        step_start = datetime.now()
        logger.info("Running Deltaload to fetch latest data")
        
        try:
            result = subprocess.run(
                [sys.executable, str(BASE_DIR / "deltaload.py")],
                check=True,
                capture_output=True,
                text=True
            )
            
            logger.info(f"Deltaload completed: {result.stdout.strip()}")
            
            # Check if data file exists
            if not DATA_PATH.exists():
                raise FileNotFoundError(f"Deltaload did not create data file at {DATA_PATH}")
                
            # Record stats
            self.stats["steps"]["deltaload"] = {
                "status": "success",
                "duration_seconds": (datetime.now() - step_start).total_seconds(),
                "output": result.stdout.strip()
            }
            
        except subprocess.CalledProcessError as e:
            logger.error(f"Deltaload failed with exit code {e.returncode}")
            logger.error(f"Stdout: {e.stdout}")
            logger.error(f"Stderr: {e.stderr}")
            self.stats["steps"]["deltaload"] = {
                "status": "failed",
                "duration_seconds": (datetime.now() - step_start).total_seconds(),
                "error": str(e),
                "stdout": e.stdout,
                "stderr": e.stderr
            }
            raise
        except Exception as e:
            logger.error(f"Error running deltaload: {str(e)}")
            self.stats["steps"]["deltaload"] = {
                "status": "failed",
                "duration_seconds": (datetime.now() - step_start).total_seconds(),
                "error": str(e)
            }
            raise
            
    def process_twitter_data(self):
        """Process Twitter data to fix common issues with content."""
        step_start = datetime.now()
        logger.info("Processing Twitter data to fix content issues")
        
        # Check if the input data exists
        if not DATA_PATH.exists():
            logger.error(f"Data file not found at {DATA_PATH}")
            self.stats["steps"]["twitter_processing"] = {
                "status": "failed",
                "duration_seconds": (datetime.now() - step_start).total_seconds(),
                "error": f"Data file not found at {DATA_PATH}"
            }
            raise FileNotFoundError(f"Data file not found at {DATA_PATH}")
            
        try:
            # Count bookmarks to process
            total_bookmarks = self.count_lines(DATA_PATH)
            logger.info(f"Found {total_bookmarks} bookmarks to process for Twitter fixes")
            
            # Import the TwitterProcessor
            try:
                from tools.twitter_processor import TwitterProcessor, load_bookmarks, save_bookmarks
                
                # Load bookmarks
                bookmarks = load_bookmarks(DATA_PATH)
                
                # Initialize processor
                cache_dir = str(BASE_DIR / "data")
                processor = TwitterProcessor(cache_dir=cache_dir, batch_size=50)
                
                # Process bookmarks
                logger.info("Starting Twitter content processing")
                processed_bookmarks = processor.process_bookmarks(
                    bookmarks,
                    fix_content=True, 
                    fix_retweets=True,
                    fix_truncated=not self.args.skip_truncated_tweets
                )
                
                # Save processed bookmarks
                save_bookmarks(processed_bookmarks, TWITTER_PROCESSED_PATH)
                
                # Get statistics
                stats = processor.get_stats()
                
                logger.info(f"Twitter processing complete for {stats['twitter_count']} bookmarks")
                logger.info(f"Fixed {stats['content_fixed_count']} content mismatches")
                logger.info(f"Fixed {stats['retweet_fixed_count']} retweets")
                logger.info(f"Found {stats['truncated_count']} truncated tweets")
                logger.info(f"Fixed {stats['truncated_fixed_count']} truncated tweets")
                logger.info(f"  - {stats['truncated_fixed_from_cache']} from cache")
                logger.info(f"  - {stats['truncated_fixed_from_api']} from API")
                
                # Record stats
                self.stats["steps"]["twitter_processing"] = {
                    "status": "success",
                    "duration_seconds": (datetime.now() - step_start).total_seconds(),
                    "total_bookmarks": total_bookmarks,
                    "twitter_count": stats["twitter_count"],
                    "content_fixed": stats["content_fixed_count"],
                    "retweets_fixed": stats["retweet_fixed_count"],
                    "truncated_count": stats["truncated_count"],
                    "truncated_fixed": stats["truncated_fixed_count"],
                    "fixed_from_cache": stats["truncated_fixed_from_cache"],
                    "fixed_from_api": stats["truncated_fixed_from_api"]
                }
                
            except ImportError as e:
                logger.error(f"Could not import TwitterProcessor: {str(e)}")
                logger.warning("Falling back to subprocess approach")
                
                # Run the twitter processing script as a subprocess
                cmd = [
                    sys.executable, 
                    str(BASE_DIR / "run_tweet_fixes.sh")
                ]
                
                result = subprocess.run(
                    cmd,
                    check=True,
                    capture_output=True,
                    text=True
                )
                
                logger.info(f"Twitter processing via subprocess completed: {result.stdout.strip()}")
                
                # Verify the output file exists
                if not Path(BASE_DIR / "data-bookmark-fixed-all.jsonl").exists():
                    raise FileNotFoundError(f"Twitter processing did not create output file")
                    
                # Copy the output file to our expected location
                import shutil
                shutil.copy2(BASE_DIR / "data-bookmark-fixed-all.jsonl", TWITTER_PROCESSED_PATH)
                
                # Record stats
                self.stats["steps"]["twitter_processing"] = {
                    "status": "success",
                    "duration_seconds": (datetime.now() - step_start).total_seconds(),
                    "total_bookmarks": total_bookmarks,
                    "method": "subprocess",
                    "output": result.stdout.strip()
                }
            
        except subprocess.CalledProcessError as e:
            logger.error(f"Twitter processing failed with exit code {e.returncode}")
            logger.error(f"Stdout: {e.stdout}")
            logger.error(f"Stderr: {e.stderr}")
            self.stats["steps"]["twitter_processing"] = {
                "status": "failed",
                "duration_seconds": (datetime.now() - step_start).total_seconds(),
                "error": str(e),
                "stdout": e.stdout,
                "stderr": e.stderr
            }
            raise
        except Exception as e:
            logger.error(f"Error processing Twitter data: {str(e)}")
            self.stats["steps"]["twitter_processing"] = {
                "status": "failed",
                "duration_seconds": (datetime.now() - step_start).total_seconds(),
                "error": str(e)
            }
            raise
    
    def enrich_data(self):
        """Enrich the bookmark data with external content."""
        step_start = datetime.now()
        logger.info("Enriching bookmark data")
        
        # Determine input file - use Twitter processed file if available
        input_path = TWITTER_PROCESSED_PATH if TWITTER_PROCESSED_PATH.exists() else DATA_PATH
        
        # Check if the input data exists
        if not input_path.exists():
            logger.error(f"Data file not found at {input_path}")
            self.stats["steps"]["enrichment"] = {
                "status": "failed",
                "duration_seconds": (datetime.now() - step_start).total_seconds(),
                "error": f"Data file not found at {input_path}"
            }
            raise FileNotFoundError(f"Data file not found at {input_path}")
            
        try:
            # Count bookmarks to enrich
            total_bookmarks = self.count_lines(input_path)
            logger.info(f"Found {total_bookmarks} bookmarks to process from {input_path}")
            
            # Run enrichment script
            cmd = [
                sys.executable, 
                str(BASE_DIR / "enrich_bookmarks.py"),
                str(input_path),
                "--output-file", str(ENRICHED_DATA_PATH),
                "--cache-dir", str(BASE_DIR / "cache")
            ]
            
            # Add optional arguments
            if self.args.force_refresh:
                cmd.append("--force-refresh")
                
            if self.args.enrichment_limit:
                cmd.extend(["--limit", str(self.args.enrichment_limit)])
                
            result = subprocess.run(
                cmd,
                check=True,
                capture_output=True,
                text=True
            )
            
            logger.info(f"Enrichment completed: {result.stdout.strip()}")
            
            # Verify the enriched file exists
            if not ENRICHED_DATA_PATH.exists():
                raise FileNotFoundError(f"Enrichment did not create output file at {ENRICHED_DATA_PATH}")
                
            # Count enriched bookmarks
            enriched_count = self.count_lines(ENRICHED_DATA_PATH)
            
            # Record stats
            self.stats["steps"]["enrichment"] = {
                "status": "success",
                "duration_seconds": (datetime.now() - step_start).total_seconds(),
                "total_bookmarks": total_bookmarks,
                "enriched_bookmarks": enriched_count,
                "output": result.stdout.strip()
            }
            
        except subprocess.CalledProcessError as e:
            logger.error(f"Enrichment failed with exit code {e.returncode}")
            logger.error(f"Stdout: {e.stdout}")
            logger.error(f"Stderr: {e.stderr}")
            self.stats["steps"]["enrichment"] = {
                "status": "failed",
                "duration_seconds": (datetime.now() - step_start).total_seconds(),
                "error": str(e),
                "stdout": e.stdout,
                "stderr": e.stderr
            }
            raise
        except Exception as e:
            logger.error(f"Error enriching data: {str(e)}")
            self.stats["steps"]["enrichment"] = {
                "status": "failed",
                "duration_seconds": (datetime.now() - step_start).total_seconds(),
                "error": str(e)
            }
            raise
            
    def perform_quality_checks(self):
        """Perform quality checks on the enriched data."""
        step_start = datetime.now()
        logger.info("Performing quality checks on enriched data")
        
        data_path = ENRICHED_DATA_PATH if ENRICHED_DATA_PATH.exists() else DATA_PATH
        
        if not data_path.exists():
            logger.error(f"No data file found for quality checks")
            self.stats["steps"]["quality_check"] = {
                "status": "failed",
                "duration_seconds": (datetime.now() - step_start).total_seconds(),
                "error": "No data file found for quality checks"
            }
            raise FileNotFoundError("No data file found for quality checks")
            
        try:
            # Load and validate each JSON line
            bookmarks = []
            invalid_lines = []
            empty_contents = []
            invalid_dates = []
            duplicate_urls = set()
            url_counts = {}
            
            with open(data_path, 'r', encoding='utf-8') as f:
                for i, line in enumerate(f):
                    try:
                        bookmark = json.loads(line.strip())
                        bookmarks.append(bookmark)
                        
                        # Check for empty content
                        if not bookmark.get('content'):
                            empty_contents.append(i + 1)
                            
                        # Check for invalid dates
                        if 'created_at' in bookmark:
                            try:
                                # Try to parse the date
                                datetime.fromisoformat(bookmark['created_at'].replace('Z', '+00:00'))
                            except (ValueError, TypeError):
                                invalid_dates.append(i + 1)
                                
                        # Check for duplicate URLs
                        url = bookmark.get('url')
                        if url:
                            url_counts[url] = url_counts.get(url, 0) + 1
                            if url_counts[url] > 1:
                                duplicate_urls.add(url)
                        
                    except json.JSONDecodeError:
                        invalid_lines.append(i + 1)
            
            # Count by source
            source_counts = {}
            for bookmark in bookmarks:
                source = bookmark.get('source', 'unknown')
                source_counts[source] = source_counts.get(source, 0) + 1
                
            # Summary stats
            total_bookmarks = len(bookmarks)
            invalid_count = len(invalid_lines)
            empty_content_count = len(empty_contents)
            invalid_date_count = len(invalid_dates)
            duplicate_url_count = len(duplicate_urls)
            
            # Log findings
            logger.info(f"Quality check results for {data_path}:")
            logger.info(f"Total bookmarks: {total_bookmarks}")
            logger.info(f"Invalid JSON lines: {invalid_count}")
            logger.info(f"Empty content fields: {empty_content_count}")
            logger.info(f"Invalid dates: {invalid_date_count}")
            logger.info(f"Duplicate URLs: {duplicate_url_count}")
            logger.info(f"Source distribution: {source_counts}")
            
            # Determine overall status
            status = "success"
            warnings = []
            
            if invalid_count > 0:
                status = "warning"
                warnings.append(f"{invalid_count} invalid JSON lines")
                
            if empty_content_count > total_bookmarks * 0.1:  # More than 10% empty
                status = "warning"
                warnings.append(f"{empty_content_count} empty content fields")
                
            if invalid_date_count > 0:
                status = "warning"
                warnings.append(f"{invalid_date_count} invalid dates")
                
            if duplicate_url_count > 0:
                warnings.append(f"{duplicate_url_count} duplicate URLs")
                
            # Record stats
            self.stats["steps"]["quality_check"] = {
                "status": status,
                "duration_seconds": (datetime.now() - step_start).total_seconds(),
                "total_bookmarks": total_bookmarks,
                "invalid_lines": invalid_count,
                "empty_contents": empty_content_count,
                "invalid_dates": invalid_date_count,
                "duplicate_urls": duplicate_url_count,
                "source_counts": source_counts,
                "warnings": warnings if warnings else None
            }
            
            # If critical issues, raise exception
            if status == "failed":
                raise ValueError(f"Quality check failed: {', '.join(warnings)}")
                
        except Exception as e:
            if not isinstance(e, ValueError) or "Quality check failed" not in str(e):
                logger.error(f"Error during quality checks: {str(e)}")
                self.stats["steps"]["quality_check"] = {
                    "status": "failed",
                    "duration_seconds": (datetime.now() - step_start).total_seconds(),
                    "error": str(e)
                }
                raise
            else:
                # This is our own quality check failure
                raise
                
    def finalize_dataset(self):
        """Finalize the dataset for publishing."""
        step_start = datetime.now()
        logger.info("Finalizing dataset")
        
        source_path = ENRICHED_DATA_PATH if ENRICHED_DATA_PATH.exists() else DATA_PATH
        
        if not source_path.exists():
            logger.error(f"No source data file found at {source_path}")
            self.stats["steps"]["finalize"] = {
                "status": "failed",
                "duration_seconds": (datetime.now() - step_start).total_seconds(),
                "error": f"No source data file found at {source_path}"
            }
            raise FileNotFoundError(f"No source data file found at {source_path}")
            
        try:
            # For now, just copy the file to the final location
            # In a real scenario, you might do additional processing here
            import shutil
            shutil.copy2(source_path, FINAL_DATA_PATH)
            
            # Count final bookmarks
            final_count = self.count_lines(FINAL_DATA_PATH)
            
            logger.info(f"Finalized dataset with {final_count} bookmarks")
            
            # Record stats
            self.stats["steps"]["finalize"] = {
                "status": "success",
                "duration_seconds": (datetime.now() - step_start).total_seconds(),
                "bookmark_count": final_count,
                "source_file": str(source_path),
                "final_file": str(FINAL_DATA_PATH)
            }
            
        except Exception as e:
            logger.error(f"Error finalizing dataset: {str(e)}")
            self.stats["steps"]["finalize"] = {
                "status": "failed",
                "duration_seconds": (datetime.now() - step_start).total_seconds(),
                "error": str(e)
            }
            raise
            
    def enhance_with_full_text(self):
        """Enhance the finalized dataset with full text content."""
        step_start = datetime.now()
        logger.info("Enhancing dataset with full_text field")
        
        # Define paths for enhanced file and stats
        enhanced_path = BASE_DIR / "data-bookmark-enhanced.jsonl"
        stats_path = BASE_DIR / "full_text_stats.json"
        
        # Check if the final data exists
        if not FINAL_DATA_PATH.exists():
            logger.error(f"Final data file not found at {FINAL_DATA_PATH}")
            self.stats["steps"]["full_text_enhancement"] = {
                "status": "failed",
                "duration_seconds": (datetime.now() - step_start).total_seconds(),
                "error": f"Final data file not found at {FINAL_DATA_PATH}"
            }
            raise FileNotFoundError(f"Final data file not found at {FINAL_DATA_PATH}")
            
        try:
            # Run add_full_text.py script
            cmd = [
                sys.executable, 
                str(BASE_DIR / "add_full_text.py"),
                str(FINAL_DATA_PATH),
                "--output", str(enhanced_path),
                "--report", str(stats_path)
            ]
            
            # Add optional arguments
            if self.args.enrichment_limit:
                cmd.extend(["--limit", str(self.args.enrichment_limit)])
                
            result = subprocess.run(
                cmd,
                check=True,
                capture_output=True,
                text=True
            )
            
            logger.info(f"Full text enhancement completed: {result.stdout.strip()}")
            
            # Verify the enhanced file exists
            if not enhanced_path.exists():
                raise FileNotFoundError(f"Enhancement did not create output file at {enhanced_path}")
                
            # Load stats if available
            enhancement_stats = {}
            if stats_path.exists():
                try:
                    with open(stats_path, 'r', encoding='utf-8') as f:
                        enhancement_stats = json.load(f)
                except json.JSONDecodeError:
                    logger.warning("Could not parse full_text enhancement stats")
            
            # Record stats
            self.stats["steps"]["full_text_enhancement"] = {
                "status": "success",
                "duration_seconds": (datetime.now() - step_start).total_seconds(),
                "output_file": str(enhanced_path),
                "stats_file": str(stats_path),
                "stats": enhancement_stats.get("stats", {})
            }
            
        except subprocess.CalledProcessError as e:
            logger.error(f"Full text enhancement failed with exit code {e.returncode}")
            logger.error(f"Stdout: {e.stdout}")
            logger.error(f"Stderr: {e.stderr}")
            self.stats["steps"]["full_text_enhancement"] = {
                "status": "failed",
                "duration_seconds": (datetime.now() - step_start).total_seconds(),
                "error": str(e),
                "stdout": e.stdout,
                "stderr": e.stderr
            }
            raise
        except Exception as e:
            logger.error(f"Error enhancing data with full_text: {str(e)}")
            self.stats["steps"]["full_text_enhancement"] = {
                "status": "failed",
                "duration_seconds": (datetime.now() - step_start).total_seconds(),
                "error": str(e)
            }
            raise
            
    def update_documentation(self):
        """Update README and PR documentation."""
        step_start = datetime.now()
        logger.info("Updating documentation")
        
        try:
            # Update README with last run date and stats
            self.update_readme()
            
            # Update PR README with pipeline context
            self.update_pr_readme()
            
            # Record stats
            self.stats["steps"]["documentation"] = {
                "status": "success",
                "duration_seconds": (datetime.now() - step_start).total_seconds()
            }
            
        except Exception as e:
            logger.error(f"Error updating documentation: {str(e)}")
            self.stats["steps"]["documentation"] = {
                "status": "failed",
                "duration_seconds": (datetime.now() - step_start).total_seconds(),
                "error": str(e)
            }
            raise
            
    def update_readme(self):
        """Update the main README with latest run information."""
        if not README_PATH.exists():
            logger.warning(f"README file not found at {README_PATH}, creating new one")
            readme_content = "# Deltaload ETL Pipeline\n\n"
        else:
            with open(README_PATH, 'r', encoding='utf-8') as f:
                readme_content = f.read()
                
        # Check if the README has a Last Updated section
        if "## Last Updated" in readme_content:
            # Replace the existing section
            import re
            pattern = r"## Last Updated\n\n.*?(?=\n##|\Z)"
            replacement = self.generate_last_updated_section()
            readme_content = re.sub(pattern, replacement, readme_content, flags=re.DOTALL)
        else:
            # Add the section at the end
            readme_content += "\n\n" + self.generate_last_updated_section()
            
        # Write the updated README
        with open(README_PATH, 'w', encoding='utf-8') as f:
            f.write(readme_content)
            
        logger.info(f"Updated README at {README_PATH}")
        
    def generate_last_updated_section(self):
        """Generate the Last Updated section for the README."""
        now = datetime.now()
        
        # Get dataset stats
        bookmark_count = self.count_lines(FINAL_DATA_PATH)
        source_distribution = self.get_source_distribution(FINAL_DATA_PATH)
        
        section = f"## Last Updated\n\n"
        section += f"Last pipeline run: {now.strftime('%Y-%m-%d %H:%M:%S')}\n\n"
        section += f"### Dataset Statistics\n\n"
        section += f"- Total bookmarks: {bookmark_count}\n"
        section += "- Source distribution:\n"
        
        for source, count in source_distribution.items():
            percentage = (count / bookmark_count) * 100 if bookmark_count > 0 else 0
            section += f"  - {source}: {count} ({percentage:.1f}%)\n"
            
        return section
        
    def update_pr_readme(self):
        """Update PR README with pipeline stats."""
        logger.info("Updating PR README")
        
        # Read the current PR README content
        try:
            with open(PR_README_PATH, 'r', encoding='utf-8') as f:
                pr_content = f.read()
        except FileNotFoundError:
            # Create a basic PR README if it doesn't exist
            pr_content = "# Pipeline PR\n\n"
        
        # Add the pipeline section at the end or replace existing section
        pipeline_section = self.generate_pipeline_section()
        
        if "## Pipeline Run" in pr_content:
            # Replace the existing section with a more robust regex pattern
            import re
            # This pattern will match from "## Pipeline Run" until either the next top-level heading (##)
            # or the end of the file, consuming all nested content in between
            pattern = r"## Pipeline Run\n[\s\S]*?(?=\n## |\Z)"
            pr_content = re.sub(pattern, pipeline_section, pr_content)
        else:
            # Add the section at the end
            pr_content += "\n\n" + pipeline_section
            
        # Write the updated PR README
        with open(PR_README_PATH, 'w', encoding='utf-8') as f:
            f.write(pr_content)
            
        logger.info(f"Updated PR README at {PR_README_PATH}")
        
    def generate_pipeline_section(self):
        """Generate the Pipeline Run section for the PR README."""
        now = datetime.now()
        
        section = f"## Pipeline Run\n\n"
        section += f"Run date: {now.strftime('%Y-%m-%d %H:%M:%S')}\n\n"
        
        # Include overall stats
        section += "### Pipeline Stats\n\n"
        
        # Add deltaload stats
        if "deltaload" in self.stats["steps"]:
            deltaload = self.stats["steps"]["deltaload"]
            section += f"#### Deltaload\n\n"
            section += f"- Status: {deltaload['status']}\n"
            section += f"- Duration: {deltaload['duration_seconds']:.2f} seconds\n"
            if deltaload['status'] == "failed" and 'error' in deltaload:
                section += f"- Error: {deltaload['error']}\n"
                
        # Add Twitter processing stats
        if "twitter_processing" in self.stats["steps"]:
            twitter = self.stats["steps"]["twitter_processing"]
            section += f"\n#### Twitter Processing\n\n"
            section += f"- Status: {twitter['status']}\n"
            section += f"- Duration: {twitter['duration_seconds']:.2f} seconds\n"
            
            if 'method' in twitter and twitter['method'] == 'subprocess':
                section += f"- Method: Shell script (run_tweet_fixes.sh)\n"
            else:
                if 'twitter_count' in twitter:
                    section += f"- Twitter bookmarks processed: {twitter['twitter_count']}\n"
                if 'content_fixed' in twitter:
                    section += f"- Content mismatches fixed: {twitter['content_fixed']}\n"
                if 'retweets_fixed' in twitter:
                    section += f"- Retweets reformatted: {twitter['retweets_fixed']}\n"
                if 'truncated_count' in twitter:
                    section += f"- Truncated tweets found: {twitter['truncated_count']}\n"
                if 'truncated_fixed' in twitter:
                    section += f"- Truncated tweets fixed: {twitter['truncated_fixed']}\n"
                    if 'fixed_from_cache' in twitter and 'fixed_from_api' in twitter:
                        section += f"  - From cache: {twitter['fixed_from_cache']}\n"
                        section += f"  - From API: {twitter['fixed_from_api']}\n"
            
            if twitter['status'] == "failed" and 'error' in twitter:
                section += f"- Error: {twitter['error']}\n"
                
        # Add enrichment stats
        if "enrichment" in self.stats["steps"]:
            enrichment = self.stats["steps"]["enrichment"]
            section += f"\n#### Enrichment\n\n"
            section += f"- Status: {enrichment['status']}\n"
            section += f"- Duration: {enrichment['duration_seconds']:.2f} seconds\n"
            if 'total_bookmarks' in enrichment:
                section += f"- Processed: {enrichment['total_bookmarks']} bookmarks\n"
            if enrichment['status'] == "failed" and 'error' in enrichment:
                section += f"- Error: {enrichment['error']}\n"
                
        # Add quality check stats
        if "quality_check" in self.stats["steps"]:
            qc = self.stats["steps"]["quality_check"]
            section += f"\n#### Quality Check\n\n"
            section += f"- Status: {qc['status']}\n"
            section += f"- Duration: {qc['duration_seconds']:.2f} seconds\n"
            if 'total_bookmarks' in qc:
                section += f"- Total bookmarks: {qc['total_bookmarks']}\n"
            if 'source_counts' in qc:
                section += "- Source distribution:\n"
                for source, count in qc['source_counts'].items():
                    percentage = (count / qc['total_bookmarks']) * 100 if qc.get('total_bookmarks', 0) > 0 else 0
                    section += f"  - {source}: {count} ({percentage:.1f}%)\n"
            if 'warnings' in qc and qc['warnings']:
                section += "- Warnings:\n"
                for warning in qc['warnings']:
                    section += f"  - {warning}\n"
                    
        # Add finalize stats
        if "finalize" in self.stats["steps"]:
            finalize = self.stats["steps"]["finalize"]
            section += f"\n#### Finalization\n\n"
            section += f"- Status: {finalize['status']}\n"
            section += f"- Duration: {finalize['duration_seconds']:.2f} seconds\n"
            if 'bookmark_count' in finalize:
                section += f"- Final bookmark count: {finalize['bookmark_count']}\n"
        
        # Add full text enhancement stats
        if "full_text_enhancement" in self.stats["steps"]:
            enhancement = self.stats["steps"]["full_text_enhancement"]
            section += f"\n#### Full Text Enhancement\n\n"
            section += f"- Status: {enhancement['status']}\n"
            section += f"- Duration: {enhancement['duration_seconds']:.2f} seconds\n"
            
            if 'stats' in enhancement:
                stats = enhancement['stats']
                if 'total' in stats:
                    section += f"- Total bookmarks processed: {stats['total']}\n"
                if 'with_full_text_before' in stats and 'with_full_text_after' in stats:
                    before_percent = (stats['with_full_text_before'] / stats['total']) * 100 if stats.get('total', 0) > 0 else 0
                    after_percent = (stats['with_full_text_after'] / stats['total']) * 100 if stats.get('total', 0) > 0 else 0
                    section += f"- Bookmarks with full_text before: {stats['with_full_text_before']} ({before_percent:.1f}%)\n"
                    section += f"- Bookmarks with full_text after: {stats['with_full_text_after']} ({after_percent:.1f}%)\n"
                
                if 'by_source' in stats:
                    section += "- Source distribution:\n"
                    for source, count in stats['by_source'].items():
                        percentage = (count / stats['total']) * 100 if stats.get('total', 0) > 0 else 0
                        section += f"  - {source}: {count} ({percentage:.1f}%)\n"
            
            if enhancement['status'] == "failed" and 'error' in enhancement:
                section += f"- Error: {enhancement['error']}\n"
                
        return section
        
    def save_stats(self):
        """Save pipeline stats to a JSON file."""
        self.stats["total_duration_seconds"] = (
            datetime.fromisoformat(self.stats["end_time"]) - 
            datetime.fromisoformat(self.stats["start_time"])
        ).total_seconds()
        
        # Save stats to file
        os.makedirs(STATS_PATH.parent, exist_ok=True)
        with open(STATS_PATH, 'w', encoding='utf-8') as f:
            json.dump(self.stats, f, indent=2)
            
        logger.info(f"Saved pipeline stats to {STATS_PATH}")
        
    def count_lines(self, file_path):
        """Count lines in a file."""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                return sum(1 for _ in f)
        except Exception as e:
            logger.error(f"Error counting lines in {file_path}: {str(e)}")
            return 0
            
    def get_source_distribution(self, file_path):
        """Get distribution of bookmark sources."""
        sources = {}
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                for line in f:
                    try:
                        bookmark = json.loads(line.strip())
                        source = bookmark.get('source', 'unknown')
                        sources[source] = sources.get(source, 0) + 1
                    except json.JSONDecodeError:
                        continue
        except Exception as e:
            logger.error(f"Error getting source distribution for {file_path}: {str(e)}")
        return sources


def main():
    """Main entry point for the ETL pipeline."""
    parser = argparse.ArgumentParser(description="Run the complete ETL pipeline")
    
    # Add arguments for controlling pipeline behavior
    parser.add_argument("--skip-deltaload", action="store_true", 
                       help="Skip running the deltaload step")
    parser.add_argument("--skip-twitter-processing", action="store_true",
                       help="Skip Twitter content processing")
    parser.add_argument("--skip-truncated-tweets", action="store_true",
                       help="Skip fixing truncated tweets (still processes other Twitter content)")
    parser.add_argument("--skip-enrichment", action="store_true",
                       help="Skip enriching bookmark data")
    parser.add_argument("--skip-quality-check", action="store_true",
                       help="Skip quality check step")
    parser.add_argument("--skip-docs", action="store_true",
                       help="Skip updating documentation")
    parser.add_argument("--force-refresh", action="store_true",
                       help="Force refresh cached content during enrichment")
    parser.add_argument("--enrichment-limit", type=int,
                       help="Limit number of bookmarks to enrich")
    parser.add_argument("--skip-full-text-enhancement", action="store_true",
                       help="Skip full text enhancement step")
    
    args = parser.parse_args()
    
    # Run the pipeline
    pipeline = ETLPipeline(args)
    success = pipeline.run()
    
    # Exit with appropriate code
    sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()