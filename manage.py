import tornado.httpserver
import tornado.ioloop

from src.app import create_app
from src.settings import app_config

def runserver():
    """ Serves Tornado App """
    app = create_app(app_config)
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(8000)
    tornado.ioloop.IOLoop.instance().start()

if __name__ == '__main__':
    runserver()
