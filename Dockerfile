# Base image is Python 3.8 provided by AWS Lambda in Docker Hub
FROM public.ecr.aws/lambda/python:3.8

WORKDIR /app

# Copy and install jsonschema package
COPY requirements.txt .
RUN pip3 install -r requirements.txt

COPY schema.json /tmp

# Copy the script
COPY grade.py .

# Run the handler function
CMD ["app/grade.handler"]