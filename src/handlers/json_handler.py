"""
Request handler where requests and responses speak JSON
Thanks: https://gist.github.com/mminer/5464753
"""
import json

from tornado.web import RequestHandler

class JsonHandler(RequestHandler):

    def prepare(self):
        self.response = dict()

    def set_default_headers(self):
        self.set_header('Content-type', 'application/json')

    def write_json(self):
        output = json.dumps(self.response)
        self.write(output)
