"""
Application exceptions are found in this file.

All HTTP exceptions sets the content-type to JSON by default.
All HTTP exceptions are derived from the Bottle HTTPResponse class.
"""
import json
from bottle import HTTPResponse, HTTPError


# HTTP responses.

class ValidationFailed(HTTPResponse):
    """Validation exception.

    If the validation of arguments fails, this exception is raised.
    """

    def __init__(self, body='', status=422, headers=None, **more_headers):
        if headers is None or 'Content-type' not in headers:
            headers = {'Content-type': 'application/json'}

        super(ValidationFailed, self).__init__(body=json.dumps(body),
                                               status=status,
                                               headers=headers,
                                               **more_headers)


class NotFound(HTTPResponse):
    """Not found exception.

    If a record is not found in the database, this exception is raised.
    """

    def __init__(self, body='', status=404, headers=None, **more_headers):
        if headers is None or 'Content-type' not in headers:
            headers = {'Content-type': 'application/json'}

        super(NotFound, self).__init__(body=json.dumps(body),
                                       status=status,
                                       headers=headers,
                                       **more_headers)


class FatalError(HTTPResponse):
    """Fatal error exception.

    If something unrecoverable happens, this exception is raised.
    """

    def __init__(self, body='', status=500, headers=None, **more_headers):
        if headers is None or 'Content-type' not in headers:
            headers = {'Content-type': 'application/json'}

        super(FatalError, self).__init__(body=json.dumps(body),
                                         status=status,
                                         headers=headers,
                                         **more_headers)


class Forbidden(HTTPResponse):
    """Forbidden exception.

    If a user doesn't have access to a resource/record, this exception is
    raised.
    """

    def __init__(self, body='', status=403, headers=None, **more_headers):
        if headers is None or 'Content-type' not in headers:
            headers = {'Content-type': 'application/json'}

        super(Forbidden, self).__init__(body=json.dumps(body),
                                        status=status,
                                        headers=headers,
                                        **more_headers)


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
        super(ValidationError, self).__init__(status, body, exception,
                                              traceback, **options)


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
        super(MissingRequiredHeaderError, self).__init__(
            status, body, exception, traceback, **options
        )
