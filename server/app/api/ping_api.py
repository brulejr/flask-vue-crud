from flask_restplus import Resource, fields

from . import api, ping_ns
from .token_required import token_required


@ping_ns.route('/')
class Ping(Resource):

    @api.doc(description='Pings a service')
    @token_required
    def get(self, current_user):
        return "pong"
