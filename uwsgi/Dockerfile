FROM python:3.12-alpine

RUN apk update
RUN apk add bash

COPY ./requirements.txt /app/requirements.txt
WORKDIR /app

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY . .

RUN chmod +x ./entrypoint_uwsgi.sh
RUN chmod +x ./wait-for-it.sh
