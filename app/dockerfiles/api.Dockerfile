FROM python:3.12.2

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /project
RUN mkdir app
COPY ./app/requirements.txt ./requirements.txt

RUN apt upgrade |\
    apt update |\
    pip install --no-cache-dir -r requirements.txt

ADD ./app ./app