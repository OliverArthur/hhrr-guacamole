from flask_restplus import Namespace, fields


class UserDto:
    api = Namespace('user', description='user related operations')
    user = api.model('user', {
        'email': fields.String(required=True, description='user email address'),
        'last_name': fields.String(required=True, description='user last name'),
        'name': fields.String(required=True, description='user name'),
        'password': fields.String(required=True, description='user password'),
        'public_id': fields.String(description='user Identifier')
    })


class AuthDto:
    api = Namespace('auth', description='authentication related operations')
    user_auth = api.model('auth_details', {
        'email': fields.String(required=True, description='The email address'),
        'password': fields.String(required=True, description='The user password')
    })


class PostDto:
    api = Namespace('post', description='post related operations')
    post = api.model('post', {
        'title': fields.String(required=True, description='The post title'),
        'body': fields.String(required=True, description='The post text body'),
        'image_url': fields.String(required=False, description='The post main image')
    })
