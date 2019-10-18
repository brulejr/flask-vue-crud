from collections import OrderedDict


BOOKS = OrderedDict([
    ('1', {'bookId': '1', 'title': 'On the Road', 'author': 'Jack Kerouac', 'read': True}),
    ('2', {'bookId': '2', 'title': 'Harry Potter', 'author': 'J. K. Rowling', 'read': False}),
    ('3', {'bookId': '3', 'title': 'Green Eggs and Ham', 'author': 'Dr. Seuss', 'read': True})
])


class BookNotFoundException(Exception):
    pass


def add_book(title, author, read):
    book_id = '{}'.format(int(max(BOOKS.keys())) + 1)
    BOOKS[book_id] = {
        'bookId': book_id,
        'title': title,
        'author': author,
        'read': read
    }
    return BOOKS[book_id]


def delete_book(book_id):
    book = find_book(book_id)
    del BOOKS[book_id]
    return book


def find_book(book_id):
    if book_id in BOOKS:
        return BOOKS[book_id]
    else:
        raise BookNotFoundException(book_id)


def get_books():
    return BOOKS


def update_book(book_id, new_book):
    book = find_book(book_id)
    for item in new_book.keys():
        if item in book.keys() and new_book[item] is not None:
            book[item] = new_book[item]
    BOOKS[book_id] = book
    return book
