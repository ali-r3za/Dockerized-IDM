# use python slim version(smaller size)
FROM python::3.11-slim
# set working directory
WORKDIR /app
COPY requirements.txt
# install packages (internal miror recommended)
RUN pip install -i https://mirror-pypi.runflare.com/simple -r requirements.txt
COPY main.py
ENTRYPOINT ["python", "downloader.py"]
