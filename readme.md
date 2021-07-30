# Grading Script Boilerplate

This template repository contains the boilerplate code needed in order to create an AWS Lambda function that can be written by any tutor to grade a response area in any way they like.

This version is specifically for python, however the ultimate goal is to make similar boilerplate repositories in any language, allowing tutors the freedom to code in what they feel most comfortable with.

## Repository Structure

```bash
.gitignore
.github/
    workflows/
        build-base-image.yml # for redeploying the base image to Docker Hub
        test-and-deploy.yml # for testing and deploying grading scripts to AWS
app/
    __init__.py
    algorithm.py # script to grade answers
    schema.json # schema to check the data is well structured
    requirements.txt # list of packages needed for algorithm.py

    tools/ # folder of middleware functions (for testing only)
        __init__.py
        app.py # main parsing, handling functions
        validate.py # script for validating request body using schema.json
        healthcheck.py # script for running tests in a JSON-encodable format

        Dockerfile # for building the base image
        base_requirements.txt # packages needed by tools/

    tests/ # folder of scripts to check the algorithm and schema work
        __init__.py
        handling.py # for checking functions in tools/ work
        validation.py # for checking schema.json works
        grading.py # for checking algorithm.py works
    
    Dockerfile # for building whole image to deploy to AWS
```

## How it works

### Docker & Amazon Web Services (AWS)

The grading scripts are hosted AWS Lambda, using containers to run a docker image of the app. Docker is a popular tool in software development that allows programs to be hosted on any machine by bundling all its requirements and dependencies into a single file called an __image__.

Images are run within __containers__ on AWS, which give us a lot of flexibility over what programming language and packages/libraries can be used.

For more information on Docker, read [this introduction to containerisation](https://www.freecodecamp.org/news/a-beginner-friendly-introduction-to-containers-vms-and-docker-79a9e3e119b/). To learn more about AWS Lambda, click [here](https://geekflare.com/aws-lambda-for-beginners/).

### Middleware Functions

### GitHub Actions

## Pre-requisities

## Installation

## Usage

### Getting Started

### Best Practises

### Coding

#### `algorithm.py`

#### `schema.json`

### Testing

#### `tests/grading.py`

#### `tests/validation.py`

### Deployment
