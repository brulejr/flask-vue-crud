from flask_restplus import Resource, fields

from . import api, book_ns
from app.services import books, BookNotFoundException


book = api.model('Book', {
    'bookId': fields.String(required=True, description='The book identifier'),
    'title': fields.String(required=True, description='The book title'),
    'author': fields.String(required=True, description='The book author'),
    'read': fields.String(required=False, description='The book read flag')
})
bookList = api.model('BookList', {
    'books': fields.Nested(book, description='Array of book')
})


parser = api.parser()
parser.add_argument('title', type=str, required=True, help='Title for the book', location='json')
parser.add_argument('author', type=str, required=True, help='Author for the book', location='json')
parser.add_argument('read', type=bool, required=False, help='Read flag for the book', location='json')


@book_ns.route('/')
class BookList(Resource):

    @api.doc(description='Get a list of books')
    @api.marshal_list_with(bookList)
    def get(self):
        book_list = books.get_books()
        context = {'books': []}
        for bookId in sorted(book_list.keys()):
            context['books'].append(book_list[bookId])
        return context

    @api.doc(parser=parser)
    @api.marshal_with(book, code=201)
    def post(self):
        args = parser.parse_args()
        added_book = books.add_book(
            title=args['title'],
            author=args['author'],
            read=args['read']
        )
        return added_book, 201


@book_ns.route('/<string:bookId>')
@api.param('bookId', 'The book identifier')
@api.response(404, 'Book not found')
class Book(Resource):

    @api.doc('get_book')
    @api.marshal_with(book)
    def get(self, bookId):
        try:
            return books.find_book(bookId)
        except BookNotFoundException:
            api.abort(404, message="Book {} doesn't exist".format(bookId))

    @api.doc(responses={204: 'Book deleted'})
    def delete(self, bookId):
        try:
            removed_book = books.delete_book(bookId)
            return removed_book, 204
        except BookNotFoundException:
            api.abort(404, message="Book {} doesn't exist".format(bookId))

    @api.doc(parser=parser)
    @api.marshal_with(book)
    def put(self, bookId):
        try:
            args = parser.parse_args()
            updated_book = books.update_book(book_id=bookId, new_book=args)
            return updated_book, 201
        except BookNotFoundException:
            api.abort(404, message="Book {} doesn't exist".format(bookId))
