from unittest import TestCase
from app import app


class BaseTest(TestCase):
    def setUP(self):
        app.testing = True
        self.app = app.test_client()
