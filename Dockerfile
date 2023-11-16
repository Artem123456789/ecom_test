FROM python:3.8-slim-buster

ENV LANG C.UTF-8
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

COPY requirements.txt /tmp
RUN pip3 install --upgrade pip && pip3 install -r /tmp/requirements.txt && rm /tmp/requirements.txt

WORKDIR /code
COPY . /code

EXPOSE 8000