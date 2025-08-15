#!/usr/bin/env python3
"""
Raindrop.io Backup Script
This script downloads all your Raindrop.io bookmarks using the API,
starting from the most recent and proceeding at the fastest possible rate.
"""

import os
import json
import time
import asyncio
import aiohttp
import pandas as pd
from datetime import datetime
from tqdm.asyncio import tqdm

# Your Raindrop.io API credentials
CLIENT_ID = "6507036842b6ddb458e88bf9"
CLIENT_SECRET = "160141a8-fc07-4674-9ef8-f41c309721f8"
TEST_TOKEN = "4f70fcd2-add2-44e2-b501-e23ca1550f60"

class RaindropBackup:
    def __init__(self, token, output_dir="raindrop_backup"):
        self.token = token
        self.output_dir = output_dir
        self.base_url = "https://api.raindrop.io/rest/v1"
        self.headers = {
            "Authorization": f"Bearer {self.token}",
            "Content-Type": "application/json"
        }
        
        # Create output directory if it doesn't exist
        os.makedirs(self.output_dir, exist_ok=True)
        
    async def fetch_data(self, session, url, params=None):
        """Fetch data from Raindrop API with rate limiting considerations"""
        try:
            async with session.get(url, headers=self.headers, params=params) as response:
                if response.status == 429:  # Too Many Requests
                    retry_after = int(response.headers.get('Retry-After', 1))
                    print(f"Rate limited. Waiting for {retry_after} seconds")
                    await asyncio.sleep(retry_after)
                    return await self.fetch_data(session, url, params)
                
                response.raise_for_status()
                return await response.json()
        except Exception as e:
            print(f"Error fetching {url}: {e}")
            return None
    
    async def get_collections(self, session):
        """Get all collections"""
        url = f"{self.base_url}/collections"
        return await self.fetch_data(session, url)
    
    async def get_raindrops(self, session, collection_id, page=0, per_page=50):
        """Get raindrops for a specific collection with pagination"""
        url = f"{self.base_url}/raindrops/{collection_id}"
        params = {
            "sort": "-created",  # Sort by created date, newest first
            "page": page,
            "perpage": per_page
        }
        return await self.fetch_data(session, url, params)
    
    async def get_all_raindrops(self, session, collection_id):
        """Get all raindrops for a collection (handles pagination)"""
        all_raindrops = []
        page = 0
        per_page = 50  # Maximum allowed by API
        
        while True:
            data = await self.get_raindrops(session, collection_id, page, per_page)
            if not data or not data.get('items'):
                break
            
            raindrops = data.get('items', [])
            all_raindrops.extend(raindrops)
            
            # Check if we've reached the end
            if len(raindrops) < per_page:
                break
            
            page += 1
            # Small pause to be nice to the API
            await asyncio.sleep(0.1)
        
        return all_raindrops
    
    async def backup_all_collections(self):
        """Backup all collections and their raindrops"""
        async with aiohttp.ClientSession() as session:
            # Get collections
            collections_data = await self.get_collections(session)
            if not collections_data:
                print("Failed to fetch collections")
                return
            
            collections = collections_data.get('items', [])
            print(f"Found {len(collections)} collections")
            
            # Process each collection
            all_raindrops = []
            for collection in tqdm(collections, desc="Collections"):
                collection_id = collection.get('_id')
                collection_title = collection.get('title', 'Unknown')
                
                raindrops = await self.get_all_raindrops(session, collection_id)
                print(f"Collection '{collection_title}' has {len(raindrops)} raindrops")
                
                # Add collection info to each raindrop
                for raindrop in raindrops:
                    raindrop['collection_title'] = collection_title
                
                all_raindrops.extend(raindrops)
            
            # Save all data
            self.save_data(collections, all_raindrops)
    
    def save_data(self, collections, raindrops):
        """Save collections and raindrops to files"""
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        
        # Save collections
        collections_file = os.path.join(self.output_dir, f"collections_{timestamp}.json")
        with open(collections_file, 'w', encoding='utf-8') as f:
            json.dump(collections, f, ensure_ascii=False, indent=2)
        
        # Save raindrops
        raindrops_file = os.path.join(self.output_dir, f"raindrops_{timestamp}.json")
        with open(raindrops_file, 'w', encoding='utf-8') as f:
            json.dump(raindrops, f, ensure_ascii=False, indent=2)
        
        # Save as CSV for easier viewing
        try:
            # Extract key fields for the CSV
            csv_data = []
            for drop in raindrops:
                csv_data.append({
                    'id': drop.get('_id'),
                    'title': drop.get('title'),
                    'url': drop.get('link'),
                    'created': drop.get('created'),
                    'tags': ', '.join(drop.get('tags', [])),
                    'collection': drop.get('collection_title'),
                    'note': drop.get('note', '')
                })
            
            df = pd.DataFrame(csv_data)
            csv_file = os.path.join(self.output_dir, f"raindrops_{timestamp}.csv")
            df.to_csv(csv_file, index=False, encoding='utf-8')
            
            print(f"Successfully backed up {len(raindrops)} raindrops")
            print(f"Files saved to:")
            print(f"- Collections: {collections_file}")
            print(f"- Raindrops JSON: {raindrops_file}")
            print(f"- Raindrops CSV: {csv_file}")
        except Exception as e:
            print(f"Error creating CSV: {e}")
            print(f"Raw data is still saved to: {raindrops_file}")

async def main():
    backup = RaindropBackup(TEST_TOKEN)
    await backup.backup_all_collections()

if __name__ == "__main__":
    # Ensure output directory exists
    output_dir = os.path.join(os.path.expanduser("~"), "Desktop", "raindrop_backup")
    os.makedirs(output_dir, exist_ok=True)
    
    # Create backup instance with the output directory
    backup = RaindropBackup(TEST_TOKEN, output_dir=output_dir)
    
    # Run the backup process
    asyncio.run(backup.backup_all_collections())