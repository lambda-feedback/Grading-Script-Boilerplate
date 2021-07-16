import unittest

from ..algorithm import grading_function
from ..validate import validate_request

class TestGradingFunction(unittest.TestCase):
    """
        TestCase Class used to test the algorithm and the schema.
        ---
        Tests are used here to check that the algorithm written 
        is working as it should. 
        
        It's best practise to write these tests first to get a 
        kind of 'specification' for how your algorithm should 
        work, and you should run these tests before committing 
        your code to AWS.

        Read the docs on how to use unittest here:
        https://docs.python.org/3/library/unittest.html

        Use validate request to check that your schema and 
        grading_function() to check your algorithm are both 
        working as they should.
    """

    def test_invalid_grading_data(self):
        body = {"hello": "world"}

        validation_error = validate_request(body)

        self.assertNotEqual(validation_error, None)
        self.assertEqual(validation_error.get("message"), "Schema threw an error when validating the request body.")

    def test_valid_grading_data(self):
        body = {"command": "grade"}

        validation_error = validate_request(body)
        response = grading_function(body)

        self.assertEqual(validation_error, None)
        self.assertEqual(response.get("is_correct"), True)