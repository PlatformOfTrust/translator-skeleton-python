"""
Application logging.

Use this logger to log messages in the application.
"""
import logging
import settings


def get_logger(name: str = 'api') -> logging.Logger:
    """Returns the logger instance.

    :param name: Logger name.
    :type name: str
    :return: The logger instance.
    :rtype: logging.Logger
    """
    log = logging.getLogger(name)

    if settings.ENV == 'test':
        return log

    log.setLevel(logging.DEBUG)

    handler = logging.StreamHandler()
    handler.setLevel(logging.DEBUG)

    formatter = logging.Formatter(
        '[%(asctime)s] %(name)s [%(levelname)s]: %(message)s')

    handler.setFormatter(formatter)

    log.addHandler(handler)

    return log


logger = get_logger()
