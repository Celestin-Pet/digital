# syntax=docker/dockerfile:1
FROM python:3.10.7-alpine

# Disable python buffering and bytecode *.pyc compiling. 
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Project directory.
WORKDIR /srv/www/kirillzhosul/api

# Install requirements.
COPY api/requirements.txt /srv/www/kirillzhosul/api/
RUN apk add build-base
RUN pip install --upgrade pip
RUN pip install --upgrade --no-cache-dir -r requirements.txt

# Copy whole project.
COPY . /srv/www/kirillzhosul/api/

# Run project.
CMD ["gunicorn", "app.app:app", "-c", "gunicorn.conf.py"]
