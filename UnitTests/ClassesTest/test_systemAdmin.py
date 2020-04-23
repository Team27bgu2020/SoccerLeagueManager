import datetime as date
from unittest import TestCase

from Domain.SystemAdmin import SystemAdmin
from Domain.SignedUser import SignedUser
from Domain.Team import Team

""" Idan """

class TestSystemAdmin(TestCase):

    teamA = Team("Arsenal")
    teamB = Team("Manchester United")
    user = SignedUser("userName", "password", "myName", date.datetime(2000, 1, 1), "0.0.0.1", 22)

    def setUp(self):
        user_name = 'default'
        password = 'default'
        name = 'default'
        birth_date = date.datetime(2000, 1, 1)
        self.SystemAdmin = SystemAdmin(user_name, password, name, birth_date, "0.0.0.2", 1)

    def tearDown(self):
        pass

    """ Testing the follow personal page method """

    def test_close_team(self):
        self.assertRaises(TypeError, self.SystemAdmin.close_team, self.user)
        self.SystemAdmin.close_team(self.teamA)
        self.assertFalse(self.teamA.is_open, False)
        self.SystemAdmin.close_team(self.teamB)
        self.assertRaises(ValueError, self.SystemAdmin.close_team, self.teamB)









