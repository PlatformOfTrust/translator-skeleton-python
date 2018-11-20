"""
Application controllers are defined in this file.

The controllers handle all requests and routes, returns responses to consumers.
"""
import bottle

import app.responses as responses
import app.services as services
import utils
from webargs import fields

from exceptions import ValidationFailed
from log import logger


def request_args(args):
    """Decorator for request arguments.

    Defines fields that should be passed to the controller action.

    :param args: The arguments of the request.
    :type args: dict
    :return: The decorator.
    :rtype:
    """

    def _decorator(f):
        f.args = args
        return f

    return _decorator


class Status(object):
    """Status controller.

    Mainly used for health check endpoints, but can also add
    more status endpoints to the API.
    """

    @staticmethod
    def health_check() -> responses.JSONResponse:
        """Returns 200 OK with empty object.

        Used for health checks.

        :return: Empty response.
        :rtype: responses.JSONResponse
        """
        return responses.JSONResponse({})


class Translator(object):
    """Translator controller.

    Handles fetching and returning of the data.
    """
    _service = None  # type: services.Translator

    def __init__(self):
        """Initializes the translator controller"""
        self._service = services.Translator()

    @request_args({
        'timestamp': fields.Str(required=True),
        'productCode': fields.Str(required=True),
        'parameters': fields.Dict(allow_none=True),
    })
    def fetch(self, args: dict) -> responses.JSONResponse:
        """Returns the data to the PoT Broker API.

        :param args: The arguments for the request.
        :type args: dict
        :return: The translator data.
        :rtype: responses.JSONResponse
        :raise ValidationFailed: If the validation fails.
        """
        # Validate the headers, and the raw request body.
        try:
            raw_body = bottle.request.body.read()
            utils.validate(bottle.request.headers, raw_body.decode('utf-8'))
        except bottle.HTTPError:
            logger.exception('Validation failed.')
            raise ValidationFailed('Validation failed.')

        # Get the needed data, based on the parameters sent.
        data = self._service.get_data(args['parameters'])
        # Sign the data.
        headers = self._service.get_headers(data, bottle.request.headers)
        # Return the data.
        return responses.JSONResponse(data, headers=headers)