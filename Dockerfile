FROM python:3.10

#ENV Vars
WORKDIR /app
ENV PEC_USER=user
ENV PEC_PASS=pass!

# install google chrome
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add -
RUN sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list'
RUN apt-get -y update
RUN apt-get install -y google-chrome-stable

# install chromedriver
RUN apt-get install -yqq unzip nano bash cron
RUN wget -O /tmp/chromedriver.zip http://chromedriver.storage.googleapis.com/`curl -sS chromedriver.storage.googleapis.com/LATEST_RELEASE`/chromedriver_linux64.zip
RUN unzip /tmp/chromedriver.zip chromedriver -d /usr/local/bin/

# set display port to avoid crash
ENV DISPLAY=:99

# copy application source
#CP ./src/requirements.txt requirements.txt
COPY ./src/. .
COPY crontab crontab

# upgrade pip
RUN pip install --upgrade pip

# install selenium
RUN pip install selenium

## shedule the script to run
#RUN crontab crontab

#CMD ["crond", "-f"]

