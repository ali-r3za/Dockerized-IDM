# Python CLI Download Manager

This is a simple Dockerize command-line program (CLI) Download manager built with Python that helps you download files from the internet.

## Features

- **Resumable Downloads**: If a download is interrupted, the program can resume from where it left off.
- **Progress Tracking**: A progress bar shows how much of the download is left.
- **Docker Support**: If you have Docker installed, you can run this program in an isolated and easy-to-use environment.

## requirements

- **Python**: Version 3.11 or higher.
- **pip**: The Python package installer (usually comes with Python).
- **Docker**: (Optional) If you want to use the Docker feature.

## Installation

### 1. Clone the Repo

First, clone the repository from GitHub:
```bash
git clone https://github.com/ali-r3za/Dockerized-IDM.git
cd Dockerized-IDM
```

### 2. Install required libraries 

pip install -r requirements.txt 

(or you can use the internal miror):

pip install -i https://mirror-pypi.runflare.com/simple -r requirements.txt

### 3.How to use 
1. Build the Docker image: 

docker build -t download-manager .

2. Run the Program with Docker:

docker run --rm -v "$(pwd):/app" download-manager python main.py <file_URL> <saved_file_name>

Example: 
docker run --rm -v "$(pwd):/app" download-manager python main.py https://pub.linuxmint.io/stable/22.3/linuxmint-22.3-cinnamon-64bit.iso linux-mint.iso

### Project Structure:
Dockerized-IDM/
├── main.py               # The main script containing the download logic
├── Dockerfile            # Dockerfile for building the Docker image
├── requirements.txt      # List of required Python libraries
└──README.md             # This file, providing documentation
