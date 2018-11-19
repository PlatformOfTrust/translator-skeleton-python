"""
Application services are defined in this file.

Services usually handle communication with the database if it exists, or
sending requests to other services.
"""
import base64
import json

import utils


class Translator(object):
    """Translator service.

    Handles fetching of data depending on given parameters.
    """

    def __init__(self):
        pass

    def get_data(self, params: dict) -> dict:
        """Returns data for the translator.

        :param params: Parameters sent from the Data Broker API.
        :type params: dict
        :return: The data to be sent back to the Data Broker API.
        :rtype: dict
        """
        return {}

    @staticmethod
    def get_headers(data: dict, existing_headers: dict) -> dict:
        """Sign the data and add to headers.

        :param data: The data to sign.
        :type data: dict
        :param existing_headers: The existing headers.
        :type existing_headers: dict
        :return: The headers to pass on to the Data Broker API
        :rtype: dict
        """
        # Get the digest for the data.
        digest = utils.get_digest(json.dumps(data))

        # Encode the signature.
        signature = base64.b64encode(digest).decode()

        # Keep the existing headers that we need.
        _headers = {}
        for header, value in existing_headers.items():
            if header.lower() in utils.SUPPORTED_HEADERS:
                _headers[header] = value

        # Add the signature to the headers, this will override the previous
        # header that we got from the Data Broker API.
        _headers[utils.X_POT_SIGNATURE] = signature

        return _headers
