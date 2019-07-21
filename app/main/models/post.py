from slugify import slugify
from sqlalchemy import event

from .. import db


class Post(db.Model):
    """ Post Model for storing user's posts """

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(180), nullable=False)
    body = db.Column(db.Text, nullable=False)
    image_url = db.Column(db.String)
    slug = db.Column(db.String(80), unique=True)
    likes = db.Column(db.Integer, default=0)
    created_at = db.Column(db.DateTime, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    @staticmethod
    def generate_slug(target, value, oldValue, initiador):
        if value and (not target.slug or value != oldValue):
            target.slug = slugify(value)

    def __repr__(self):
        return "<Post {}>".format(self.id)


event.listen(Post.title, 'set', Post.generate_slug, retval=False)
