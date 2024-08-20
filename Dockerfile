FROM python:3.11-alpine
COPY . ./app
WORKDIR /app
RUN apk update && apk upgrade
RUN pip install pipenv
RUN pipenv sync --dev