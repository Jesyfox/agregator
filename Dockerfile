FROM ubuntu:bionic

RUN apt-get update

RUN apt-get install -y \
    ca-certificates \
    python3-all-dev \
    python3-pip \
    postgresql-server-dev-all \
    build-essential

ADD . /app

WORKDIR /app

RUN pip3 install --upgrade pip setuptools wheel

RUN pip3 install --trusted-host pypi.python.org -r requirements.txt

RUN useradd \
    -g users \
    myuser

RUN chown myuser logs

USER myuser

ENV PYTHONUNBUFFERED 1