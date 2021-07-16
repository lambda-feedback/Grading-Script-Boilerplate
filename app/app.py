import json, unittest, sys, os

from .algorithm import grading_function
from .validate import validate_request

from .tests import HealthcheckRunner, TestGradingFunction

"""
    Healthcheck methods
"""

def healthcheck():
    no_stream = open(os.devnull, 'w')
    sys.stderr = no_stream

    loader = unittest.TestLoader()
    runner = HealthcheckRunner(verbosity=0)
    
    result = runner.run(loader.loadTestsFromTestCase(TestGradingFunction))

    sys.stderr = sys.__stderr__
    no_stream.close()

    return result

"""
    Parsing Method
"""

def load_body(body_text):
    body, response = None, None

    try:
        body = json.loads(body_text)
    except json.JSONDecodeError as e:
        response = {
            "message": "Request body is not valid JSON.",
            "error": {
                "message": e.msg,
                "position": e.pos
            }
        }
    except TypeError as e:
        response = {
            "message": "Request body is not decoded JSON.",
        }
    
    return (body, response)

def parse_body(event):
    body, response = None, None

    if "body" not in event:
        response = {"message": "No grading data supplied in request body."}
        return (None, response)

    if type(event["body"]) == str:
        body, response = load_body(event["body"])
    else:
        body = event["body"]
    
    return (body, response)

"""
    Main Handler Method used by AWS Lambda
"""

def handler(event, context={}):
    body, parse_error = parse_body(event)

    if parse_error:
        return parse_error
    
    validation_error = validate_request(body)

    if validation_error:
        return validation_error
    
    return {
        "command": body["command"],
        "result": grading_function(body) if body["command"] == "grade" \
            else healthcheck()
    }