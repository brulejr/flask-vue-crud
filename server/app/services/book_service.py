from app.database import db
from app.models.book import Book


class BookNotFoundException(Exception):
    pass


def add_book(title, author, read):
    book = Book(
        title=title,
        author=author,
        read=read
    )
    db.session.add(book)
    db.session.commit()

    return book.to_dict()


def delete_book(book_id):
    book = Book.query.get(book_id)
    if book:
        book_dict = book.to_dict()
        db.session.delete(book)
        db.session.commit()
        return book_dict
    else:
        raise BookNotFoundException(book_id)


def find_book(book_id):
    book = Book.query.get(book_id)
    if book:
        return book.to_dict()
    else:
        raise BookNotFoundException(book_id)


def get_books():
    books = [book.to_dict() for book in Book.query.all()]
    return books


def update_book(book_id, new_book):
    book = Book.query.get(book_id)
    if book:
        book.title = new_book.title
        book.author = new_book.author
        book.read = new_book.read
        db.session.add(book)
        db.session.commit()
        return book.to_dict()
    else:
        raise BookNotFoundException(book_id)
