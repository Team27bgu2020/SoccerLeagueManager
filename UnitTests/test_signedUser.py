from unittest import TestCase
from Domain.SignedUser import *


class TestSignedUser(TestCase):
    def test_edit_personal_data(self):

        # Testing all valid inputs
        user = SignedUser()
        user.edit_personal_data('user_name', 'password', 'name', date.datetime(1993, 1, 1))
        self.assertEqual('user_name', user._SignedUser__user_name)
        self.assertEqual('password', user._SignedUser__password)
        self.assertEqual('name', user._SignedUser__name)
        self.assertEqual(date.datetime(1993, 1, 1), user._SignedUser__birth_date)

        # Testing wrong values
        self.assertRaises(ValueError, user.edit_personal_data, user_name='user', password='password', name='1234',
                          birth_date=date.datetime(1993, 1, 1))
        self.assertRaises(TypeError, user.edit_personal_data, user_name='user', password='password', name='name',
                          birth_date='1234')
