#This is a sample Image 
#https://github.com/joyzoursky/docker-python-chromedriver/blob/master/py-alpine/3.10-alpine-selenium/Dockerfile

FROM python:3.10-alpine

WORKDIR /app

# update apk repo
RUN echo "http://dl-4.alpinelinux.org/alpine/v3.14/main" >> /etc/apk/repositories && \
    echo "http://dl-4.alpinelinux.org/alpine/v3.14/community" >> /etc/apk/repositories

# install chromedriver
RUN apk update
RUN apk add chromium chromium-chromedriver nano

# upgrade pip
RUN pip install --upgrade pip

# copy application source
#CP ./src/requirements.txt requirements.txt
COPY ./src/. .

# install selenium
#RUN pip install selenium
RUN pip3 install -r requirements.txt

CMD [ "bash" ]
