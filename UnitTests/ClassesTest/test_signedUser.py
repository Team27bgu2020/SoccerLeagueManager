from unittest import TestCase
from Domain.SignedUser import *


class TestSignedUser(TestCase):
    def test_edit_personal_data(self):
        # Testing all valid inputs
        user = SignedUser('user_nam', 'password', 'name', date.datetime(1993, 1, 1), "0.0.0.1", 2)
        user.edit_personal_data('user_name', 'password', 'name', date.datetime(1993, 1, 1))
        self.assertEqual('user_name', user.user_name)
        self.assertEqual('password', user.password)
        self.assertEqual('name', user.name)
        self.assertEqual(date.datetime(1993, 1, 1), user.birth_date)

        # Testing wrong values
        self.assertRaises(TypeError, user.edit_personal_data, user_name='user', password='password', name='1234',
                          birth_date='1234')
        self.assertRaises(ValueError, user.edit_personal_data, user_name='', password='password', name='name',
                          birth_date=date.datetime(1993, 12, 1))
        self.assertRaises(ValueError, user.edit_personal_data, user_name='r', password='password', name='1234',
                          birth_date=date.datetime(1993, 12, 1))
        self.assertRaises(ValueError, user.edit_personal_data, user_name='us', password='password', name='1234',
                          birth_date=date.datetime(1993, 12, 1))
        self.assertRaises(ValueError, user.edit_personal_data, user_name='usd', password='password', name='j',
                          birth_date=date.datetime(1993, 12, 1))
        self.assertRaises(ValueError, user.edit_personal_data, user_name='usd', password='password', name='',
                          birth_date=date.datetime(1993, 12, 1))
        self.assertRaises(ValueError, user.edit_personal_data, user_name='us', password='password', name='dd',
                          birth_date=date.datetime(1993, 12, 1))
        self.assertRaises(ValueError, user.edit_personal_data, user_name='usd', password='', name='dd',
                          birth_date=date.datetime(1993, 12, 1))
        self.assertRaises(ValueError, user.edit_personal_data, user_name='usd', password='2', name='dd',
                          birth_date=date.datetime(1993, 12, 1))
        self.assertRaises(ValueError, user.edit_personal_data, user_name='us', password='22', name='dd',
                          birth_date=date.datetime(1993, 12, 1))

