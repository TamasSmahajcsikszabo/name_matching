# syntax=docker/dockerfile:1

FROM python:3.12.6
ENV VIRTUAL_ENV=/venv
RUN python3 -m venv $VIRTUAL_ENV
ADD data data
ADD src src
ADD requirements.txt requirements.txt
RUN /venv/bin/pip install -r requirements.txt
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

