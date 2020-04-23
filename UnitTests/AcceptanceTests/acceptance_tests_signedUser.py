from unittest import TestCase
import datetime as date
from Service.SignedUserController import SignedUserController


class AcceptanceTestsSignedUser(TestCase):

    # Preparation
    controller = SignedUserController()

    # UC 4.1, UC 5.1, UC 10.1 acceptance tests
    # Personal details update received from user GUI
    def update_personal_info(self):
        user_name = 'userName'
        password = 'password'

        AcceptanceTestsSignedUser.controller.add_signed_user(user_name, password, 'name', date.datetime(2000, 1, 1))

        # valid details
        valid_name = 'Shahar'
        valid_birth_date = date.datetime(1993, 1, 1)

        # Invalid details
        invalid_name = '123'
        invalid_birth_date = date.datetime(2100, 1, 1)

        # GUI calls to this method in service layer