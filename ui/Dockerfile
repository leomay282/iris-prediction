FROM  python:3.10

RUN apt-get update

WORKDIR /ui

COPY templates/ templates
COPY ui.py ui.py
COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt