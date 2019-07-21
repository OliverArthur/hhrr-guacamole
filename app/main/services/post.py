import datetime

from app.main import db
from app.main.models.post import Post


def create_new_post(data):
    try:
        post = Post(
            title=data['title'],
            body=data['body'],
            image_url=data['image_url'],
            created_at=datetime.datetime.utcnow()
        )

        save_change(post)
        response_object = {
            'status': 'success',
            'message': 'Post created Successfully'
        }
        return response_object, 201

    except Exception as e:
        print(e)
        response_object = {
            'status': 'error',
            'message': 'Some error occurred. Please try again.'
        }
        return response_object, 403


def save_change(data):
    db.session.add(data)
    db.session.commit()
