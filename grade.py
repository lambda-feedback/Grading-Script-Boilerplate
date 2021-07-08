from jsonschema import Draft7Validator as Validator
import unittest, json

"""
    Validation Methods
"""

with open('./schema.json', 'r') as s:
    schema = json.load(s)

def format_error(e):
    return {
        "message": e.message,
        "path": list(e.absolute_schema_path)
    }

"""
    Main Handler Method used by AWS LAmbda
"""

def handler(event, context):
    if "body" not in event:
        return {
            "message": "No grading data supplied in request body.",
            "is_graded": False
        }
    
    try:
        body = json.loads(event["body"])
    except json.JSONDecodeError as e:
        return {
            "message": "Request body threw an error attempting to parse the request body.",
            "is_graded": False,
            "error": {
                "message": e.msg,
                "position": e.pos
            }
        }        


    v = Validator(schema)

    if not v.is_valid(body):
        error_list = []

        for e in v.iter_errors(body):
            error_list.append(format_error(e))

        return {
            "message": "Grading schema threw an error when validating the request body.",
            "is_graded": False,
            "errors": error_list,
            "schema": schema
        }
    
    return {
        "is_graded": True,
        "is_correct": grade(body)
    }

"""
    Grading Function to be written by tutors
"""

def grade(body):
    return True