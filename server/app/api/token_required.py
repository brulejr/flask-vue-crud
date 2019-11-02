from flask import request, current_app
import jwt

from app.models.auth import User
from app.api import api


# required_token decorator
def token_required(f):
    def wrapper(*args, **kwargs):
        auth_header = request.headers.get('Authorization')
        current_user = None
        if auth_header:
            try:
                access_token = auth_header.split(' ')[1]

                try:
                    token = jwt.decode(access_token, current_app.config['SECRET_KEY'])
                    current_user = User.query.get(token['uid'])
                    print('current_user', current_user)
                except jwt.ExpiredSignatureError as e:
                    api.abort(401, 'Token expired')
                except (jwt.DecodeError, jwt.InvalidTokenError) as e:
                    api.abort(403, 'Token invalid')
                except:
                    api.abort(403, 'Unknown token error')

            except IndexError:
                api.abort(400, 'Token format invalid')
        else:
            api.abort(403, 'Token required')
        return f(*args, **kwargs, current_user=current_user)

    wrapper.__doc__ = f.__doc__
    wrapper.__name__ = f.__name__
    return wrapper
