# this is a cli donwload manager. it is dockerized for easy deployment and usage.
# import os, requests, sys for sys operations (idm) and tqdm for cli command and displaying progress
import requests
import os 
import sys 
from tqdm import tqdm

chunk_size = 1024
def download(url, filename):
    """this func download a file from a given URL to a specified filename."""
    downloaded_bytes = 0
    headers = {}
    
    # check if output file already exist to support download resumption.
    if os.path.exists(filename):
       downloaded_bytes = os.path.getsize(filename)
       headers["Range"] = f"bytes={downloaded_bytes}-"
       print(f"Resuming download from byte {downloaded_bytes}")
    
    # http get request
    response = requests.get(url, headers=headers, stream=True, timeout=(5, 30))
    total_size = response.headers.get("content-length")

    if total_size is not None:
        total_size = int(total_size) + downloaded_bytes

    mode = 'ab' if downloaded_bytes > 0 else 'wb'

    # open file and create progress bar 
    try:
        with open(filename, mode) as file, tqdm(total=total_size, initial=downloaded_bytes, unit='B', unit_scale=True, unit_divisor=1024, desc=filename) as bar:
            for chunk in response.iter_content(chunk_size=chunk_size):
                if chunk:
                    file.write(chunk)
                    bar.update(len(chunk))
    # e.g (ctrl+c)
    except KeyboardInterrupt:
        print("\n Download paused!. you can resume later.")
        return
    print("Download completed successfully!")
    
if __name__ == "__main__":
    if len(sys.argv) != 3: 
        print("Usage : python downloader.py <URL> <output_file>")
        sys.exit(1)
    
    url = sys.argv[1]
    filename = sys.argv[2]

    download(url, filename)
