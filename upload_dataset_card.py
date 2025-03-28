"""
Script to upload the dataset card to Hugging Face
"""

import os
from huggingface_hub import HfApi, upload_file

# Initialize the Hugging Face API
api = HfApi()

# Path to your dataset card
dataset_card_path = "/Users/imac/Desktop/ETL/deltaload/dataset_card.md"

# Your Hugging Face username and dataset name
repo_id = "J94/bookmarks-dataset"

# Upload the dataset card as README.md
print(f"Uploading dataset card to {repo_id}...")
api.upload_file(
    path_or_fileobj=dataset_card_path,
    path_in_repo="README.md",
    repo_id=repo_id,
    repo_type="dataset",
)

print(f"Dataset card uploaded successfully!")
print(f"View your updated dataset at: https://huggingface.co/datasets/{repo_id}")
print("The dataset card will now provide proper documentation for your dataset in the Hugging Face Hub")