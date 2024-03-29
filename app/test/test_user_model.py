import unittest
import datetime

from app.main import db
from app.main.models.user import User
from app.test.base import BaseTestCase

class TestUserModel(BaseTestCase):

        def test_encode_auth_token(self):
            user = User(
                email='oliver@test.com',
                last_name='Arthur',
                name='Oliver',
                password='Test1234x',
                registered_on=datetime.datetime.utcnow()
            )
            db.session.add(user)
            db.session.commit()
            auth_token = User.encode_auth_token(user.id)
            self.assertTrue(isinstance(auth_token, bytes))

        def test_decode_auth_token(self):
            user = User(
                email='oliver@test.com',
                last_name='Arthur',
                name='Oliver',
                password='Test1234x',
                registered_on=datetime.datetime.utcnow()
            )

            db.session.add(user)
            db.session.commit()
            auth_token = user.encode_auth_token(user.id)
            self.assertTrue(isinstance(auth_token, bytes))
            self.assertTrue(User.decode_auth_token(auth_token.decode("utf-8") ) == 1)

if __name__ == '__main__':
    unittest.main()
