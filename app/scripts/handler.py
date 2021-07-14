import json, unittest, sys, os

from .validate import validate_request

from ..algorithm import grading_function
from ..tests import HealthcheckRunner, TestGradingFunction

"""
    Healthcheck methods
"""

def healthcheck():
    load_test_case = unittest.TestLoader().loadTestsFromTestCase
    grading_function_tests = load_test_case(TestGradingFunction)

    no_stream = open(os.devnull, 'w')
    sys.stderr = no_stream

    test_runner = HealthcheckRunner(verbosity=0)
    result = test_runner.run(grading_function_tests)

    sys.stderr = sys.__stderr__
    no_stream.close()

    return result

"""
    Parsing Method
"""

def parse_body(event):
    if "body" not in event:
        response = {"message": "No grading data supplied in request body."}
        return (None, response)

    try:
        body = json.loads(event["body"])
    except json.JSONDecodeError as e:

        response = {
            "message": "Request body threw an error attempting to parse the request body.",
            "error": {
                "message": e.msg,
                "position": e.pos
            }
        }

        return (None, response)
    
    return (body, None)

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