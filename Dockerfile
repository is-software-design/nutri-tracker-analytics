FROM python:3.8-slim

WORKDIR /source

RUN apt-get update && \
 apt-get install -y gcc make libpq-dev apt-transport-https ca-certificates build-essential

COPY requirements.txt .
RUN pip install psycopg2-binary==2.9.3
RUN pip install -r requirements.txt

ENV PORT=5000
ARG DB_PORT
ARG DB_HOST
ARG DB_NAME
ARG DB_USER
ARG DB_PASSWORD

COPY ./src ./src
WORKDIR /source/src

CMD ["python", "app.py"]
