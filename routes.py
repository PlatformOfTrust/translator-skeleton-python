"""API Routes

Application routes are defined in this file.
To add new routes, use app.route(<route>, <method>, <controller.action>)
If the controller action has any arguments defined, add as last parameter
apply=use_args(controller.action.args).
"""

import app.controllers as controllers
import bottle
from webargs.bottleparser import use_args

# Instantiate the controllers here, for easy mocking.
status = controllers.Status()
translator = controllers.Translator()


def setup_routing(app: bottle.Bottle):
    # Status
    app.route('/health', 'GET', status.health_check)

    # Translator
    app.route('/fetch', 'POST', translator.fetch,
              apply=use_args(translator.fetch.args))
