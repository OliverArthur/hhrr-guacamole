from flask import request
from flask_restplus import Resource

from ..util.dto import PostDto
from ..services.post import create_new_post

api = PostDto.api
_post = PostDto.post


@api.route('/')
class PostList(Resource):
    @api.response(201, 'Post successfully created.')
    @api.expect(_post, validate=True)
    def post(self):
        """Create a new post"""
        data = request.json
        return create_new_post(data=data)
