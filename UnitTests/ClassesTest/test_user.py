from unittest import TestCase
from Domain.User import User


class TestUser(TestCase):

    # Test set_ip_address
    def test_set_ip_address(self):
        u = User("0.0.0.0", 23)
        valid_ip = '1.1.1.1'
        invalid_ip = "a.1.2.3.4.5"

        # Test valid input
        u.set_ip_address(valid_ip)
        self.assertEqual(valid_ip, u.user_ip)
        # Test invalid input
        self.assertRaises(ValueError, u.set_ip_address, invalid_ip)


    # Test set_ip_address
    def test_set_user_id(self):
        u = User("0.0.0.0", 23)
        valid_user_id = 5
        invalid_user_id = 'b'
        invalid_user_id2 = -3

        # Test valid input
        u.set_user_id(valid_user_id)
        self.assertEqual(valid_user_id, u.user_id)

        # Test invalid input
        self.assertRaises(ValueError, u.set_user_id, invalid_user_id)
        self.assertRaises(ValueError, u.set_user_id, invalid_user_id2)
