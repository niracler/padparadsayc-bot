FROM python:3.8

WORKDIR /app

COPY requirements.txt /app/
RUN pip install -r requirements.txt

COPY entrypoint.sh /app/
COPY bot.py /app/

ENTRYPOINT [ "sh", "./entrypoint.sh" ]