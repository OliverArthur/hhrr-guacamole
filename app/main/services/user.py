import uuid
import datetime

from app.main import db
from app.main.models.user import User


def create_new_user(data):
    user = User.query.filter_by(email=data['email']).first()

    if not user:
        new_user = User(
            email=data['email'],
            last_name=data['last_name'],
            name=data['name'],
            password=data['password'],
            public_id=str(uuid.uuid4()),
            registered_on=datetime.datetime.utcnow()
        )
        save_changes(new_user)
        return generate_token(new_user)
    else:
        response_object = {
            'status': 'error',
            'message': 'User already exists, Please log in'
        }
        return response_object, 409


def get_all_users():
    return User.query.all()


def get_an_user(public_id):
    return User.query.filter_by(public_id=public_id).first()


def generate_token(user):
    try:
        auth_token = User.encode_auth_token(user.id)
        response_object = {
            'status': 'success',
            'message': 'Successfully registered.',
            'Authorization': auth_token.decode()
        }

        return response_object, 201

    except Exception as e:
        response_object = {
            'status': 'error',
            'message': 'Some error occurred. Please try again.'
        }

        return response_object, 401


def save_changes(data):
    db.session.add(data)
    db.session.commit()
