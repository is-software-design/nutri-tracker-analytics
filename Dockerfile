FROM python:3.8-slim

WORKDIR  /usr/src

RUN apt-get update && \
 apt-get install -y gcc make libpq-dev apt-transport-https ca-certificates build-essential

COPY requirements.txt .
RUN pip install psycopg2-binary==2.9.3
RUN pip install -r requirements.txt

COPY src .

CMD ["python", "app.py"]
