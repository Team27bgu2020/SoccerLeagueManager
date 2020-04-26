from unittest import TestCase
import datetime as date

from DataBases.UserDB import UserDB
from Service.SignedUserController import SignedUserController


class AcceptanceTestsSignedUser(TestCase):

    # Preparation
    user_db = UserDB()
    controller = SignedUserController(user_db)

    # UC 4.1, UC 5.1, UC 10.1 acceptance tests
    # Personal details update received from user GUI
    def test_update_personal_info(self):
        ip_address = '1.1.1.1'
        user_name = 'userName'
        password = 'password'

        self.controller.add_signed_user(user_name, password, 'name', date.datetime(2000, 1, 1), ip_address)
        user = self.controller.get_user(user_name)

        # valid details
        valid_name = 'Shahar'
        valid_birth_date = date.datetime(1993, 1, 1)

        # Invalid details
        invalid_name = '123'
        invalid_birth_date = date.datetime(2100, 1, 1)

        # --- Testing valid input data ---
        # GUI calls to this method in service layer
        self.controller.edit_personal_data(user, user_name, password, valid_name, valid_birth_date)
        self.assertEqual(self.controller.get_user(user_name).name, valid_name)
        self.assertEqual(self.controller.get_user(user_name).birth_date, valid_birth_date)

        # --- Testing invalid input data
        self.assertRaises(ValueError, self.controller.edit_personal_data, user, user_name, password, invalid_name, invalid_birth_date)
