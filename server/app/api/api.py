from flask import Blueprint
from flask_restplus import Api


apiv1 = Blueprint('api', __name__, url_prefix='/v1')
api = Api(
    apiv1,
    version='1.0',
    title='Library API',
    description='A simple demo API'
)

book_ns = api.namespace('book', 'Book methods')
ping_ns = api.namespace('ping', 'Ping methods')
