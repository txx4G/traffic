FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /app
VOLUME /app /static /media

COPY server ./

RUN apt-get update \
&& apt-get -y install binutils libproj-dev gdal-bin git-all wget build-essential libgeos-dev libexpat1 pkg-config libsqlite3-mod-spatialite \
&& python3 -m pip install --no-cache-dir --no-warn-script-location --user -r requirements.txt
