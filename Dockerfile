FROM ubuntu:bionic

RUN apt-get update

RUN apt-get install -y \
    ca-certificates \
    python3-all-dev \
    python3-pip \
    postgresql-server-dev-all \
    build-essential

WORKDIR /app

COPY . /app

RUN echo "" > /app/supervisord-agregator.log

RUN echo "" > /app/supervisord-celery.log

RUN pip3 install --upgrade pip setuptools wheel

RUN pip3 install --trusted-host pypi.python.org -r requirements.txt


RUN useradd \
    -g users \
    myuser

USER myuser

ENV PYTHONUNBUFFERED 1