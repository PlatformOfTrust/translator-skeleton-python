"""
Application routes are defined in this file.
"""
import bottle
from webargs.bottleparser import use_args

import app.controllers as controllers

# Instantiate the controllers here, for easy mocking.
status = controllers.Status()
translator = controllers.Translator()


def setup_routing(app: bottle.Bottle):
    # Status
    app.route('/health', 'GET', status.health_check)

    # Translator
    app.route('/fetch', 'POST', translator.fetch,
              apply=use_args(translator.fetch.args))
