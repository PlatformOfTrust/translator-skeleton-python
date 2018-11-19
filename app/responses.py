"""
Responses are defined in this file.

The responses are returned in the controllers to the consumer.
"""
from bottle import HTTPResponse


class JSONResponse(HTTPResponse):
    """JSONResponse class.

    Content-Type defaults to application/json.
    This class should be used by default when returning data from the API.
    """

    def __init__(self, body='', status=None, headers=None, **more_headers):
        if not headers:
            headers = dict()

        if 'Content-Type' not in headers:
            headers['Content-Type'] = 'application/json'

        super(JSONResponse, self).__init__(body, status, headers,
                                           **more_headers)
