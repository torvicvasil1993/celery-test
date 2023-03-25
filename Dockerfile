FROM python:3.8-slim-buster

RUN apt-get update && \
    apt-get install -y --no-install-recommends gcc && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /app

RUN chgrp -R 0 /app && \
    chmod -R u+rw /app && \
    chmod -R g=u /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["celery", "-A", "myapp", "worker", "-B", "--loglevel=info"]
