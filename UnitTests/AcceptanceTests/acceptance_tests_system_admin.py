from unittest import TestCase
from Service.SignedUserController import SignedUserController
from Service.ComplaintController import ComplaintController
from DataBases.UserDB import UserDB
from DataBases.ComplaintDB import ComplaintDB
from Domain.SystemAdmin import SystemAdmin
from Domain.Team import Team
from Domain.Fan import Fan
import datetime as date


class AcceptanceTestsSystemAdmin(TestCase):
    # Preparation
    fan = Fan('fan', '1234', 'name', date.datetime(1993, 1, 9), '1.1.1.1', 2)
    system_admin = SystemAdmin('boss', '1234', 'name', date.datetime(1993, 1, 9), '1.1.1.1', 1)
    team1 = Team('Hapoel beer sheva', [])
    answer = 'complaint ans'

    def setUp(self):
        self.user_db = UserDB()
        self.user_controller = SignedUserController()

        self.complaint_db = ComplaintDB()
        self.complaint_controller = ComplaintController(self.complaint_db)
        self.complaint_controller.new_complaint('first comp', self.fan)

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
