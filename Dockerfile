# Dockerfiles are a list of instructions that Docker will follow to create your container for you
FROM python:3

COPY . /usr/src/app

WORKDIR /usr/src/app
RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "./bot.py"]