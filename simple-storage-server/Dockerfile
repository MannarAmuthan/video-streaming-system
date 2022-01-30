FROM python:3.7-slim

RUN apt-get -y update
RUN apt-get -y upgrade

WORKDIR /working_directory
COPY . .

RUN pip3 install pipenv
RUN pipenv install
RUN pipenv run pip3 freeze > requirements.txt
RUN pip3 install -r requirements.txt

ENV PYTHONUNBUFFERED True

ENV PORT 8080
ENV PYTHONPATH src/
EXPOSE 8080

CMD exec gunicorn server:flask_app  --timeout=0