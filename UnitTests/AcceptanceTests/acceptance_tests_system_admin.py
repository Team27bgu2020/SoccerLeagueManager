from unittest import TestCase

from DataBases.TeamDB import TeamDB
from Domain.TeamUser import TeamUser
from Domain.TeamOwner import TeamOwner
from Service.SignedUserController import SignedUserController
from Service.ComplaintController import ComplaintController
from DataBases.MongoDB.MongoUsersDB import MongoUserDB
from DataBases.ComplaintDB import ComplaintDB
from Domain.SystemAdmin import SystemAdmin
from Domain.Team import Team
from Domain.Fan import Fan
import datetime as date

from Service.TeamManagementController import TeamManagementController


class AcceptanceTestsSystemAdmin(TestCase):
    # Preparation
    fan = Fan('fan', '1234', 'name', date.datetime(1993, 1, 9), 2)
    system_admin = SystemAdmin('boss', '1234', 'name', date.datetime(1993, 1, 9), 1)
    team1 = Team("Beer Sheva", [])
    answer = 'complaint ans'

    def setUp(self):
        self.user_db = MongoUserDB()
        self.team_db = TeamDB()
        self.user_controller = SignedUserController(self.user_db)
        self.team_owner = TeamUser('user_name', 'password', 'name', date.datetime(1980, 5, 5), 3,
                                   TeamOwner())

        self.complaint_db = ComplaintDB()
        self.complaint_controller = ComplaintController(self.complaint_db)
        self.complaint_controller.new_complaint('first comp', self.fan)

        self.team_controller = TeamManagementController(self.team_db)

    # UC 1.1
    def test_init_system(self):
        """we init the DataBase in set up function ^ """
        d2 = date.datetime(1998, 4, 23)
        self.user_controller.add_system_admin("admin", "1234", "ro", d2)
        admin = self.user_controller.get_user_by_name('admin')
        self.assertTrue(self.user_controller.confirm_user('admin', '1234'))
        self.assertRaises(AssertionError, self.user_controller.delete_signed_user, admin.user_id)

    def test_init_system_no_acceptance(self):
        """we init the DataBase in set up function ^ """
        d2 = date.datetime(1998, 4, 23)
        self.assertRaises(ValueError, self.user_controller.add_system_admin, "", "1234", "ro", d2)

    # UC 8.1
    def test_close_team(self):
        self.team_controller.open_new_team("Tiberias", self.team_owner)
        """admin is connected and chose what team he wants to close"""
        all_teams = self.team_controller.dictionary_team
        """admin see only the team that in the system"""
        """if admin want to exit he press on exit and stop here"""
        self.team_controller.close_team("Tiberias")
        self.assertFalse(self.team_controller.get_team("Tiberias", None).is_open)

    #UC 8.2
    def test_remove_signed_user(self):
        """ Admin in connected and want to close team """
        d1 = date.datetime(2020, 4, 23)
        d2 = date.datetime(1998, 4, 23)
        self.user_controller.add_system_admin("name_u1", "1234", "ro", d1)
        self.user_controller.add_system_admin("admin", "1234", "ro", d2)
        admin = self.user_controller.get_user_by_name('name_u1')
        self.assertTrue(self.user_controller.delete_signed_user(admin.user_id))
        admin = self.user_controller.get_user_by_name('admin')

    # UC 8.3
    def test_show_complaint_and_respond(self):
        # admin wants to see all user complaints
        complaints = self.complaint_controller.show_complaints()
        com = self.complaint_db.show_complaints()
        self.assertEqual(com, complaints.show_complaints())
        # admin chooses a complaint to answer on
        complaint = complaints.get_complaints(self.fan, 1)
        # admin tries to respond to the complaint but doesnt write anything
        self.assertRaises(TypeError, self.complaint_controller.respond_to_complaint, None, complaint.complainer, complaint.complaint_id)
        # admin responds to the complaint as he should
        self.complaint_controller.respond_to_complaint(self.answer, complaint.complainer, complaint.complaint_id)
        self.assertEqual(complaint.answer, self.answer)
