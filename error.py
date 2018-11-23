"""
Custom error handler for the API.
"""
import bottle
import json


def custom_error_handler(error: bottle.HTTPError) -> str:
    """Defines the custom error handler for HTTPErrors.

    :param error: The HTTPError.
    :type error: bottle.HTTPError
    :return: JSON string of the error.
    :rtype: str
    """
    try:
        body = json.loads(error.body)
    except json.decoder.JSONDecodeError:
        body = error.body

    data = {
        'error': {
            'status': error.status_code,
            'message': body,
        }
    }
    return json.dumps(data)


# Add more error codes here if needed.
handler = {
    422: custom_error_handler,
    500: custom_error_handler,
}
