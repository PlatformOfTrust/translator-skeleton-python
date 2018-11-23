"""
Main application.
"""
import bottle

import error
import settings
import routes
import log

application = bottle.Bottle()
# Set our custom error handler.
application.error_handler = error.handler
# If debugging on, let bottle handle the exception.
if settings.DEBUG:
    application.catchall = True

bottle.debug(settings.DEBUG)

# Set up routes for app.
routes.setup_routing(application)

log.logger.info('Translator API started...')

log.logger.info(f'''
Application settings:
    server = "{settings.SERVER}"
    host = "{settings.HOST}"
    port = {settings.PORT}
    reloader = {settings.RELOAD}
    debug = {settings.DEBUG}
    ''')

if __name__ == "__main__":
    bottle.run(
        application,
        server=settings.SERVER,
        host=settings.HOST,
        port=settings.PORT,
        reloader=settings.RELOAD
    )
