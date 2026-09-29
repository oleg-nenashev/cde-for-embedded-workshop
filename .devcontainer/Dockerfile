FROM mcr.microsoft.com/devcontainers/python:3-3.14-trixie

RUN apt-get update
RUN apt-get install -y libsass-dev build-essential libcairo2 git pngquant

RUN pip install --upgrade pip
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
