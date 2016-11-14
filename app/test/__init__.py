import unittest

from app import create_app


class AppTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app().test_client()

    def request_api_route(self, method, route):
        return getattr(self.app, method)('/api/v0%s' % route)
