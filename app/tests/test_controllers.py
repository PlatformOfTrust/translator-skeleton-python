"""
Application unit tests for controllers are defined in this file.
"""
from webtest import TestApp as WebTestApp, \
    TestResponse as WebTestResponse

import utils
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


class TestTranslatorController(BaseTestCase):
    """Tests the translator controller."""

    _body = {
        "timestamp": "2018-11-01T12:01:01Z",
        "productCode": "product-1",
        "parameters": {
            "name": "The name",
        }
    }

    def setUp(self):
        super().setUp()

    def testSignatureValidation(self):
        """Tests the generating and validating of the signature.

        :return: None
        :rtype: None
        """
        signature = utils.generate_signature(self._body)

        self.assertTrue(utils.validate_signature(signature, self._body))

    def testFetch(self):
        """Tests the fetch endpoint.

        :return: None
        :rtype: None
        """
        signature = utils.generate_signature(self._body)
        headers = {
            'X-Pot-Signature': signature
        }
        self._response = self._app.post_json('/fetch',
                                             params=self._body,
                                             headers=headers)

        self.assertEqual(self._response.status, '200 OK')

        self.assertMatchSnapshot(self._response.json_body)

    def testFailedSignature(self):
        """Tests invalid body against signature.

        :return: None
        :rtype: None
        """
        signature = utils.generate_signature(self._body)

        self.assertFalse(
            utils.validate_signature(
                signature,
                '{"timestamp": "2018-11-01T12:01:01Z", '
                '"productCode": "product-1"}'
            )
        )

    def testMissingAttribute(self):
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

        signature = utils.generate_signature(params)
        headers = {
            'X-Pot-Signature': signature
        }
        self._response = self._app.post_json('/fetch',
                                             params=params,
                                             headers=headers,
                                             expect_errors=True)

        self.assertMatchSnapshot(self._response.json_body)
