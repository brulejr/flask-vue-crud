from flask import current_app, request
from flask_restplus import Resource, fields
import hashlib
import re
from werkzeug.security import check_password_hash

from . import api, auth_v1_ns
from app.services import auth_service


register_model = api.model('Register', {
    'username': fields.String(required=True),
    'password': fields.String(required=True)
})

return_token_model = api.model('ReturnToken', {
    'access_token': fields.String(required=True),
    'refresh_token': fields.String(required=True)
})

refresh_token_model = api.model('RefreshToken', {
    'refresh_token': fields.String(required=True)
})

user_resource_model = api.model('User', {
    'username': fields.String(required=True)
})


class ValidationException(Exception):
    def __init__(self, message='Validation error', error_field_name='unknown_field', *args):
        super().__init__(args)
        self.error_field_name = error_field_name
        self.message = message


@auth_v1_ns.route('/register')
class Register(Resource):
    # 4-16 symbols, can contain A-Z, a-z, 0-9, _ (_ can not be at the begin/end and can not go in a row (__))
    USERNAME_REGEXP = r'^(?![_])(?!.*[_]{2})[a-zA-Z0-9._]+(?<![_])$'

    # 6-64 symbols, required upper and lower case letters. Can contain !@#$%_  .
    PASSWORD_REGEXP = r'^(?=.*[\d])(?=.*[A-Z])(?=.*[a-z])[\w\d!@#$%_]{6,64}$'

    @auth_v1_ns.expect(register_model, validate=True)
    @auth_v1_ns.marshal_with(user_resource_model)
    @auth_v1_ns.response(400, 'username or password incorrect')
    def post(self):
        try:
            if not re.search(self.USERNAME_REGEXP, api.payload['username']):
                raise ValidationException(error_field_name='username',
                                          message='4-16 symbols, can contain A-Z, a-z, 0-9, _ \
                                          (_ can not be at the begin/end and can not go in a row (__))')

            if not re.search(self.PASSWORD_REGEXP, api.payload['password']):
                raise ValidationException(error_field_name='password',
                                          message='6-64 symbols, required upper and lower case letters. \
                                          Can contain !@#$%_')

            user = auth_service.get_user(username=api.payload['username'])
            if user:
                raise ValidationException(error_field_name='username', message='This username is already exists')

            user = auth_service.store_user(username=api.payload['username'], password=api.payload['password'])

            return user

        except ValidationException as e:
            auth_v1_ns.abort(400, e.message, field=e.error_field_name)


@auth_v1_ns.route('/login')
class Login(Resource):
    @auth_v1_ns.expect(register_model)
    @auth_v1_ns.response(200, 'Success', return_token_model)
    @auth_v1_ns.response(401, 'Incorrect username or password')
    def post(self):
        """
        Look implementation notes
        This API implemented JWT. Token's payload contain:
        'uid' (user id),
        'exp' (expiration date of the token),
        'iat' (the time the token is generated)
        """
        try:
            user = auth_service.find_user(username=api.payload['username'])

            if check_password_hash(user.password_hash, api.payload['password']):
                token_pair = auth_service.generate_token(user_id=user.id, secret=current_app.config['SECRET_KEY'])

                user_agent_string = request.user_agent.string.encode('utf-8')
                user_agent_hash = hashlib.md5(user_agent_string).hexdigest()

                refresh_token = auth_service.store_refresh_token(
                    user=user,
                    user_agent_hash=user_agent_hash,
                    refresh_token=token_pair.refresh_token
                )

                return {'access_token': token_pair.access_token, 'refresh_token': refresh_token.refresh_token}, 200

            else:
                auth_v1_ns.abort(401, 'Incorrect username or password')

        except auth_service.UserNotFoundException:
            auth_v1_ns.abort(401, 'Incorrect username or password')
        except auth_service.AuthenticationException:
            auth_v1_ns.abort(500, 'Unexpected authentication error')


@auth_v1_ns.route('/refresh')
class Refresh(Resource):
    @auth_v1_ns.expect(refresh_token_model, validate=True)
    @auth_v1_ns.response(200, 'Success', return_token_model)
    def post(self):
        try:
            refresh_token = api.payload['refresh_token']

            new_token_pair = auth_service.update_refresh_token(refresh_token, current_app.config['SECRET_KEY'])

            return new_token_pair, 200

        except auth_service.RefreshTokenNotFoundException:
            auth_v1_ns.abort(401, 'Unknown token error')
        except auth_service.RefreshTokenInvalidException:
            auth_v1_ns.abort(400, 'Invalid token error')
        except auth_service.AuthenticationException:
            auth_v1_ns.abort(500, 'Unexpected authentication error')
