"""
Exports factory fucntion for creating a tornado app
"""
from tornado.web import Application as TornadoApp

from .handlers import handlers

def create_app(app_config):
    app = TornadoApp(handlers, **app_config)
    return app
