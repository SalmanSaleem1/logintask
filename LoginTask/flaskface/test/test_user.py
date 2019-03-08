from flaskface.test.testbase import BaseTestCase
import unittest
from flaskface.Models import User
from flaskface import bcrypt
import json
from marshmallow import pprint


class TestUser(BaseTestCase):

    def test_check_password(self):
        user = User.query.filter_by(email='hamza@gmail.com').first()
        self.assertTrue(bcrypt.check_password_hash(user.password, 'salmanmayo'))
        self.assertFalse(bcrypt.check_password_hash(user.password, 'salman'))

    def test_user_registeration(self):
        print('test_user_registeration\n')
        with self.client:
            response = self.client.post('/registers', data=dict(
                name='Junaid', username='junaid', email='junaid@gmail.com',
                password='salmanmayo'
            ), follow_redirects=True)
            self.assertIn(b'', response.data)
            assert response.status_code == 200
            # pprint(response.data)

    def test_user_incorrect_registeration(self):
        with self.client:
            response = self.client.post('http://127.0.0.1:5000/registers', data=dict(
                name='waleed', usernname='waleed1', email='waleedgmail.com',
                password='salmanmayo'
            ), follow_redirects=True)
            self.assertIn(b'', response.data)
            assert response.status_code == 200


class TestUserLogin(BaseTestCase):

    def test_login_user(self):
        with self.client:
            response = self.client.post('http://127.0.0.1:5000/login', data=dict(
                email='hamza@gmail.com', password='salmanmayo'
            ), follow_redirects=True)
            self.assertIn(b'', response.data)
            assert response.status_code == 200


if __name__ == '__main__':
    unittest.main()
