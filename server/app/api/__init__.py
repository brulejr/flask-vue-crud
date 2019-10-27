from flask import Blueprint
from flask_restplus import Api

apiv1 = Blueprint('api', __name__, url_prefix='/v1')
api = Api(
    apiv1,
    version='1.0',
    title='Library API',
    description='A simple demo API'
)

auth_ns = api.namespace('auth', 'Auth methods')
book_ns = api.namespace('book', 'Book methods')
ping_ns = api.namespace('ping', 'Ping methods')

from .auth_api import api as auth_api
from .book_api import api as book_api
from .ping_api import api as ping_api
