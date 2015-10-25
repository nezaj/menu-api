#!/usr/bin/env python
import sys

import tornado.httpserver
import tornado.ioloop

from src.app import create_app
from src.settings import app_config

# TODO: Make this take args when you add things like port
# pylint: disable=unused-argument
def runserver(*args):
    """ Serves Tornado App """
    app = create_app(app_config)
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(8000)
    tornado.ioloop.IOLoop.instance().start()

commands = {
    'runserver': runserver
}

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print "Usage: ./manage.py <command> [args]"
        sys.exit(1)

    command = commands.get(sys.argv[1])
    if not command:
        print "{} not supported. Supported commands are: {}"\
            .format(sys.argv[1], commands.keys())
        sys.exit(1)
    options = sys.argv[2:] if len(sys.argv) > 2 else []

    command(*options)
