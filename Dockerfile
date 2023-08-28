FROM python:3.6-slim

RUN \
    apt-get update -y && \
    apt-get install -y \
        curl \
        git

RUN \
    pip install --upgrade pip

COPY requirements.txt requirements.txt

RUN \
    pip install -r requirements.txt

WORKDIR /app
