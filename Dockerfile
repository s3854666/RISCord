# Dockerfiles are a list of instructions that Docker will follow to create your container for you
FROM debian:stable-slim

COPY . /src

WORKDIR /src
RUN apt-get update
RUN apt-get install python3 python3-pip -y
RUN pip3 install -r requirements.txt

RUN ["chmod", "+x", "/src/bot.py"]
ENTRYPOINT ["/src/bot.py"]