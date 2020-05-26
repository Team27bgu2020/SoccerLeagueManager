from unittest import TestCase

from Domain.TeamOwner import TeamOwner
from Domain.TeamManager import TeamManager


class TestTeamManager(TestCase):
    team_owner = TeamOwner("Oscar")
    team_manger = TeamManager(team_owner)

    def test_set_assigned_by(self):
        self.team_manger.approve_all()
        self.assertTrue(self.team_manger.approval_open_close is True)
        self.assertTrue(self.team_manger.approval_accounting is True)
        self.assertTrue(self.team_manger.approval_add_remove is True)
        self.assertTrue(self.team_manger.approval_set_permission is True)

        self.team_manger.set_approval_add_remove(False)
        self.assertTrue(self.team_manger.approval_add_remove is False)
        self.assertTrue(self.team_manger.approval_open_close is True)
        self.assertTrue(self.team_manger.approval_accounting is True)
        self.assertTrue(self.team_manger.approval_set_permission is True)
