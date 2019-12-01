from app.database import db


class Book(db.Model):
    book_id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(64), index=True)
    author = db.Column(db.String(120), index=True)
    genre = db.Column(db.String(120), index=True)
    read = db.Column(db.Boolean)

    def to_dict(self):
        return {
            'bookId': self.book_id,
            'title': self.title,
            'author': self.author,
            'genre': self.genre,
            'read': self.read
        }

    def __repr__(self):
        return '<Book {}>'.format(self.title)
