# Base image is Python 3.8 provided by AWS Lambda in Docker Hub
FROM public.ecr.aws/lambda/python:3.8

WORKDIR /app

# Copy and install jsonschema package
COPY base_requirements.txt .
RUN pip3 install -r base_requirements.txt

# Copy the scripts
COPY __init__.py app.py validate.py ./app/
COPY tests/* ./app/tests/