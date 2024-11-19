FROM python:3.8-slim

WORKDIR  /usr/src

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

ENV DB_PORT=$DB_PORT
ENV DB_HOST=$DB_HOST
ENV DB_NAME=$DB_NAME
ENV DB_USER=$DB_USER
ENV DB_PASSWORD=$DB_PASSWORD

COPY src .

CMD ["python", "app.py"]
