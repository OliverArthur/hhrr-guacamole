from flask_restplus import Api
from flask import Blueprint

from .main.controller.user import api as user_ns

blueprint = Blueprint('api', __name__)

api = Api(blueprint,
    title='HHRR API',
    version='1.0',
    description='API for the HHRR app client'
)

api.add_namespace(user_ns, path='/user')