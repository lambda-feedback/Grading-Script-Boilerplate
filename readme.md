# Grading Script Template Repository

This template repository contains the boilerplate code needed in order to create an AWS Lambda function that can be written by any tutor to grade a response area in any way they like.

This version is specifically for python, however the ultimate goal is to make similar boilerplate repositories in any language, allowing tutors the freedom to code in what they feel most comfortable with.

## Repository Structure

```bash
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
        tools_requirements.txt # packages needed by tools/

    tests/ # folder of scripts to check the algorithm and schema work
        __init__.py
        handling.py # for checking functions in tools/ work
        validation.py # for checking schema.json works
        grading.py # for checking algorithm.py works
    
    Dockerfile # for building whole image to deploy to AWS

.github/
    workflows/
        build-base-image.yml # for redeploying the base image to Docker Hub
        test-and-deploy.yml # for testing and deploying grading scripts to AWS

.gitignore
```

## How it works

### Docker & Amazon Web Services (AWS)

The grading scripts are hosted AWS Lambda, using containers to run a docker image of the app. Docker is a popular tool in software development that allows programs to be hosted on any machine by bundling all its requirements and dependencies into a single file called an __image__.

Images are run within __containers__ on AWS, which give us a lot of flexibility over what programming language and packages/libraries can be used. For more information on Docker, read this [introduction to containerisation](https://www.freecodecamp.org/news/a-beginner-friendly-introduction-to-containers-vms-and-docker-79a9e3e119b/). To learn more about AWS Lambda, click [here](https://geekflare.com/aws-lambda-for-beginners/).

### Middleware Functions

In order to run the algorithm and schema on AWS Lambda, some middleware functions have been provided to handle, validate and return the data so all you need to worry about is the grading script and schema.

The code needed to build the image using all the middleware functions are available in the repo under `tools/` as this allows you to test your code locally. Note, it is not possible to alter the middleware functions for your own grading script, as the final image deployed to AWS pulls the middleware functions from a base image stored on the Docker Hub.

### GitHub Actions

Whenever a commit is made to the GitHub repository, the new code will go through a pipeline, where it will be tested for syntax errors and code coverage. The pipeline used is called __GitHub Actions__ and the scripts for these can be found in `.github/workflows/`.

On top of that, when starting a new grading script, you will have to complete a set of unit test scripts, which not only make sure your code is reliable, but also helps you to build a _specification_ for how the code should function before you start programming.

Once the code passes all these tests, it will then be uploaded to AWS and will be deployed and ready to go in only a few minutes.

## Pre-requisities

Although all programming can be done through the GitHub interface, it is recommended you do this locally on your machine. To do this, you must have installed:

- Python 3.8 or higher.

- GitHub Desktop or the `git` CLI.

- A good code editor such as Atom, VS Code, or Sublime.

Copy this template over by clicking __Use this template__ button found in the repository on GitHub. Save it to the `Software-for-Maths-Learning` Organisation.

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

## Contact