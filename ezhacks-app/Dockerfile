# debian based docker image
FROM python:3.9

RUN apt-get update
RUN apt-get -y install python3-dev
RUN apt-get -y install dos2unix

COPY requirements.txt requirements.txt
RUN python -m venv venv
RUN venv/bin/pip install -r requirements.txt
RUN venv/bin/pip install gunicorn

COPY app app
COPY app.db ./
COPY config.py ./
COPY ezhacks-app.py ./
COPY boot.sh ./

RUN chmod +x boot.sh

ENV FLASK_APP app.py

EXPOSE 80
ENTRYPOINT ["./boot.sh"]