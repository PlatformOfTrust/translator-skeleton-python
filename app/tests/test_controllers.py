"""
Application unit tests for controllers are defined in this file.
"""
from webtest import TestApp as WebTestApp, \
    TestResponse as WebTestResponse

from application import application
from snapshottest import TestCase


class BaseTestCase(TestCase):
    """Base test case.

    Sets up things needed for all test cases.
    """
    _response = None  # type: WebTestResponse
    _app = None  # type: WebTestApp

    def setUp(self) -> None:
        """Sets up the web test application.

        :return: None
        :rtype: None
        """
        self._app = WebTestApp(application)


class TestStatusController(BaseTestCase):
    """Tests the status controller."""

    def setUp(self) -> None:
        super().setUp()

    def testHealth(self) -> None:
        """Tests the health check endpoint.

        :return: None
        :rtype: None
        """
        self._response = self._app.get('/health')

        self.assertEqual(self._response.status, '200 OK')
