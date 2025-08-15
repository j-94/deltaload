"""
Script to upload dataset to Hugging Face
"""

import os
from huggingface_hub import HfApi, create_repo

# Initialize the Hugging Face API
api = HfApi()

# Path to your dataset
dataset_path = "/Users/imac/Desktop/ETL/deltaload/hf_bookmarks_dataset_fixed"

# Your Hugging Face username and dataset name
repo_id = "J94/bookmarks-dataset"

# Create the dataset repository
try:
    create_repo(repo_id=repo_id, repo_type="dataset", exist_ok=True)
    print(f"Repository {repo_id} created or already exists")
except Exception as e:
    print(f"Error creating repository: {e}")
    exit(1)

# Upload the dataset files
print(f"Uploading dataset from {dataset_path} to {repo_id}...")
api.upload_folder(
    folder_path=dataset_path,
    repo_id=repo_id,
    repo_type="dataset",
)

print(f"Dataset uploaded successfully!")
print(f"View your dataset at: https://huggingface.co/datasets/{repo_id}")
print("You can explore it in Data Studio by clicking on 'Explore in Data Studio'")