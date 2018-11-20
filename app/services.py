"""
Application services are defined in this file.

Services usually handle communication with the database if it exists, or
sending requests to other services.
"""


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
