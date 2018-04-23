FROM python:2.7-alpine

LABEL maintainer "tiago@reichert.eti.br"

ENV PYTHONUNBUFFERED 1
COPY . /app
ENTRYPOINT ["python","/app/main.py"]