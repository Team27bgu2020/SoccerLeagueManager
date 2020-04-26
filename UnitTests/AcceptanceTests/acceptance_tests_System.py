from datetime import datetime
from unittest import TestCase

from Domain.SystemAdmin import SystemAdmin
from Domain.TeamUser import TeamUser
from System import System


class AcceptanceTestReferee(TestCase):

    def setUp(self):
        self.system = System('user_name', 'password', 'name', datetime(1993, 1, 1), '1.1.1.1')

    def test_system_reboot(self):

        # Test if the system is rebooted with system
        self.assertEqual(len(self.system.user_controller.get_signed_users()), 1)
        self.assertIsInstance(self.system.user_controller.get_user('user_name'), SystemAdmin)


