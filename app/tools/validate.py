import json, os

from typing import Union
from jsonschema import Draft7Validator as Validator

schema_path_local = '/Users/louismanestar/OneDrive - Imperial College London/Jobs/StudentShapers 2021/software-for-maths-learning/grading-script-boilerplate/concept_v2/app/request_body_schema.json'
schema_path_aws = '/app/request_body_schema.json'

path = os.path.abspath(os.path.dirname(__file__))
schema_path = os.path.join(path, "..", "request_body_schema.json")

# Load the request body schema and validator
with open(schema_path, 'r') as s:
    request_body_schema = json.load(s)
    request_body_validator = Validator(request_body_schema)

def validate_request(body: dict) -> Union[dict, None]:
    """
    Function to return any errors in the request body based on its schema.
    ---
    If there are no issues with the request body, then None is returned. Otherwise, a
    JSON-encodable response containing the schema and errors will be returned. Each
    element in the list of errors is a dictionary containing the error message and the
    path to the rule in the schema that has thrown the error.
    """
    
    if not request_body_validator.is_valid(body):
        error_list = []

        for e in request_body_validator.iter_errors(body):
            error_list.append({
                "message": e.message,
                "path": list(e.absolute_schema_path)
            })

        return {
            "message": "Schema threw an error when validating the request body.",
            "errors": error_list,
            "request_body_schema": request_body_schema
        }
    
    return None