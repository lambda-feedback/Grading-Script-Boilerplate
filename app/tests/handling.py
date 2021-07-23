import unittest, json

from pprint import pprint

from ..tools.app import handler

class TestHandlerFunction(unittest.TestCase):
    def __init__(self, methodName: str) -> None:
        super().__init__(methodName=methodName)
        self._response = {}

    def tearDown(self) -> None:
        #pprint(self._response)

        return super().tearDown()

    def test_handle_bodyless_event(self):
        event = {
            "random": "metadata",
            "without": "a body"
        }

        self._response = handler(event)

        self.assertEqual(self._response.get("message"), "LookupError: No grading data supplied in request body.")

    def test_non_json_body(self):
        event = {
            "random": "metadata",
            "body": "{}}}{{{[][] this is not json."
        }

        self._response = handler(event)

        self.assertEqual(self._response.get("message"), "JSONDecodeError: Request body is not valid JSON.")

    def test_healthcheck(self):
        body = {"command": "healthcheck"}
        event = {
            "random": "metadata",
            "body": json.dumps(body)
        }

        self._response = handler(event)
        self.assertEqual(self._response.get("command"), "healthcheck")

        result = self._response.get("result")
        self.assertNotEqual(len(result.get("successes")), 0)
        self.assertTrue(result.get("tests_passed"))

if __name__ == "__main__":
    unittest.main()