API_NAME = 'translator-skeleton-python'
# One place to change the environment names.
ENV_DEVELOPMENT = 'development'
ENV_STAGING = 'staging'
ENV_PRODUCTION = 'production'

SUPPORTED_ENVIRONMENTS = [
    ENV_DEVELOPMENT,
    ENV_STAGING,
    ENV_PRODUCTION,
]

# environment (production, staging, development, test)
ENV = ENV_DEVELOPMENT

# server backend (cherrypy, gunicorn, waitress, tornado, wsgiref, ...)
# if set to '', a default server backend will be used
SERVER = 'wsgiref'

# define host
HOST = '0.0.0.0'
# define port
PORT = 8080

# debug error messages
DEBUG = True

# auto-reload
RELOAD = True

# The shared secret that was generated when the data product was created.
SHARED_SECRET = 'very_secret123'

# Load local settings if any.
try:
    from settings_local import *
except ImportError:
    pass
