"""
Application utilities are defined in this file.
"""
import base64
import json

from exceptions import (
    MissingRequiredHeaderError,
    ValidationError
)
import settings
import hmac
import hashlib

X_POT_SIGNATURE = 'x-pot-signature'
X_POT_TOKEN = 'x-pot-token'
X_POT_APP = 'x-pot-app'

SUPPORTED_HEADERS = {
    X_POT_SIGNATURE: {
        'required': True,
    },
    X_POT_TOKEN: {
        'required': False,
    },
    X_POT_APP: {
        'required': False,
    },
}


def validate(headers: dict, body: dict) -> None:
    """Validates headers, security.

    :param headers: The headers of the request.
    :type headers: dict
    :param body: The body to validate.
    :type body: dict
    :return: None
    :rtype: None
    :raise ValidationError: If the validation fails.
    :raise MissingRequiredHeaderError: If the validation fails.
    """
    for header, rules in SUPPORTED_HEADERS.items():
        if rules['required'] and header.lower() not in headers:
            raise MissingRequiredHeaderError(
                f'Missing required header "{header.lower()}"'
            )

    if validate_signature(headers[X_POT_SIGNATURE], json.dumps(body)):
        raise ValidationError('Signature validation failed.')

    # Todo: validate timestamp as well.


def validate_signature(signature: str, body: str) -> bool:
    """Validates the given signature.

    :param signature: The signature to validate.
    :type signature: str
    :param body: The request body
    :type body: str
    :return: True if signature verification successful, False otherwise.
    :rtype: bool
    """
    digest = get_digest(body)

    # Compare the digest and return the answer.
    return hmac.compare_digest(
        signature.encode('utf-8'),
        base64.b64encode(digest)
    )


def get_digest(body: str) -> str:
    """Returns the HMAC-SHA256 digest for the given body.

    :param body: The body to generate the digest for.
    :type body: str
    :return: The digest.
    :rtype: str
    """
    # Get the shared secret from the settings.
    secret = settings.SHARED_SECRET

    # Create the HMAC digest with SHA-256.
    return hmac.new(secret.encode('utf-8'),
                    body.encode('utf8'),
                    hashlib.sha256).digest()
