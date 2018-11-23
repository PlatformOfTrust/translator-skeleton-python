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


def generate_signature(data: dict) -> str:
    """Returns the signature for the given data.

    :param data: The data to generate the signature on.
    :type data: dict
    :return: The generated signature.
    :rtype: str
    """
    digest = get_digest(data)
    return base64.b64encode(digest).decode()


def validate(headers: dict, body) -> None:
    """Validates headers, security.

    :param headers: The headers of the request.
    :type headers: dict
    :param body: The body to validate.
    :type body: str
    :return: None
    :rtype: None
    :raise ValidationError: If the validation fails.
    :raise MissingRequiredHeaderError: If the validation fails.
    """
    for header, rules in SUPPORTED_HEADERS.items():
        header = header.lower()
        if rules['required'] and header not in headers:
            raise MissingRequiredHeaderError(
                f'Missing required header "{header}"'
            )

    if not validate_signature(headers[X_POT_SIGNATURE], body):
        raise ValidationError('Signature validation failed.')

    # Todo: validate timestamp as well.


def validate_signature(signature: str, body) -> bool:
    """Validates the given signature.

    :param signature: The signature to validate.
    :type signature: str
    :param body: The request body
    :type body: str|dict
    :return: True if signature verification successful, False otherwise.
    :rtype: bool
    """
    # Validate the raw value of the body.
    digest = get_digest(body)

    # Compare the digest and return the answer.
    return hmac.compare_digest(
        signature.strip().encode('utf-8'),
        base64.b64encode(digest)
    )


def get_digest(body) -> str:
    """Returns the HMAC-SHA256 digest for the given body.

    :param body: The body to generate the digest for.
    :type body: str|dict
    :return: The digest.
    :rtype: str
    :raise RuntimeError: If the body is not a string or dictionary.
    """
    # Get the shared secret from the settings.
    secret = settings.SHARED_SECRET
    if not isinstance(body, (str, dict)):
        raise RuntimeError(
            f'Invalid body type. Must be `str` or `dict`, got {type(body)}')

    # Create the hash from the body dict.
    if isinstance(body, dict):
        body_hash = json.dumps(
            body,
            sort_keys=True,
            indent=None,
            separators=(',', ': ')
        ).strip()
    else:
        body_hash = body.strip()  # Strip white space from start and end.

    # Create the HMAC digest with SHA-256.
    return hmac.new(secret.encode('utf-8'),
                    body_hash.encode('utf-8'),
                    hashlib.sha256).digest()
