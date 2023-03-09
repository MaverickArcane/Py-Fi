FROM alpine:3.14

# Install python/pip
ENV PYTHONUNBUFFERED=1
RUN apk add --update --no-cache python3 && ln -sf python3 /usr/bin/python

COPY ./server.py ./server.py
RUN mkdir ./htdocs
COPY htdocs/index.html ./htdocs/index.html
RUN mkdir ./logs

CMD [ "python", "/server.py" ]
