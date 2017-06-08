FROM tiangolo/uwsgi-nginx-flask:flask
ENV PYTHONUNBUFFERED 1
COPY . /app
RUN chmod +x entrypoint.sh
ENTRYPOINT ["./entrypoint.sh"]