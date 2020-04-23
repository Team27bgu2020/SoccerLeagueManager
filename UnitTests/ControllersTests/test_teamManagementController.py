from unittest import TestCase

from Domain.Player import Player
from Domain.SignedUser import SignedUser
from Domain.Team import Team
import Domain.Team as TeamDomain
from Domain.TeamUser import TeamUser
from Service.TeamManagementController import TeamManagementController


class TestTeamManagementController(TestCase):
    control = TeamManagementController()
    barcelona = Team("Barca")
    # admin = SignedUser("", "", "", "")
    # u1 = TeamUser(barcelona, Player())
    # u2 = TeamUser(barcelona, Player())
    # u_l = [u1, u2]
    control.add_existing_team(barcelona)

    """ Testing getting team by name or id """

    def test_get_team(self):
        test_team = self.control.get_team("Barca")
        self.assertTrue(test_team.__eq__(self.barcelona))

    """ Testing adding a new team """

    def test_open_new_team(self):
        self.control.open_new_team("Real Madrid")
        self.assertTrue(self.control.get_team("Real Madrid").name == "Real Madrid")

    """ Testing closing and reopening of team"""

    def test_reopen_team(self):
        test_team = self.control.get_team("Barca")
        self.assertTrue(test_team.is_open)
        test_team.close_team()
        self.assertFalse(test_team.is_open)

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

    def test_set_stadium_to_team(self):
        self.control.set_stadium_to_team("Barca","Camp")
        # self.assertRaises(self.control.get_team_stadium("Barcelona"),"Camp")
        self.assertEqual(self.control.get_team_stadium("Barca"),"Camp")

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
