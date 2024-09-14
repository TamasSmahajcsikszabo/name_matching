# syntax=docker/dockerfile:1

FROM python:3.12.6
RUN python3 -m venv /venv
ADD data data
ADD src src
ADD requirements.txt requirements.txt
RUN /venv/bin/pip install -r requirements.txt
