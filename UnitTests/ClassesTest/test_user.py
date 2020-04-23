from unittest import TestCase
from Domain.User import User


class TestUser(TestCase):

    def __init__(self):
        self.user = User()

    # Test set_ip_address
    def test_set_ip_address(self):

        valid_ip = '1.1.1.1'
        invalid_ip = "a.1.2.3.4.5"

        # Test valid input
        self.user.set_ip_address(valid_ip)
        self.assertEqual(valid_ip, self.user._User__ip_address)

        # Test invalid input
        self.assertRaises(ValueError, self.user.set_ip_address, invalid_ip)

    # Test set_ip_address
    def test_set_user_id(self):

        valid_user_id = 5
        invalid_user_id = 'b'
        invalid_user_id2 = -3

        # Test valid input
        self.user.set_user_id(valid_user_id)
        self.assertEqual(valid_user_id, self.user._User__ip_address)

        # Test invalid input
        self.assertRaises(ValueError, self.user.set_ip_address, invalid_user_id)
        self.assertRaises(ValueError, self.user.set_ip_address, invalid_user_id2)
