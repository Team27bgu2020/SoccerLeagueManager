from datetime import date
from unittest import TestCase

from DataBases.MongoDB.MongoTeamDB import MongoTeamDB
from DataBases.MongoDB.MongoUsersDB import MongoUserDB
from Domain.Player import Player
from Domain.Team import Team
from Domain.TeamManager import TeamManager
from Domain.TeamOwner import TeamOwner
from Domain.TeamUser import TeamUser
import datetime as date
from Service.TeamManagementController import TeamManagementController
from Service.SignedUserController import SignedUserController

""" Those are both the test for manager and owner"""
""" The Manager will use the same functionality depended on the permission he has"""
""" The Functionality here is presented to all owners only , the team argument is automated from gui"""


class AcceptanceTestsOwnerManager(TestCase):

    def setUp(self):
        # Preparation
        self.team_db = MongoTeamDB()
        self.user_db = MongoUserDB()
        self.team_control = TeamManagementController(self.team_db, self.user_db)
        self.user_controller = SignedUserController(self.user_db)

        self.user_controller.add_team_owner('user_nam2', 'password', 'NameB', date.datetime(1993, 1, 12))
        self.owner = self.user_controller.get_user_by_name('user_nam2')
        self.user_controller.add_team_owner('user_nam3', 'password', 'NameC', date.datetime(1993, 1, 12))
        self.add_owner = self.user_controller.get_user_by_name('user_nam3')
        self.user_controller.add_team_owner('owner_with_team', 'password', 'owner', date.datetime(1993, 1, 1))
        self.owner_with_team = self.user_controller.get_user_by_name('owner_with_team')

        self.user_controller.add_team_manager('user_nam1', 'password', 'nameA', date.datetime(1993, 1, 1))
        self.manager = self.user_controller.get_user_by_name('user_nam1')
        self.user_controller.add_team_manager('manager_with_team', 'password', 'manager', date.datetime(1993, 1, 1))
        self.manager_with_team = self.user_controller.get_user_by_name('manager_with_team')

        self.user_controller.add_player('user_nam4', 'password', 'NameD', date.datetime(1993, 1, 12))
        self.p1 = self.user_controller.get_user_by_name('user_nam4')
        self.user_controller.add_player('user_nam5', 'password', 'NameE', date.datetime(1993, 1, 12))
        self.p2 = self.user_controller.get_user_by_name('user_nam5')

        self.team_control.open_new_team("Barca", self.owner.user_id)
        self.team_control.open_new_team("ajax", self.owner_with_team.user_id)

        self.team_control.add_manager_to_team('ajax', self.manager_with_team.user_id)

    def tearDown(self):

        self.team_control.delete_team('Barca')
        self.team_control.delete_team('ajax')

        self.user_controller.delete_signed_user(self.owner.user_id)
        self.user_controller.delete_signed_user(self.add_owner.user_id)
        self.user_controller.delete_signed_user(self.owner_with_team.user_id)

        self.user_controller.delete_signed_user(self.manager.user_id)
        self.user_controller.delete_signed_user(self.manager_with_team.user_id)

        self.user_controller.delete_signed_user(self.p1.user_id)
        self.user_controller.delete_signed_user(self.p2.user_id)

    """ Testing adding a new team member,list of members
       and  deletion of list and one member"""

    # UC 6.1.1
    """Testing adding player info"""

    def test_add_team_member_to_team(self):
        # acceptance
        test_team = self.team_control.get_team('Barca')
        # add player
        self.team_control.add_team_member_to_team("Barca", self.p1.user_id)
        test_team = self.team_control.get_team('Barca')
        self.assertTrue(self.p1.user_id in test_team.team_members)
        # Message presented

        # not acceptance
        # add player not correct input will be will be in the GUI
        # Message presented that values incorrect

        # not acceptance
        # adding team member already in a team
        self.assertRaises(ValueError, self.team_control.add_team_member_to_team, "Barca", self.p1.user_id)

    # UC 6.1.2
    """Testing edit player info"""

    def test_update_asset_acceptance(self):
        # acceptance
        # Owner chose update a coach or player:
        # The owner can update only attribute effected by the team
        # owner choose edit certain team member
        # Message presented are you sure
        # If agrees updates
        self.team_control.set_number_to_player(self.p1.user_id, "9")
        self.p1 = self.user_controller.get_user_by_id(self.p1.user_id)
        self.assertTrue(self.p1.role.number == "9")
        self.team_control.set_position_to_player(self.p1.user_id, "9")
        self.p1 = self.user_controller.get_user_by_id(self.p1.user_id)
        self.assertTrue(self.p1.role.position == "9")

        self.team_control.set_stadium_to_team("Barca", "Camp")
        self.assertTrue(self.team_control.get_team("Barca").stadium == "Camp")
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
        self.team_control.add_team_member_to_team("Barca", self.p2.user_id)
        # preparation for UC
        self.assertTrue(self.p2.user_id in self.team_control.get_team("Barca").team_members)
        # owner goes to remove member
        # Gui Ask if he is sure
        # owner agree ,remove player
        self.team_control.remove_team_member_from_team("Barca", self.p2.user_id)
        self.assertFalse(self.p2.user_id in self.team_control.get_team("Barca").team_members)

        # not acceptance
        self.team_control.add_team_member_to_team("Barca", self.p2.user_id)
        # preparation for UC
        self.assertTrue(self.p2.user_id in self.team_control.get_team("Barca").team_members)
        # owner goes to remove member
        # Gui Ask if he is sure
        # owner disagree
        self.assertTrue(self.p2.user_id in self.team_control.get_team("Barca").team_members)
        # nothing happens

    # UC 6.2 add Set team additional owner
    def test_add_team_owner(self):
        self.assertEqual(1, len(self.team_control.get_team_owners('Barca')))
        # owner choose to add owner to the team
        # user accept
        self.team_control.add_owner_to_team("Barca", self.add_owner.user_id)
        # message presented by gui
        self.assertEqual(2, len(self.team_control.get_team_owners('Barca')))
        # not acceptance
        # manager trying to add owner that already in a team
        self.assertRaises(ValueError, self.team_control.add_owner_to_team, "Barca", self.owner_with_team.user_id)
        # message presented

    # UC 6.3 remove additional owner
    def test_remove_owner_acceptance(self):
        # preparation for UC
        self.team_control.add_owner_to_team("Barca", self.add_owner.user_id)
        # owner choose team manager in the team
        # Gui ask if he is sure
        self.team_control.remove_owner_from_team("Barca", self.add_owner.user_id)
        self.assertEqual(1, len(self.team_control.get_team_owners("Barca")))

    def test_remove_owner_not_acceptance(self):
        # Manager try to delete team without add owner
        self.assertRaises(Exception, self.team_control.remove_owner_from_team, "Barca", self.owner.user_id)
        # Get Gui message says there is no manager to delete

    # UC 6.4 add Set team Manager
    def test_add_team_manager_acceptance(self):
        # owner choose to add manager to the team
        # user accept
        self.team_control.add_manager_to_team("Barca", self.manager.user_id)
        # message presented by gui
        self.assertEqual(1, len(self.team_control.get_team_managers('Barca')))

    def test_add_team_manager_not_acceptance(self):
        # owner choose to add manager already has a Manager /owner role in a team
        self.assertRaises(ValueError, self.team_control.add_manager_to_team, "Barca", self.manager_with_team.user_id)
        # The system dont allow to add the manager and present message

    # UC 6.5 remove Team manager
    def test_remove_team_manager_acceptance(self):
        # preparation for UC
        self.team_control.add_manager_to_team("Barca", self.manager.user_id)
        # owner choose team manager in the team
        # Gui ask if he is sure
        self.team_control.remove_manager_from_team("Barca", self.manager.user_id)
        self.assertEqual(0, len(self.team_control.get_team_managers("Barca")))

    def test_remove_team_manager_not_acceptance(self):
        # Manager try to delete team without manger
        self.assertRaises(ValueError, self.team_control.remove_manager_from_team, "Barca", self.manager.user_id)
        # Get Gui message says there is no manager to delete

    # UC 6.6.1 Close Team
    def test_close_team_acceptance(self):
        # Owner chose close team
        test_team = self.team_control.get_team("Barca")
        self.assertTrue(test_team.is_open)
        # chose option to close
        # GUI ask if you sure
        self.team_control.close_team("Barca")
        test_team = self.team_control.get_team("Barca")
        self.assertFalse(test_team.is_open)
        # message presented
        # all the team get notify

    def test_close_team_not_acceptance(self):
        # Owner chose  close team
        test_team = self.team_control.get_team("Barca")
        self.assertTrue(test_team.is_open)
        # chose option to close
        # GUI ask if you sure
        # owner choose not to close
        # nothing happen

        # UC 6.6.1 Close Team

    def test_open_team_acceptance(self):
        # prepertion
        self.team_control.close_team("Barca")
        # Owner open  close team
        test_team = self.team_control.get_team("Barca")
        self.assertFalse(test_team.is_open)
        # chose option to open
        # GUI ask if you sure
        self.team_control.reopen_team("Barca")
        test_team = self.team_control.get_team("Barca")
        self.assertTrue(test_team.is_open)
        # message presented
        # all the team get notify

    def test_open_team_not_acceptance(self):
        # prepertion
        self.team_control.close_team("Barca")
        # Owner open  close team
        test_team = self.team_control.get_team("Barca")
        self.assertFalse(test_team.is_open)
        # chose option to open
        # GUI ask if you sure
        # owner choose not to open
        # nothing happen

    # UC 6.7.1 Add expanse
    def test_add_income_acceptance(self):
        # Owner chose add income
        # fill in correct input
        self.team_control.add_income_to_team("Barca", 500, "Sponsorship")
        self.assertTrue("+,500, Sponsorship" in self.team_control.get_team_incomes("Barca"))
        # Message presented by GUI

    def test_add_income_not_acceptance(self):
        # Owner chose add income
        # fill in incorrect input
        self.assertRaises(ValueError, self.team_control.add_income_to_team, "Barca", -500, "Sponsorship")
        # Message presented by GUI

    # UC 6.7.2 Add expanse
    def test_add_expanse_acceptance(self):
        # Owner chose add expanse
        # fill in incorrect input
        self.team_control.add_income_to_team("Barca", 500, "Sponsorship")
        self.team_control.add_expanse_to_team("Barca", 499, "Sponsorship")
        self.assertTrue("-,499, Sponsorship" in self.team_control.get_team_expanses("Barca"))
        # Message presented by GUI

    def test_add_expanse_not_acceptance(self):
        # Owner chose add expanse
        # fill in incorrect input
        self.assertRaises(ValueError, self.team_control.add_expanse_to_team, "Barca", -500, "Sponsorship")
        # Message presented by GUI
