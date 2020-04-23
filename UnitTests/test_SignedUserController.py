from unittest import TestCase
import datetime
from Domain.Guest import Guest
from Domain.SignedUser import SignedUser
from Service.SignedUserController import SignedUserController

""" Created By: Roman"""

class TestSignedUserController(TestCase):
    print("**Start testing**")

    """ Received: ip """

    def test_add_guest(self):
        signed_user_controller = SignedUserController()
        signed_user_controller.add_guest("0.0.0.1")
        signed_user_controller.add_guest("0.0.0.2")
        self.assertEqual(1, signed_user_controller.get_guests().get("0.0.0.1").user_id)
        self.assertEqual(2, signed_user_controller.get_guests().get("0.0.0.2").user_id)
        self.assertIsNone(signed_user_controller.get_guests().get("0.0.02"))

        print("Done Successfully: test_add_guest")

    """ Received: user_name, password, name, birth_date """

    def test_add_system_admin(self):
        """
        test if the admin in the DB
        If we ran all test its check that ID of the guest is not getting up when we got same guest
        @return:
        """
        signed_user_controller = SignedUserController()
        signed_user_controller.add_guest("0.0.0.1")
        d = datetime.datetime(2020, 4, 23)
        signed_user_controller.add_system_admin("name_u0", "1234", "ro", d)
        self.assertIsNotNone(signed_user_controller.get_signed_users().get("name_u0"))
        print("Done Successfully: test_add_system_admin")

    """ Received: user_name, password, name, birth_date """

    def test_add_signed_user(self):
        signed_user_controller = SignedUserController()
        signed_user_controller.add_guest("0.0.0.1")
        signed_user_controller.add_guest("0.0.0.1")
        d1 = datetime.datetime(2020, 4, 23)
        d2 = datetime.datetime(1998, 4, 23)
        signed_user_controller.add_signed_user("name_u1", "1234", "ro", d1)
        signed_user_controller.add_signed_user("name_u2", "1234", "ro", d2)
        self.assertIsNotNone(signed_user_controller.get_signed_users().get("name_u1").user_id)
        self.assertEqual(3, (signed_user_controller.get_guests().__len__()) + (
            signed_user_controller.get_signed_users().__len__()))
        print("Done Successfully: test_add_signed_user")

    """ Received: user_name, password, name, birth_date """

    def test_add_user(self):
        signed_user_controller = SignedUserController()
        d1 = datetime.datetime(2020, 4, 23)
        s_u = SignedUser("name_u1", "1234", "ro", d1)
        g = Guest("0.0.0.1", 23)
        signed_user_controller.add_user(s_u)
        signed_user_controller.add_user(g)
        self.assertEqual(2, (signed_user_controller.get_guests().__len__()) + (
            signed_user_controller.get_signed_users().__len__()))
        self.assertIsNotNone(signed_user_controller.get_signed_users().get("name_u1"))
        self.assertIsNotNone(signed_user_controller.get_guests().get("0.0.0.1"))
        self.assertIsNone(signed_user_controller.get_signed_users().get("0.0.0.1"))
        print("Done Successfully: test_add_user")

    """ Received: user_name """

    def test_delete_signed_user(self):
        signed_user_controller = SignedUserController()
        d1 = datetime.datetime(2020, 4, 23)
        d2 = datetime.datetime(1998, 4, 23)
        signed_user_controller.add_signed_user("name_u1", "1234", "ro", d1)
        signed_user_controller.add_signed_user("name_u2", "1234", "ro", d2)
        signed_user_controller.delete_signed_user("name_u1")
        signed_user_controller.delete_signed_user("name_u12")
        self.assertEqual(1, signed_user_controller.get_signed_users().__len__())
        self.assertIsNone(signed_user_controller.get_signed_users().get("name_u1"))
        print("Done Successfully: test_delete_signed_user")

    """ Received: ip """

    def test_delete_guest(self):
        signed_user_controller = SignedUserController()
        g1 = Guest("0.0.0.1", 23)
        g2 = Guest("0.0.0.2", 46)
        signed_user_controller.add_user(g1)
        signed_user_controller.add_user(g2)
        signed_user_controller.delete_guest(g1.user_ip)
        """ Cannot be deleted """
        signed_user_controller.delete_guest("0.020.1")
        self.assertEqual(1, signed_user_controller.get_guests().__len__())
        self.assertIsNone(signed_user_controller.get_guests().get("0.0.0.1"))
        print("Done Successfully: test_delete_guest")

    """ Received: user: SignedUser, new_name """

    def test_show_all_users(self):
        signed_user_controller = SignedUserController()
        signed_user_controller.add_guest("0.0.0.1")
        signed_user_controller.add_guest("0.0.0.3")
        signed_user_controller.add_guest("0.0.0.3")
        d1 = datetime.datetime(2020, 4, 23)
        signed_user_controller.add_signed_user("name_u1", "1234", "ro", d1)
        l1, l2 = signed_user_controller.show_all_users()
        self.assertEqual(3, l1.__len__() + l2.__len__())
        print("Done Successfully: test_show_all_users")

    """ Received: user_name, password """

    def test_confirm_user(self):
        pass

    """ Received: user: SignedUser, new_name """

    def test_edit_personal_name(self):
        pass

    """ Received: user: SignedUser, birth_date """

    def test_edit_personal_birth_date(self):
        pass

    """ Received: user name, old password, new password """

    def test_edit_personal_password(self):
        pass

    """ Received: user_name, massage """

    def test_add_search(self):
        pass

    """ Received: user_name """

    def test_get_user(self):
        signed_user_controller = SignedUserController()
        d1 = datetime.datetime(2020, 4, 23)
        s = SignedUser("name_u1", "1234", "ro", d1)
        signed_user_controller.add_user(s)
        self.assertEqual(s, signed_user_controller.get_user(s.user_name))
        print("Done Successfully: test_get_user")