# Download the first 10 files out of 54 files from gs://ntu_mh6812-groupproj/hacker_news_full_*.parquet
# Example filename: gs://ntu_mh6812-groupproj/hacker_news_full_000000000000.parquet
# Example destination: ./data/hacker_news_full_000000000000.parquet

import os
from google.cloud import storage

def download_blob(
    bucket_name: str = "ntu_mh6812_nlp_groupproj", 
    source_blob_name: str = "hacker_news_full_*.parquet", 
    n_files: int=10
) -> None:
    """Downloads a blob from the bucket."""
    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)
    
    for i in range(n_files):
        print(f"Downloading file {i} out of {n_files} files.", end="\r")
        blob = bucket.blob(source_blob_name.replace("*", str(i).zfill(12)))
        destination_file_name = os.path.join("./data", blob.name)
        blob.download_to_filename(destination_file_name)
        print(f"Blob {blob.name} downloaded to {destination_file_name}.")

if __name__ == "__main__":
    # Set environment variable GOOGLE_APPLICATION_CREDENTIALS to the path of the service account key file
    # TODO: Replace the path with your own path!
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "/home/vinhloc30796/work_ntu/mh6812_nlp_ai/personal-sandbox-320321-a91a885e7dc2.json"
    
    # User input: how many files to download
    n_files = int(input("How many files to download? "))
    download_blob(n_files=n_files)