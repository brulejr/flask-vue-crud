from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from werkzeug.security import generate_password_hash

from app.database import db


class RefreshToken(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, ForeignKey('user.id'))
    refresh_token = db.Column(db.String(50), unique=True)
    user_agent_hash = db.Column(db.String(80))


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50))
    password_hash = db.Column(db.String(80))
    refresh_tokens = relationship('RefreshToken', backref='user')

    @property
    def password(self):
        raise AttributeError('Password not readable')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)
