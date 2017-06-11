FROM python:2.7-alpine
ENV PYTHONUNBUFFERED 1
COPY . /app
ENTRYPOINT ["python","/app/main.py"]