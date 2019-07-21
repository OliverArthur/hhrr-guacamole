import unittest
import json

from app.test.base import BaseTestCase


def create_new_post(self):
    return self.client.post(
        '/post/',
        data=json.dumps(dict(
            title='Hello world',
            body='new post from hello world',
            image_url='https://www.donalthrump.com/cat.jpg'
        )),
        content_type='application/json'
    )


class TestPostBlueprint(BaseTestCase):

    def test_create_new_post(self):
        """ Test create new post """
        with self.client:
            response = create_new_post(self)
            data = json.loads(response.data.decode())
            self.assertTrue(data['status'] == 'success')
            self.assertTrue(data['message'] == 'Post created Successfully')
            self.assertEqual(response.status_code, 201)


if __name__ == '__main__':
    unittest.main()
