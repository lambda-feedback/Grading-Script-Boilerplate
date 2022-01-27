# Base image is Python 3.8 provided by AWS Lambda in Docker Hub
FROM public.ecr.aws/lambda/python:3.8

WORKDIR /app

# Install backend dependencies
COPY backend/requirements.txt ./backend/
RUN pip3 install -r backend/requirements.txt

# Copy the scripts
COPY __init__.py ./app/
COPY backend/__init__.py ./app/backend/
COPY backend/tests/*.py ./app/backend/tests/
COPY backend/tools/*.py ./app/backend/tools/

ENV REQUEST_SCHEMA_URL https://raw.githubusercontent.com/lambda-feedback/request-response-schemas/master/request.json
ENV RESPONSE_SCHEMA_URL https://raw.githubusercontent.com/lambda-feedback/request-response-schemas/master/response.json