from unittest import TestCase

from DataBases.MongoDB.MongoTeamDB import MongoTeamDB
from Domain.TeamUser import TeamUser
from Domain.TeamOwner import TeamOwner
from Service.SignedUserController import SignedUserController
from Service.ComplaintController import ComplaintController
from DataBases.MongoDB.MongoUsersDB import MongoUserDB
from DataBases.MongoDB.MongoComplaintDB import MongoComplaintDB
from Domain.SystemAdmin import SystemAdmin
from Domain.Team import Team
from Domain.Fan import Fan
import datetime as date

from Service.TeamManagementController import TeamManagementController


class AcceptanceTestsSystemAdmin(TestCase):
    # Preparation
    user_db = MongoUserDB()
    team_db = MongoTeamDB()
    complaint_db = MongoComplaintDB()
    user_controller = SignedUserController(user_db)
    complaint_controller = ComplaintController(complaint_db, user_db)
    team_controller = TeamManagementController(team_db, user_db)

    fan = None
    team_owner = None
    system_admin = None
    complaint = None
    answer = 'complaint ans'

    def setUp(self):

        self.user_controller.add_team_owner('user_name', 'password', 'name', date.datetime(1980, 5, 5))
        self.team_owner = self.user_controller.get_user_by_name('user_name')
        self.user_controller.add_fan('fan', '1234', 'name', date.datetime(1993, 1, 9))
        self.fan = self.user_controller.get_user_by_name('fan')
        self.team_controller.open_new_team('Tiberias', self.team_owner.user_id)
        self.complaint_controller.new_complaint('first comp', self.fan.user_id)
        self.complaint = self.complaint_controller.get_complaint(self.complaint_db.get_id_counter()-1)

    def tearDown(self):

        self.team_controller.delete_team('Tiberias')
        self.user_controller.delete_signed_user(self.team_owner.user_id)
        self.user_controller.delete_signed_user(self.fan.user_id)
        self.complaint_controller.delete_complaint(self.complaint.complaint_id)

    # UC 1.1
    def test_init_system(self):
        """we init the DataBase in set up function ^ """
        d2 = date.datetime(1998, 4, 23)
        self.user_controller.add_system_admin("admin", "1234", "ro", d2)
        admin = self.user_controller.get_user_by_name('admin')
        self.assertTrue(self.user_controller.confirm_user('admin', '1234'))
        self.assertRaises(AssertionError, self.user_controller.delete_signed_user, admin.user_id)
        self.user_db.delete_user(admin.user_id)

    def test_init_system_no_acceptance(self):
        """we init the DataBase in set up function ^ """
        d2 = date.datetime(1998, 4, 23)
        self.assertRaises(ValueError, self.user_controller.add_system_admin, "", "1234", "ro", d2)

    # UC 8.1
    def test_close_team(self):
        """admin is connected and chose what team he wants to close"""
        all_teams = self.team_controller.get_all_teams()
        self.assertEqual(len(all_teams),  1)
        """admin see only the team that in the system"""
        """if admin want to exit he press on exit and stop here"""
        self.team_controller.close_team("Tiberias")
        self.assertFalse(self.team_controller.get_team("Tiberias").is_open)

    #UC 8.2
    def test_remove_signed_user(self):
        """ Admin in connected and want to close team """
        d1 = date.datetime(2020, 4, 23)
        d2 = date.datetime(1998, 4, 23)
        self.user_controller.add_fan("name_u1", "1234", "ro", d1)
        self.user_controller.add_fan("admin", "1234", "ro", d2)
        fan = self.user_controller.get_user_by_name('name_u1')
        fan2 = self.user_controller.get_user_by_name('admin')
        self.user_controller.delete_signed_user(fan.user_id)
        self.assertFalse(self.user_controller.confirm_user('name_u1', '1234'))
        self.assertTrue(self.user_controller.confirm_user('admin', '1234'))
        self.user_controller.delete_signed_user(fan2.user_id)


    # UC 8.3
    def test_show_complaint_and_respond(self):
        # admin wants to see all user complaints
        complaints = self.complaint_controller.show_complaints()
        com = self.complaint_db.get_all()
        self.assertEqual(com[0].answer, complaints[0].answer)
        # admin chooses a complaint to answer on
        self.complaint = self.complaint_controller.get_complaint(complaints[0].complaint_id)
        # admin responds to the complaint as he should
        self.complaint_controller.respond_to_complaint(self.answer, complaints[0].complaint_id)
        self.complaint = self.complaint_controller.get_complaint(complaints[0].complaint_id)
        self.assertEqual(self.complaint.answer, self.answer)
