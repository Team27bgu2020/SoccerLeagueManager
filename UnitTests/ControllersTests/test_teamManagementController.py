from unittest import TestCase

from Domain.Player import Player
from Domain.SignedUser import SignedUser
from Domain.Team import Team
import Domain.Team as TeamDomain
from Domain.TeamManager import TeamManager
from Domain.TeamOwner import TeamOwner
from Domain.TeamUser import TeamUser
from Service.TeamManagementController import TeamManagementController


class TestTeamManagementController(TestCase):
    control = TeamManagementController()
    barcelona = Team("Barca")
    manager = TeamUser(barcelona, TeamManager())
    owner = TeamUser(barcelona, TeamOwner())
    p1 = TeamUser(barcelona, Player())
    p2 = TeamUser(barcelona, Player())

    budget = barcelona.budget_manager

    """ Testing getting team by name or id """

    def test_get_team(self):
        self.control.add_existing_team(self.barcelona)
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
        self.control.close_team("Barca")
        self.assertFalse(test_team.is_open)
        self.control.reopen_team("Barca")
        self.assertTrue(test_team.is_open)


    """ Testing adding a new team member,list of members
     and  deletion of list and one member"""

    def test_add_team_member_to_team(self):
        self.control.add_existing_team(self.barcelona)
        test_team = self.control.get_team("Barca")
        # add player
        self.control.add_team_member_to_team("Barca", self.p1)
        self.assertTrue(self.p1 in test_team.team_members)
        # remove player
        self.control.remove_team_member_from_team("Barca", self.p1)
        self.assertFalse(self.p1 in test_team.team_members)

        # add players
        self.control.add_team_members_to_team("Barca", [self.p1, self.p2])
        self.assertTrue(self.p1 in test_team.team_members)
        # remove players
        self.control.remove_team_members_from_team("Barca", [self.p1, self.p2])
        self.assertFalse(self.p1 in test_team.team_members)

    """ Testing get,set and remove team manager"""

    def test_get_set_remove_team_manager(self):
        # get
        self.barcelona.manager = self.manager
        self.control.add_existing_team(self.barcelona)
        ret_manager = self.control.get_team_manager("Barca")
        self.assertEqual(ret_manager, self.manager)

        # remove
        self.control.remove_manager_from_team("Barca")
        self.assertIsNone(self.control.get_team_manager("Barca"))

        # set
        self.control.set_manager_to_team("Barca", self.manager)
        ret_manager = self.control.get_team_manager("Barca")
        self.assertEqual(ret_manager, self.manager)

    """ Testing get,set and remove team owner"""

    def test_get_set_remove_team_owner(self):
        # get
        self.barcelona.owner = self.owner
        self.control.add_existing_team(self.barcelona)
        ret_owner = self.control.get_team_owner("Barca")
        self.assertEqual(ret_owner, self.owner)

        # remove
        self.control.remove_owner_from_team("Barca")
        self.assertIsNone(self.control.get_team_owner("Barca"))

        # set
        self.control.set_owner_to_team("Barca", self.owner)
        ret_owner = self.control.get_team_owner("Barca")
        self.assertEqual(ret_owner, self.owner)

    """ Testing get_set to stadium of certain team"""

    def test_set_stadium_to_team(self):
        self.control.add_existing_team(self.barcelona)
        self.control.set_stadium_to_team("Barca", "Camp")
        # self.assertIsNone(self.control.get_team_stadium("Barcelona"),"Camp")
        self.assertEqual(self.control.get_team_stadium("Barca"), "Camp")

    """ Testing the team budget component"""

    def test_team__budget(self):
        self.control.add_existing_team(self.barcelona)
        self.control.add_expanse_to_team("Barca", 500, "Arnona")
        self.assertTrue("-,500, Arnona" in self.control.get_team_expanses("Barca"))
        self.control.add_income_to_team("Barca", 500, "Sponsorship")
        self.assertTrue("+,500, Sponsorship" in self.control.get_team_incomes("Barca"))
        self.assertTrue("+,500, Sponsorship" in self.control.get_team_transactions("Barca"))
        self.assertTrue("-,500, Arnona" in self.control.get_team_transactions("Barca"))
        self.assertEqual(self.control.get_team_budget("Barca"), 0)

