import hashlib
from unittest import TestCase
import datetime

from Domain.Fan import Fan
from Domain.Guest import Guest
from Domain.Referee import Referee
from Domain.SignedUser import SignedUser
from Enums.RefereeQualificationEnum import RefereeQualificationEnum
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
        signed_user_controller.add_system_admin("name_u0", "1234", "ro", d, "0.0.0.5")
        self.assertIsNotNone(signed_user_controller.get_signed_users().get("name_u0"))
        print("Done Successfully: test_add_system_admin")

    """ Received: user_name, password, name, birth_date """

    def test_add_signed_user(self):
        signed_user_controller = SignedUserController()
        signed_user_controller.add_guest("0.0.0.1")
        signed_user_controller.add_guest("0.0.0.1")
        d1 = datetime.datetime(2020, 4, 23)
        d2 = datetime.datetime(1998, 4, 23)
        signed_user_controller.add_signed_user("name_u1", "1234", "ro", d1, "0.0.0.5")
        signed_user_controller.add_signed_user("name_u2", "1234", "ro", d2, "0.0.0.6")
        self.assertIsNotNone(signed_user_controller.get_signed_users().get("name_u1").user_id)
        self.assertEqual(3, (signed_user_controller.get_guests().__len__()) + (
            signed_user_controller.get_signed_users().__len__()))
        print("Done Successfully: test_add_signed_user")

    """ Received: user_name, password, name, birth_date """

    def test_add_user(self):
        signed_user_controller = SignedUserController()
        d1 = datetime.datetime(2020, 4, 23)
        s_u = SignedUser("name_u1", "1234", "ro", d1, "0.0.0.5", 23)
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
        signed_user_controller.add_signed_user("name_u1", "1234", "ro", d1, "0.0.0.5")
        signed_user_controller.add_signed_user("name_u2", "1234", "ro", d2, "0.0.0.6")
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
        signed_user_controller.add_signed_user("name_u1", "1234", "ro", d1, "0.0.0.5")
        l1, l2 = signed_user_controller.show_all_users()
        self.assertEqual(3, l1.__len__() + l2.__len__())
        print("Done Successfully: test_show_all_users")

    """ Received: user_name, password """

    def test_confirm_user(self):
        signed_user_controller = SignedUserController()
        d1 = datetime.datetime(2020, 4, 23)
        signed_user_controller.add_system_admin("name_u1", "1234", "ro", d1, "0.0.0.5")
        self.assertEqual("SystemAdmin", signed_user_controller.confirm_user("name_u1", "1234"))
        self.assertFalse(signed_user_controller.confirm_user("name_u1", "12345"))
        self.assertFalse(signed_user_controller.confirm_user("name_u2", "1234"))
        print("Done Successfully: test_confirm_user")

    """ Received: user: SignedUser, new_name """

    def test_edit_personal_name(self):
        signed_user_controller = SignedUserController()
        d1 = datetime.datetime(2020, 4, 23)
        signed_user_controller.add_signed_user("name_u1", "1234", "ro", d1, "0.0.0.5")
        self.assertTrue(signed_user_controller.edit_personal_name("name_u1", "moshe"))
        self.assertNotEqual("ro", signed_user_controller.get_user("name_u1").name)
        self.assertEqual("moshe", signed_user_controller.get_user("name_u1").name)
        self.assertFalse(signed_user_controller.edit_personal_name("name21", "moshe"))
        print("Done Successfully: test_edit_personal_name")

    """ Received: user: SignedUser, birth_date """

    def test_edit_personal_birth_date(self):
        signed_user_controller = SignedUserController()
        d1 = datetime.datetime(2020, 4, 23)
        d2 = datetime.datetime(1998, 4, 23)
        signed_user_controller.add_signed_user("name_u1", "1234", "ro", d1, "0.0.0.5")
        self.assertTrue(signed_user_controller.edit_personal_birth_date("name_u1", d2))
        self.assertNotEqual(d1, signed_user_controller.get_user("name_u1").birth_date)
        self.assertEqual(d2, signed_user_controller.get_user("name_u1").birth_date)
        self.assertFalse(signed_user_controller.edit_personal_birth_date("name21", d1))
        print("Done Successfully: test_edit_personal_birth_date")

    """ Received: user name, old password, new password """

    def test_edit_personal_password(self):
        signed_user_controller = SignedUserController()
        d1 = datetime.datetime(2020, 4, 23)
        old_password = "1234"
        new_password = "1548"
        signed_user_controller.add_signed_user("name_u1", old_password, "ro", d1, "0.0.0.5")
        self.assertTrue(signed_user_controller.edit_personal_password("name_u1", old_password, new_password))
        self.assertNotEqual(str(hashlib.sha256(old_password.encode()).hexdigest()), signed_user_controller.get_user("name_u1").password)
        self.assertEqual(str(hashlib.sha256(new_password.encode()).hexdigest()), signed_user_controller.get_user("name_u1").password)
        self.assertFalse(signed_user_controller.edit_personal_password("name1", new_password, old_password))
        print("Done Successfully: test_edit_personal_password")

    """ Received: user_name, massage """

    def test_add_search(self):
        signed_user_controller = SignedUserController()
        d1 = datetime.datetime(2020, 4, 23)
        s = SignedUser("name_u1", "1234", "ro", d1, "0.0.0.5", 23)
        signed_user_controller.add_user(s)
        signed_user_controller.add_search(s.user_name, "first massage")
        signed_user_controller.add_search(s.user_name, "second massage")
        self.assertIsNotNone(signed_user_controller)
        print("Done Successfully: test_add_search")


    """ Received: user_name """

    def test_get_user(self):
        signed_user_controller = SignedUserController()
        d1 = datetime.datetime(2020, 4, 23)
        s = SignedUser("name_u1", "1234", "ro", d1, "0.0.0.5", 23)
        signed_user_controller.add_user(s)
        self.assertEqual(s, signed_user_controller.get_user(s.user_name))
        print("Done Successfully: test_get_user")

    def test_add_fan_to_data(self):
        signed_user_controller = SignedUserController()
        d1 = datetime.datetime(2020, 4, 23)
        signed_user_controller.add_fan_to_data("name_u1", "1234", "ro", d1, "0.0.0.5")
        self.assertTrue(signed_user_controller.get_user("name_u1"))
        self.assertTrue(type(signed_user_controller.get_user("name_u1")) is Fan)
        print("Done Successfully: test_add_fan_to_data")

    def test_add_referee_to_data(self):
        signed_user_controller = SignedUserController()
        d1 = datetime.datetime(2020, 4, 23)
        signed_user_controller.add_referee_to_data(RefereeQualificationEnum.MAIN, "name_u1", "1234", "ro", d1, "0.0.0.5")
        self.assertTrue(signed_user_controller.get_user("name_u1"))
        self.assertTrue(type(signed_user_controller.get_user("name_u1")) is Referee)
        print("Done Successfully: test_add_referee_to_data")

    def test_number_of_admins(self):
        signed_user_controller = SignedUserController()
        d1 = datetime.datetime(2020, 4, 23)
        d2 = datetime.datetime(2020, 4, 23)
        self.assertEqual(0, signed_user_controller.number_of_admins())
        signed_user_controller.add_system_admin("name_u1", "1234", "ro", d1, "0.0.0.5")
        signed_user_controller.add_system_admin("name_u21", "1234", "rso", d2, "0.0.0.2")
        signed_user_controller.add_fan_to_data("name_u2221", "12334", "rowe", d2, "0.0.0.1")
        self.assertEqual(2, signed_user_controller.number_of_admins())
        print("Done Successfully: test_add_referee_to_data")
