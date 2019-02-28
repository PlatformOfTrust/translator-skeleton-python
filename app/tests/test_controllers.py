"""API tests.

Application unit tests for controllers are defined in this file.
"""
import app.utils
import settings

from application import application
from snapshottest import TestCase
from webtest import (
    TestApp as WebTestApp,
    TestResponse as WebTestResponse
)


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

    def test_health(self) -> None:
        """Tests the health check endpoint.

        :return: None
        :rtype: None
        """
        self._response = self._app.get('/health')

        self.assertEqual(self._response.status, '200 OK')


class TestTranslatorController(BaseTestCase):
    """Tests the translator controller."""

    _body = {
        'timestamp': '2018-11-01T12:01:01Z',
        'productCode': 'product-1',
        'parameters': {
            'name': 'The name',
        }
    }

    def setUp(self):
        super().setUp()

    def test_signature_validation(self):
        """Tests the generating and validating of the signature.

        :return: None
        :rtype: None
        """
        signature = app.utils.generate_signed_data(
            self._body,
            settings.PRIVATE_KEY
        )

        self.assertTrue(app.utils.validate_signed_data(
            self._body,
            signature,
            settings.PUBLIC_KEY
        ))

    def test_fetch(self):
        """Tests the fetch endpoint.

        :return: None
        :rtype: None
        """
        headers = {
            'X-Pot-Signature': 'foo',
            'X-Pot-App': 'bar'
        }
        self._response = self._app.post_json('/fetch',
                                             params=self._body,
                                             headers=headers)

        self.assertEqual(self._response.status, '200 OK')

        self.assertMatchSnapshot(self._response.json_body)

    def test_failed_signature(self):
        """Tests invalid body against signature.

        :return: None
        :rtype: None
        """
        signature = app.utils.generate_signed_data(
            self._body,
            settings.PRIVATE_KEY
        )

        self.assertFalse(
            app.utils.validate_signed_data(
                {
                    'productCode': 'product-1'
                },
                signature,
                settings.PUBLIC_KEY
            )
        )

    def test_missing_attribute(self):
        """Tests missing mandatory attribute.

        :return: None
        :rtype: None
        """
        params = {
            'timestamp': '2018-11-01T12:01:01Z',
            'parameters': {
                'name': 'Test'
            }
        }

        headers = {
            'X-Pot-Signature': 'foo',
            'X-Pot-App': 'bar'
        }
        self._response = self._app.post_json('/fetch',
                                             params=params,
                                             headers=headers,
                                             expect_errors=True)

        self.assertMatchSnapshot(self._response.json_body)
