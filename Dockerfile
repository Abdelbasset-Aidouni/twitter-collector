FROM python:3.8

RUN apt-get update \
    && apt-get upgrade -y \
    && apt-get install -y \
    build-essential \
    libssl-dev \
    libffi-dev \
    python3-dev \
    build-essential \
    libjpeg-dev \
    zlib1g-dev \
    gcc \
    libc-dev \
    bash \
    git \
    && pip3 install --upgrade pip

RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add -
RUN sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list'
RUN apt-get -y update
RUN apt-get install -y google-chrome-stable

ENV DISPLAY=:99

ENV LIBRARY_PATH=/lib:/usr/lib

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

RUN mkdir /code
COPY . /code/
WORKDIR /code

COPY requirements.txt /code/

RUN pip3 --no-cache-dir install -r requirements.txt
