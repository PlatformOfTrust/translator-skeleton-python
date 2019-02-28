"""API Utils.

Application utilities are defined in this file.
Any helper functions should be defined here.
"""
import base64
import dateutil.parser
import json
import settings

from datetime import datetime, timezone
from exceptions import (
    MissingRequiredHeaderError,
    ValidationError
)
from jwt.algorithms import RSAAlgorithm

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
        'required': True,
    },
}


def rfc3339() -> str:
    """Gets the current datetime in UTC iso formatted string.

    E.g. "2019-01-01T12:00:00+00:00"

    :return: The current UTC datetime in ISO format.
    :rtype: str
    """
    return str(datetime.now(timezone.utc).isoformat(timespec='seconds'))


def get_current_utc() -> datetime:
    """Gets the current datetime in UTC.

    :return: The UTC time.
    :rtype: datetime
    """
    return get_datetime_from_date_string(rfc3339())


def get_datetime_from_date_string(date_string: str) -> datetime:
    """Returns a datetime object from given date string.

    :param date_string: The date string.
    :type date_string: str
    :return: The datetime object.
    :rtype: datetime
    """
    return dateutil.parser.parse(date_string)


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

    valid_signature = validate_signed_data(
        body,
        base64.b64decode(headers[X_POT_SIGNATURE].encode('utf-8')),
        settings.POT_PUBLIC_KEY
    )
    if not valid_signature:
        raise ValidationError('Signature validation failed.')

    # Todo: validate timestamp as well.


def get_signature_payload(body) -> str:
    """Returns the signature payload as a string.

    The body of the payload may be a dict or a string.

    :param body: The body to be hashed.
    :type body: str|dict
    :return: The body hash.
    :rtype: str
    :raise RuntimeError: IF the body is not a string or dict.
    """
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

    return body_hash


def generate_signed_data(payload, private_pem: str) -> str:
    """Generates signature for payload.

    :param payload: The payload to sign.
    :type payload: str|dict
    :param private_pem: The private key used for signing.
    :type private_pem: str
    :return: The signature.
    :rtype: str
    """
    payload_hash = get_signature_payload(payload)
    alg_obj = RSAAlgorithm(RSAAlgorithm.SHA256)
    key = alg_obj.prepare_key(private_pem)
    return alg_obj.sign(payload_hash.encode('utf-8'), key)


def validate_signed_data(payload, signature: str, public_pem: str) -> bool:
    """Validates a signature for given payload.

    :param payload: The payload to validate.
    :type payload: str|dict
    :param signature: The signature to validate.
    :type signature: str
    :param public_pem: The public key used for validating.
    :type public_pem: str
    :return: True if signature valid, False otherwise.
    :rtype: bool
    """
    payload_hash = get_signature_payload(payload)
    alg_obj = RSAAlgorithm(RSAAlgorithm.SHA256)
    key = alg_obj.prepare_key(public_pem)
    return alg_obj.verify(payload_hash.encode('utf-8'), key, signature)
