from flask_restplus import Resource, fields

from . import api, book_v1_ns
from .token_required import token_required
from app.services import book_service, BookNotFoundException


book = api.model('Book', {
    'bookId': fields.String(required=True, description='The book identifier'),
    'title': fields.String(required=True, description='The book title'),
    'author': fields.String(required=True, description='The book author'),
    'read': fields.Boolean(required=False, description='The book read flag')
})
bookList = api.model('BookList', {
    'books': fields.Nested(book, description='Array of book')
})


parser = api.parser()
parser.add_argument('title', type=str, required=True, help='Title for the book', location='json')
parser.add_argument('author', type=str, required=True, help='Author for the book', location='json')
parser.add_argument('read', type=bool, required=False, help='Read flag for the book', location='json')


@book_v1_ns.route('/')
class BookList(Resource):

    @api.doc(description='Get a list of books')
    @api.marshal_list_with(bookList)
    @token_required
    def get(self, current_user):
        book_list = book_service.get_books()
        return {'books': book_list}

    @api.doc(parser=parser)
    @api.marshal_with(book, code=201)
    @token_required
    def post(self, current_user):
        args = parser.parse_args()
        added_book = book_service.add_book(
            title=args['title'],
            author=args['author'],
            read=args['read']
        )
        return added_book, 201


@book_v1_ns.route('/<string:bookId>')
@api.param('bookId', 'The book identifier')
@api.response(404, 'Book not found')
class Book(Resource):

    @api.doc('get_book')
    @api.marshal_with(book)
    @token_required
    def get(self, current_user, bookId):
        try:
            return book_service.find_book(bookId)
        except BookNotFoundException:
            api.abort(404, message="Book {} doesn't exist".format(bookId))

    @api.doc(responses={204: 'Book deleted'})
    @token_required
    def delete(self, current_user, bookId):
        try:
            removed_book = book_service.delete_book(bookId)
            return removed_book, 204
        except BookNotFoundException:
            api.abort(404, message="Book {} doesn't exist".format(bookId))

    @api.doc(parser=parser)
    @api.marshal_with(book)
    @token_required
    def put(self, current_user, bookId):
        try:
            args = parser.parse_args()
            updated_book = book_service.update_book(book_id=bookId, new_book=args)
            return updated_book, 201
        except BookNotFoundException:
            api.abort(404, message="Book {} doesn't exist".format(bookId))
