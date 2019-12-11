FROM python:3.7-alpine
COPY . /app
WORKDIR /app
RUN date
RUN apk add tzdata
RUN apk add build-base
RUN cp /usr/share/zoneinfo/America/New_York /etc/localtime
RUN echo "America/New_York" > /etc/timezone
RUN date
RUN pip install -r requirements.txt
CMD [ "python", "-u", "src/server.py" ]