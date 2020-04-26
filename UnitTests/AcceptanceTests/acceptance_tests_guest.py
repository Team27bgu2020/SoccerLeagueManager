from unittest import TestCase
from Service.SignedUserController import SignedUserController
from DataBases.UserDB import UserDB
from Service.PageController import PageController
from DataBases.PageDB import PageDB

import datetime as date


class AcceptanceTestsGuest(TestCase):
    # Preparation
    ip = '1.1.1.1'
    user_name = 'idan'
    password = '1234'
    name = 'idan'
    birth_date = date.datetime(1993, 1, 9)

    def setUp(self):
        self.db = UserDB()
        self.user_controller = SignedUserController(self.db)
        self.user_controller.add_signed_user(self.user_name, self.password, self.name, self.birth_date, self.ip)

        self.page_db = PageDB()
        self.page_controller = PageController(self.page_db)
        self.page_controller.add_page('ReuvenOved')

    # UC 2.2 acceptance tests
    def test_sign_me_up(self):
        # --- user with bad name want to sign up for the system ---
        bad_name = '10101'
        self.assertRaises(ValueError, self.user_controller.add_signed_user, self.user_name, self.password,
                          bad_name, self.birth_date, self.ip)

    # UC 2.3 acceptance tests
    def test_login(self):
        # user puts correct details of login
        self.assertTrue(self.user_controller.confirm_user('idan', '1234'))

        # user puts wrong password details of login
        self.assertFalse(self.user_controller.confirm_user('idan', '1010'))

        # user puts wrong username details of login
        self.assertFalse(self.user_controller.confirm_user('jack', '1234'))

    # UC 2.4 + UC 2.5 acceptance tests
    def test_search_page(self):
        # the user searched for Reuven Oved's page
        self.assertEqual(self.page_controller.search_personal_page('ReuvenOved'), self.page_db.show_personal_page('ReuvenOved'))

        # the user searched for Lady Gaga's page -> which doesnt exist
        self.assertRaises(ValueError, self.page_controller.search_personal_page, 'LadyGaga')
