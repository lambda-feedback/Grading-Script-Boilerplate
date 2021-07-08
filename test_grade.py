import unittest, grade, json

class TestGradingFunction(unittest.TestCase):
    def test_handle_bodyless_event(self):
        context = {}
        event = {
            "random": "metadata",
            "without": "a body"
        }

        response = grade.handler(event, context)

        self.assertEqual(response.get("message"), "No grading data supplied in request body.")
        self.assertEqual(response.get("is_graded"), False)

    def test_non_json_body(self):
        context = {}
        event = {
            "random": "metadata",
            "body": "{}}}{{{[][] this is not json."
        }

        response = grade.handler(event, context)

        self.assertEqual(response.get("message"), "Request body threw an error attempting to parse the request body.")
        self.assertEqual(response.get("is_graded"), False)

    def test_invalid_grading_data(self):
        context = {}
        body = {"hello": "world"}
        event = {
            "random": "metadata",
            "body": json.dumps(body)
        }

        response = grade.handler(event, context)

        self.assertEqual(response.get("message"), "Grading schema threw an error when validating the request body.")
        self.assertEqual(response.get("is_graded"), False)

    def test_valid_grading_data(self):
        context = {}
        body = {"type": "grade"}
        event = {
            "random": "metadata",
            "body": json.dumps(body)
        }

        response = grade.handler(event, context)

        self.assertEqual(response.get("is_graded"), True)
        self.assertEqual(response.get("is_correct"), True)

if __name__ == "__main__":
    unittest.main()