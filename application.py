"""
Main application.
"""
import bottle
import settings
import routes
import log

application = bottle.Bottle()
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
