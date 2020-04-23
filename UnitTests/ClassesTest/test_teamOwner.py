from unittest import TestCase

from Domain.TeamOwner import TeamOwner
from Domain.Player import Player
from Domain.Coach import Coach


class TestTeamOwner(TestCase):
    team_owner = TeamOwner("Oscar")
    player = Player("striker")
    coach = Coach("1")
    """ This test check getter and setter"""

    def test_set_assigned_by(self):
        self.assertEqual(self.team_owner.get_assigned_by(), "Oscar")
        self.team_owner.set_assigned_by("Dor")
        self.assertEqual(self.team_owner.get_assigned_by(), "Dor")

    def test_get_roles(self):
        self.team_owner.add_role(self.player)
        self.team_owner.add_role(self.coach)
        self.assertEqual([self.player, self.coach], self.team_owner.get_roles())

    def test_add_role(self):
        self.team_owner.add_role(self.player)
        self.team_owner.add_role(self.coach)
        assert (self.player in self.team_owner.get_roles())
        assert (self.player in self.team_owner.get_roles())
        print(self.team_owner.get_roles())

    def test_remove_role(self):
        self.team_owner.add_role(self.player)
        assert (self.player in self.team_owner.get_roles())
        self.team_owner.remove_role(self.player)
        assert (self.player not in self.team_owner.get_roles())

