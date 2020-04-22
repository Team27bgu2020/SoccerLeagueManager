from unittest import TestCase

from Domain.Team import Team
import Domain.Team as TeamDomain
from Service.TeamManagementController import TeamManagementController


class TestTeamManagementController(TestCase):

    control = TeamManagementController()
    barcelona = Team("Barca","Campnou")

    def test_get_team(self):
        self.control

    def test_open_new_team(self):
        self.fail()

    def test_reopen_team(self):
        self.fail()

    def test_close_team(self):
        self.fail()

    def test_add_team_member_to_team(self):
        self.fail()

    def test_add_list_team_members_to_team(self):
        self.fail()

    def test_delete_team_member_from_team(self):
        self.fail()

    def test_delete_list_team_members_to_team(self):
        self.fail()

    def test_get_team_manager(self):
        self.fail()

    def test_get_team_owner(self):
        self.fail()

    def test_set_owner_to_team(self):
        self.fail()

    def test_remove_owner_to_team(self):
        self.fail()

    def test_set_manager_to_team(self):
        self.fail()

    def test_remove_manager_to_team(self):
        self.fail()

    def test_set_field_to_team(self):
        self.fail()

    def test_get_team_incomes(self):
        self.fail()

    def test_get_team_expanses(self):
        self.fail()

    def test_get_team_transactions(self):
        self.fail()

    def test_get_team_current(self):
        self.fail()

    def test_add_income_to_team(self):
        self.fail()

    def test_add_expanse_to_team(self):
        self.fail()
