from unittest import TestCase

from Domain.TeamOwner import TeamOwner
from Domain.TeamManager import TeamManager


class TestTeamManager(TestCase):
    team_owner = TeamOwner("Oscar")
    team_manger = TeamManager(team_owner)

    def test_set_assigned_by(self):
        team_owner_b = TeamOwner("Beta")
        self.team_manger.set_assigned_by(team_owner_b)
        self.assertEqual(self.team_manger.get_assigned_by(),team_owner_b)

        team_manger = TeamManager(team_owner_b)
        self.assertRaises(self.team_manger.set_assigned_by(team_manger))

    # def test_get_assigned_by(self):
    #     self.assertEqual(self.team_manger.get_assigned_by(),self.team_owner)
    #
    # def test_approve_all(self):
    #     self.assertEqual(self.team_manger.get)
    #
    #
    #
    #
    #
    #
    #
    # def test_to_string(self):
    #     self.fail()
