FROM  python:3.12-rc-slim-buster

WORKDIR /usr/src/app


ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

RUN apt-get update && apt-get install -y \
       build-essential  \
       libpq-dev \
       && rm -rf /var/lib/apt/lists/*
RUN pip install --upgrade pip

       # Установка пакетов для проекта
COPY requirements.txt ./requirements.txt
RUN pip install -r requirements.txt

       
COPY .  .