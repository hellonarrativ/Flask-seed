import json

from test import AppTestCase


class TestHelloWorld(AppTestCase):
    def test_returns_hello_world(self):
        response = self.request_api_route('get', '/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.data), {'data': 'Hello, World!'})
