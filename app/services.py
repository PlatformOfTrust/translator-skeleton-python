"""API services.

Application services are defined in this file.

Services usually handle communication with the database if it exists, or
sending requests to other services.
"""
import app.utils
import base64
import settings

from copy import copy


class Translator(object):
    """Translator service.

    Handles fetching of data depending on given parameters.
    """

    def get_data(self, params: dict) -> dict:
        """Returns data for the translator.

        Own functions may be defined in this class if needed, e.g.
        response parsing, fetching data from other sources etc.

        :param params: Parameters sent from the Data Broker API.
        :type params: dict
        :return: The data to be sent back to the Data Broker API.
        :rtype: dict
        """
        created_at = app.utils.rfc3339()
        # Get the data for the translator response here.
        data = {}
        signature = self.sign_data(data, created_at)
        # Set the @context, @type, signature.type, signature.creator
        # The signature.type MUST be same as defined in the data product
        # organizationPublicKeys[].type
        # The signature.creator MUST be same as defined in the data product
        # organizationPublicKeys[].url
        # If multiple keys are defined for the data product, at least one of
        # the defined keys MUST validate.
        return {
            '@context': '',
            '@type': '',
            'data': data,
            'signature': {
                'type': '',
                'created': created_at,
                'creator': '',
                'signatureValue': signature
            }
        }

    @staticmethod
    def sign_data(data: dict, created_at: str) -> str:
        """Generates a signature of the data.

        The signature is base64 encoded.

        The created_at time will be included in the data __signed__ key,
        and removed once the payload is signed.

        :param data: The data to sign.
        :type data: dict
        :param created_at: The created timestamp.
        :type created_at: str
        :return: The signature.
        :rtype: str
        """
        # Make a copy of the data, and include the created at time in the data.
        sign_data = copy(data)
        sign_data['__signed__'] = created_at
        # Todo: Use the corresponding private key that was defined in the
        #  data product organizationPublicKeys[].url
        signature = app.utils.generate_signed_data(
            sign_data,
            settings.PRIVATE_KEY
        )

        return base64.b64encode(signature).decode("utf-8")
