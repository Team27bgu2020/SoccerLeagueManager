from datetime import date
from unittest import TestCase

from DataBases.TeamDB import TeamDB
from Domain.Player import Player
from Domain.Team import Team
from Domain.TeamManager import TeamManager
from Domain.TeamOwner import TeamOwner
from Domain.TeamUser import TeamUser
import datetime as date
from Service.TeamManagementController import TeamManagementController

""" Those are both the test for manager and owner"""
""" The Manager will use the same functionality depended on the permission he has"""
""" The Functionality here is presented to all owners only , the team argument is automated from gui"""


class AcceptanceTestsOwnerManager(TestCase):

    def setUp(self):
        # Preparation
        self.team_db = TeamDB()
        self.control = TeamManagementController(self.team_db)
        self.barcelona = Team("Barca")
        self.manager = TeamUser('user_nam1', 'password', 'NameA', date.datetime(1993, 1, 1), 2, team=None,
                                role=None)
        self.manager_with_team = TeamUser('user_nam1', 'password', 'NameA', date.datetime(1993, 1, 1), 2,
                                          team=Team("ajax"), role=TeamManager())

        self.owner = TeamUser('user_nam2', 'password', 'NameB', date.datetime(1993, 1, 12), 3,
                              team=Team("ajax"),
                              role=TeamOwner())
        self.add_owner = TeamUser('user_nam2', 'password', 'NameB', date.datetime(1993, 1, 12), 3, team=None,
                                  role=TeamOwner())
        self.add_owner2 = TeamUser('user_nam2', 'password', 'NameB', date.datetime(1993, 1, 12), 3,
                                   team=None, role=TeamOwner())

        self.add_owner3 = TeamUser('user_nam2', 'password', 'NameB', date.datetime(1993, 1, 12), 3,
                                   team=Team("ajax"), role=TeamOwner())
        self.p1 = TeamUser('user_nam3', 'password', 'NameC', date.datetime(1993, 1, 12), 3, team=None,
                           role=Player())
        self.p2 = TeamUser('user_nam4', 'password', 'NameD', date.datetime(1993, 1, 12), 3, team=None,
                           role=Player())
        self.p3 = TeamUser('user_nam4', 'password', 'NameD', date.datetime(1993, 1, 12), 3,
                           team=Team("ajax"),
                           role=Player())
        self.budget = self.barcelona.budget_manager
        self.manager2 = TeamUser('user_nam5', 'password', 'NameD', date.datetime(1993, 1, 12), 3,
                                 Team("Macabi"),
                                 TeamManager())
        self.control.add_existing_team(self.barcelona)
        self.control.add_existing_team(Team("Bayer"))

    """ Testing adding a new team member,list of members
       and  deletion of list and one member"""

    # UC 6.1.1
    """Testing adding player info"""

    def test_add_team_member_to_team(self):
        # acceptance
        test_team = self.control.get_team("Barca", None)
        # add player
        self.control.add_team_member_to_team("Barca", self.p1)
        self.assertTrue(self.p1 in test_team.team_members)
        # Message presented

        # not acceptance
        # add player not correct input will be will be in the GUI
        # Message presented that values incorrect

        # not acceptance
        # adding team member already in a team
        self.assertRaises(ValueError, self.control.add_team_member_to_team, "Barca", self.p3)

    # UC 6.1.2
    """Testing edit player info"""

    def test_update_asset_acceptance(self):
        # acceptance
        # Owner chose update a coach or player:
        # The owner can update only attribute effected by the team
        # owner choose edit certain team member
        # Message presented are you sure
        # If agrees updates
        self.control.set_number_to_player(self.p1, "9")
        self.assertTrue(self.p1.role.number == "9")
        self.control.set_position_to_player(self.p1, "9")
        self.assertTrue(self.p1.role.position == "9")
        self.control.set_qualification_to_player(self.p1, "9")
        self.assertTrue(self.p1.role.qualification == "9")
        self.control.set_stadium_to_team("Barca", "Camp")
        self.assertTrue(self.control.get_team("Barca", None).stadium == "Camp")
        # Message presented

        # not acceptance
        # owner choose edit certain team member
        # Message presented are you sure
        # owner disagree nothing happened

    # UC 6.1.3
    """Testing remove asset """

    def test_remove_team_asset(self):
        # acceptance
        # add player
        self.control.add_team_member_to_team("Barca", self.p2)
        # preparation for UC
        self.assertTrue(self.p2 in self.control.get_team("Barca", None).team_members)
        # owner goes to remove member
        # Gui Ask if he is sure
        # owner agree ,remove player
        self.control.remove_team_member_from_team("Barca", self.p2)
        self.assertFalse(self.p2 in self.control.get_team("Barca", None).team_members)

        # not acceptance
        self.control.add_team_member_to_team("Barca", self.p2)
        # preparation for UC
        self.assertTrue(self.p2 in self.control.get_team("Barca", None).team_members)
        # owner goes to remove member
        # Gui Ask if he is sure
        # owner disagree
        self.assertTrue(self.p2 in self.control.get_team("Barca", None).team_members)
        # nothing happens

    # UC 6.2 add Set team additional owner
    def test_add_team_owner(self):
        # owner choose to add owner to the team
        # user accept
        self.control.add_owner_to_team("Barca", self.add_owner)
        # message presented by gui
        self.assertIsNotNone(self.control.get_team_owners("Barca"))
        # not acceptance
        # manager trying to set different team owner
        self.assertRaises(ValueError, self.control.add_owner_to_team, "Barca", self.add_owner3)
        # message presented

    # UC 6.3 remove additional owner
    def test_remove_owner_acceptance(self):
        # preparation for UC
        self.control.add_owner_to_team("Barca", self.add_owner)
        # owner choose team manager in the team
        # Gui ask if he is sure
        self.control.add_owner_to_team("Barca", self.add_owner2)
        self.control.remove_owner_from_team("Barca", self.add_owner)
        self.assertEqual(1, len(self.control.get_team_owners("Barca")))

    def test_remove_owner_not_acceptance(self):
        # Manager try to delete team without add owner
        self.control.add_owner_to_team("Barca", self.add_owner)
        self.assertRaises(ValueError, self.control.remove_owner_from_team, "Bayer", self.add_owner)
        # Get Gui message says there is no manager to delete

    # UC 6.4 add Set team Manager
    def test_add_team_manager_acceptance(self):
        # owner choose to add manager to the team
        # user accept
        self.control.add_manager_to_team("Barca", self.manager)
        # message presented by gui
        self.assertIsNotNone(self.control.get_team_managers("Barca"))

    def test_add_team_manager_not_acceptance(self):
        # owner choose to add manager already has a Manager /owner role in a team
        self.assertRaises(ValueError, self.control.add_manager_to_team, "Barca", self.manager_with_team)
        # The system dont allow to add the manager and present message

    # UC 6.5 remove Team manager
    def test_remove_team_manager_acceptance(self):
        # preparation for UC
        self.control.add_manager_to_team("Barca", self.manager)
        # owner choose team manager in the team
        # Gui ask if he is sure
        self.control.remove_manager_from_team("Barca", self.manager)
        self.assertEqual(0, len(self.control.get_team_managers("Barca")))

    def test_remove_team_manager_not_acceptance(self):
        # Manager try to delete team without manger
        self.assertRaises(ValueError, self.control.remove_manager_from_team, "Bayer", self.manager)
        # Get Gui message says there is no manager to delete

    # UC 6.6.1 Close Team
    def test_close_team_acceptance(self):
        # Owner chose close team
        test_team = self.control.get_team("Barca", None)
        self.assertTrue(test_team.is_open)
        # chose option to close
        # GUI ask if you sure
        self.control.close_team("Barca")
        self.assertFalse(test_team.is_open)
        # message presented
        # all the team get notify

    def test_close_team_not_acceptance(self):
        # Owner chose  close team
        test_team = self.control.get_team("Barca", None)
        self.assertTrue(test_team.is_open)
        # chose option to close
        # GUI ask if you sure
        # owner choose not to close
        # nothing happen

        # UC 6.6.1 Close Team

    def test_open_team_acceptance(self):
        # prepertion
        self.control.close_team("Barca")
        # Owner open  close team
        test_team = self.control.get_team("Barca", None)
        self.assertFalse(test_team.is_open)
        # chose option to open
        # GUI ask if you sure
        self.control.reopen_team("Barca")
        self.assertTrue(test_team.is_open)
        # message presented
        # all the team get notify

    def test_open_team_not_acceptance(self):
        # prepertion
        self.control.close_team("Barca")
        # Owner open  close team
        test_team = self.control.get_team("Barca", None)
        self.assertFalse(test_team.is_open)
        # chose option to open
        # GUI ask if you sure
        # owner choose not to open
        # nothing happen

    # UC 6.7.1 Add expanse
    def test_add_income_acceptance(self):
        # Owner chose add income
        # fill in correct input
        self.control.add_income_to_team("Barca", 500, "Sponsorship")
        self.assertTrue("+,500, Sponsorship" in self.control.get_team_incomes("Barca"))
        # Message presented by GUI

    def test_add_income_not_acceptance(self):
        # Owner chose add income
        # fill in incorrect input
        self.assertRaises(TypeError, self.control.add_income_to_team, "Barca", "9", "Sponsorship")
        # Message presented by GUI

    # UC 6.7.2 Add expanse
    def test_add_expanse_acceptance(self):
        # Owner chose add expanse
        # fill in incorrect input
        self.control.add_income_to_team("Barca", 500, "Sponsorship")
        self.control.add_expanse_to_team("Barca", 499, "Sponsorship")
        self.assertTrue("-,499, Sponsorship" in self.control.get_team_expanses("Barca"))
        # Message presented by GUI

    def test_add_expanse_not_acceptance(self):
        # Owner chose add expanse
        # fill in incorrect input
        self.assertRaises(TypeError, self.control.add_expanse_to_team, "Barca", "9", "Sponsorship")
        # Message presented by GUI
