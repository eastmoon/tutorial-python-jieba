FROM python:slim

RUN \
    apt-get update -y && \
    apt-get install -y \
        curl \
        git

RUN \
    pip install --upgrade pip

RUN \
    pip install ckipnlp ckipnlp[tagger]

RUN \
    pip install ckiptagger[tf,gdown]

RUN \
    pip install ckip-classic

COPY requirements.txt requirements.txt

RUN \
    pip install -r requirements.txt

WORKDIR /app
