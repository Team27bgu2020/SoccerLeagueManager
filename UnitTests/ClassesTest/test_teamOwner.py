from unittest import TestCase

from Domain.TeamOwner import TeamOwner
from Domain.Player import Player
from Domain.Coach import Coach


class TestTeamOwner(TestCase):
    team_owner = TeamOwner("Oscar")
    player = Player("striker")
    coach1 = Coach("1")
    coach2 = Coach("2")
    coach3 = Coach("3")

    """ This test check getter and setter"""

    def test_remove_role(self):
        self.team_owner = TeamOwner("Ben")
        self.team_owner.add_role(self.player)
        self.assertTrue(self.player in self.team_owner.roles)
        self.team_owner.remove_role(self.player)
        self.assertTrue(self.player not in self.team_owner.roles)
        self.assertRaises(ValueError,  self.team_owner.remove_role, self.coach3)

    def test_get_roles(self):
        self.team_owner.add_role(self.player)
        self.team_owner.add_role(self.coach1)
        self.assertTrue(self.player in self.team_owner.roles)
        self.assertTrue(self.coach1 in self.team_owner.roles)

    def test_add_role(self):
        self.team_owner = TeamOwner("tom")
        self.team_owner.add_role(self.player)
        self.team_owner.add_role(self.coach1)
        self.team_owner.add_role(self.coach2)
        self.assertTrue(self.player in self.team_owner.roles)
        self.assertTrue(self.coach2 in self.team_owner.roles)
        self.assertTrue(self.coach1 in self.team_owner.roles)
        self.assertTrue(3 == len(self.team_owner.roles))
        self.assertRaises(ValueError, self.team_owner.add_role, self.coach3)
