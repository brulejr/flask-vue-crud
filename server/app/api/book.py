from collections import OrderedDict
from flask_restplus import Resource, fields

from . import api, book_ns


book = api.model('Book', {
    'bookId': fields.String(required=True, description='The book identifier'),
    'title': fields.String(required=True, description='The book title'),
    'author': fields.String(required=True, description='The book author'),
    'read': fields.String(required=False, description='The book read flag')
})
bookList = api.model('BookList', {
    'books': fields.Nested(book, description='Array of book')
})

BOOKS = OrderedDict([
    ('1', {'bookId': '1', 'title': 'On the Road', 'author': 'Jack Kerouac', 'read': True}),
    ('2', {'bookId': '2', 'title': 'Harry Potter', 'author': 'J. K. Rowling', 'read': False}),
    ('3', {'bookId': '3', 'title': 'Green Eggs and Ham', 'author': 'Dr. Seuss', 'read': True})
])


def abort_if_book_doesnt_exist(bookId):
    if bookId not in BOOKS:
        api.abort(404, message="Book {} doesn't exist".format(bookId))


parser = api.parser()
parser.add_argument('title', type=str, required=True, help='Title for the book', location='json')
parser.add_argument('author', type=str, required=True, help='Author for the book', location='json')
parser.add_argument('read', type=bool, required=False, help='Read flag for the book', location='json')


@book_ns.route('/')
class BookList(Resource):

    @api.doc(description='Get a list of books')
    @api.marshal_list_with(bookList)
    def get(self):
        context = {'books': []}
        for bookId in sorted(BOOKS.keys()):
            context['books'].append(BOOKS[bookId])
        return context

    @api.doc(parser=parser)
    @api.marshal_with(book, code=201)
    def post(self):
        args = parser.parse_args()
        bookId = '{}'.format(int(max(BOOKS.keys()))+1)
        BOOKS[bookId] = {
            'bookId': bookId,
            'title': args['title'],
            'author': args['author'],
            'read': args['read']
        }
        return BOOKS[bookId], 201


@book_ns.route('/<string:bookId>')
@api.param('bookId', 'The book identifier')
@api.response(404, 'Book not found')
class Book(Resource):

    @api.doc('get_book')
    @api.marshal_with(book)
    def get(self, bookId):
        abort_if_book_doesnt_exist(bookId)
        return BOOKS[bookId]

    @api.doc(responses={204: 'Book deleted'})
    def delete(self, bookId):
        abort_if_book_doesnt_exist(bookId)
        del BOOKS[bookId]
        return '', 204

    @api.doc(parser=parser)
    @api.marshal_with(book)
    def put(self, bookId):
        abort_if_book_doesnt_exist(bookId)
        args = parser.parse_args()
        book = BOOKS[bookId]
        for item in args.keys():
            if item in book.keys() and args[item] is not None:
                book[item] = args[item]
        BOOKS[bookId] = book
        return book, 201
