FROM python:3.8-slim

WORKDIR  /usr/src

RUN apt-get update && \
 apt-get install -y gcc make libpq-dev apt-transport-https ca-certificates build-essential

COPY requirements.txt .
RUN pip install psycopg2-binary==2.9.3
RUN pip install -r requirements.txt

ENV PORT=5000
ENV DB_PORT=5432
ENV DB_HOST=postgres
ENV DB_NAME=nutri_tracker_db
ENV DB_USER=postgres_user
ENV DB_PASSWORD=postgres_password

COPY src .

CMD ["python", "app.py"]
