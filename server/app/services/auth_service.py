import datetime
import jwt
from sqlalchemy.exc import SQLAlchemyError
from typing import NamedTuple

from app.models.auth import RefreshToken, User
from app.database import db


class TokenPair(NamedTuple):
    access_token: str
    refresh_token: str


class AuthenticationException(Exception):
    pass


class RefreshTokenExpiredException(AuthenticationException):
    pass


class RefreshTokenInvalidException(AuthenticationException):
    pass


class RefreshTokenNotFoundException(AuthenticationException):
    pass


class UserNotFoundException(AuthenticationException):
    pass


def find_user(username: str):
    try:
        user = User.query.filter_by(username=username).first()
        if user:
            return user
        else:
            raise UserNotFoundException(username)
    except SQLAlchemyError:
        raise AuthenticationException('Unexpected error while finding user by username ' + username)


def generate_token(user_id: str, secret: str):
    try:
        _access_token = jwt.encode({'uid': user_id,
                                    'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=15),
                                    'iat': datetime.datetime.utcnow()}, secret).decode('utf-8')
        _refresh_token = jwt.encode({'uid': user_id,
                                     'exp': datetime.datetime.utcnow() + datetime.timedelta(days=1),
                                     'iat': datetime.datetime.utcnow()}, secret).decode('utf-8')
        return TokenPair(access_token=_access_token, refresh_token=_refresh_token)
    except jwt.PyJWTError:
        raise AuthenticationException('Unexpected error while generating tokens for user ' + user_id)


def get_user(username: str):
    try:
        return User.query.filter_by(username=username).first()
    except SQLAlchemyError as e:
        print('error', e)
        raise AuthenticationException('Unexpected error while getting user by username ' + username)


def store_refresh_token(user: User, user_agent_hash: str, refresh_token: str):
    try:
        _refresh_token = RefreshToken.query.filter_by(user_agent_hash=user_agent_hash).first()
        if not _refresh_token:
            _refresh_token = RefreshToken(user_id=user.id, refresh_token=refresh_token, user_agent_hash=user_agent_hash)
        else:
            _refresh_token.refresh_token = refresh_token

        db.session.add(_refresh_token)
        db.session.commit()

        return _refresh_token

    except SQLAlchemyError:
        raise AuthenticationException('Unexpected error while storing refresh token for user ' + user)


def store_user(username: str, password: str):
    _user = User(username=username, password=password)
    db.session.add(_user)
    db.session.commit()
    return _user


def update_refresh_token(refresh_token: str, secret: str):
    try:

        payload = jwt.decode(refresh_token, secret)
        user_id = payload['uid']

        _refresh_token = RefreshToken.query.filter_by(user_id=user_id, refresh_token=refresh_token).first()
        if not _refresh_token:
            raise RefreshTokenNotFoundException(user_id)

        token_pair = generate_token(user_id=_refresh_token.user_id, secret=secret)
        _refresh_token.refresh_token = token_pair.refresh_token

        db.session.add(_refresh_token)
        db.session.commit()

        return {'access_token': token_pair.access_token, 'refresh_token': _refresh_token.refresh_token}

    except jwt.ExpiredSignatureError as e:
        raise RefreshTokenExpiredException(e)

    except (jwt.DecodeError, jwt.InvalidTokenError) as e:
        raise RefreshTokenInvalidException(e)
