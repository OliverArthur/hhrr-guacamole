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
            registered_on=datetime.datetime.utcnow(),
            started_on=data['started_on']
        )
        save_changes(new_user)
        response_object = {
            'status': 'success',
            'message': 'Successfully registered.' 
        }
        return response_object, 201
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


def save_changes(data):
    db.session.add(data)
    db.session.commit()