from flask_restplus import Resource, fields

from .api import api, ping_ns


@ping_ns.route('/')
class Ping(Resource):

    @api.doc(description='Pings a service')
    def get(self):
        return "pong"
