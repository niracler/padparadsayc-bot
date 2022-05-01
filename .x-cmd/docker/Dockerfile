FROM python:3.8

WORKDIR /app

COPY requirements.txt /app/
RUN pip install -r requirements.txt

COPY .x-cmd/docker/entrypoint.sh /app/
COPY bot /app/bot

ENTRYPOINT [ "sh", "./entrypoint.sh" ]