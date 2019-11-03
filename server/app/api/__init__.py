from flask import Blueprint
from flask_restplus import Api

apiv1 = Blueprint('api', __name__, url_prefix='/api/v1')
api = Api(
    apiv1,
    version='1.0',
    title='Library API',
    description='A simple demo API'
)

auth_v1_ns = api.namespace('auth', 'Auth methods')
book_v1_ns = api.namespace('book', 'Book methods')
ping_v1_ns = api.namespace('ping', 'Ping methods')

from .auth_v1_api import api as auth_v1_api
from .book_v1_api import api as book_v1_api
from .ping_v1_api import api as ping_v1_api
