FROM python:3.7-alpine

ENV PYTHONUNBUFFERED 1

ARG PROJECT=muckrock
ARG PROJECT_DIR=/usr/src/app

RUN mkdir -p $PROJECT_DIR
WORKDIR $PROJECT_DIR

COPY requirements.txt .
RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev zlib-dev jpeg-dev \
                       zlib-dev \
                       freetype-dev \
                       lcms2-dev \
                       openjpeg-dev \
                       tiff-dev \
                       tk-dev \
                       tcl-dev \
                       harfbuzz-dev \
                       fribidi-dev
RUN pip3 install --upgrade pip setuptools
RUN pip3 install -r requirements.txt

COPY . .

# Server
EXPOSE 8000
ENTRYPOINT python3 manage.py migrate && python3 manage.py runserver 0.0.0.0:8000
