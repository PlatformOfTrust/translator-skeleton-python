"""
Application exceptions are found in this file.

All HTTP exceptions sets the content-type to JSON by default.
All HTTP exceptions are derived from the Bottle HTTPResponse class.
"""
import json
from bottle import HTTPResponse, HTTPError


# HTTP responses.

class BaseResponse(HTTPResponse):
    """Base HTTPResponse class.

    Sets the content-type header and standardizes the error message.
    """

    def __init__(self, body='', status=400, headers=None, **more_headers):
        """Base response exception.

        All exception responses should be derived from this base class.

        :param body: The body of the response.
        :type body: str|dict
        :param status: The HTTP status. Defaults to 400 Bad Request.
        :type status: int
        :param headers: Response headers.
        :type headers: dict
        :param more_headers: Additional headers.
        :type more_headers: dict
        """
        if headers is None:
            headers = dict()

        if 'Content-type' not in headers:
            headers = {'Content-type': 'application/json'}

        _body = {
            'error': {
                'status': status,
                'message': body
            }
        }
        super(BaseResponse, self).__init__(
            json.dumps(_body), status, headers, **more_headers
        )


class ValidationFailed(BaseResponse):
    """Validation exception.

    If the validation of arguments fails, this exception is raised.
    """

    def __init__(self, body='', status=422, headers=None, **more_headers):
        """Validation failed response.

        :param body: The body of the response.
        :type body: str|dict
        :param status: The HTTP status.
        :type status: int
        :param headers: Response headers.
        :type headers: dict
        :param more_headers: Additional headers.
        :type more_headers: dict
        """
        super(ValidationFailed, self).__init__(
            body, status, headers, **more_headers
        )


class NotFound(BaseResponse):
    """Not found exception.

    If a record is not found in the database, this exception is raised.
    """

    def __init__(self, body='', status=404, headers=None, **more_headers):
        """Not Found response.

        :param body: The body of the response.
        :type body: str|dict
        :param status: The HTTP status.
        :type status: int
        :param headers: Response headers.
        :type headers: dict
        :param more_headers: Additional headers.
        :type more_headers: dict
        """
        super(NotFound, self).__init__(
            body, status, headers, **more_headers
        )


# HTTP Errors

class ValidationError(HTTPError):
    """Validation error.

    If a validation error occurs, this exception is raised.
    """

    def __init__(self,
                 body='',
                 status=422,
                 exception=None,
                 traceback=None,
                 **options):
        """Validation error.

        :param body: The body/message of the error.
        :type body: str|dict
        :param status: The HTTP status.
        :type status: int
        :param exception: The exception.
        :type exception: Exception
        :param traceback: The backtrace of the exception.
        :type traceback: str
        :param options: Additional options.
        :type options: dict
        """
        super(ValidationError, self).__init__(
            status, body, exception, traceback, **options
        )


class MissingRequiredHeaderError(HTTPError):
    """Required header missing error.

    If a required header is missing, this exception is raised.
    """

    def __init__(self,
                 body='',
                 status=422,
                 exception=None,
                 traceback=None,
                 **options):
        """Missing required header error.

        :param body: The body/message of the error.
        :type body: str|dict
        :param status: The HTTP status.
        :type status: int
        :param exception: The exception.
        :type exception: Exception
        :param traceback: The backtrace of the exception.
        :type traceback: str
        :param options: Additional options.
        :type options: dict
        """
        super(MissingRequiredHeaderError, self).__init__(
            status, body, exception, traceback, **options
        )
