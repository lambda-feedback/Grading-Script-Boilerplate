import unittest

from ..algorithm import grading_function
from ..scripts.validate import validate_request

"""
    TestCase Class used to create unittests for the grading function.
"""

class TestGradingFunction(unittest.TestCase):
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

if __name__ == "__main__":
    unittest.main()