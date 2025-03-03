FROM python:3.8-slim AS builder

ARG USER_ID=1000
ARG GROUP_ID=1000
ARG USER_NAME=myuser

RUN groupadd --gid $GROUP_ID $USER_NAME && \
    useradd --uid $USER_ID --gid $GROUP_ID -m $USER_NAME

USER $USER_NAME

WORKDIR /usr/src

COPY requirements.txt .
RUN pip install -r requirements.txt
RUN pip install psycopg2-binary==2.9.3

COPY src .

FROM python:3.8-slim

ARG USER_ID=1000
ARG GROUP_ID=1000
ARG USER_NAME=myuser

RUN groupadd --gid $GROUP_ID $USER_NAME && \
    useradd --uid $USER_ID --gid $GROUP_ID -m $USER_NAME

USER $USER_NAME

WORKDIR /usr/src

COPY --from=builder /usr/src /usr/src
RUN pip install -r requirements.txt
RUN pip install psycopg2-binary==2.9.3

ENV PORT=5000
ENV DB_PORT=5432
ENV DB_HOST=localhost
ENV DB_NAME=nutritracker
ENV DB_USER=postgres
ENV DB_PASSWORD=postgres

CMD ["python", "app.py"]
