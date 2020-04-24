from unittest import TestCase
from Service.ComplaintController import ComplaintController
from DataBases.ComplaintDB import ComplaintDB
from Domain.Fan import Fan
import datetime as date



class TestComplaintController(TestCase):
    complaint_db = ComplaintDB()
    complaint_controller = ComplaintController(complaint_db)

    def setUp(self):
        self.fan = Fan('TheKid', 'password', 'Name', date.datetime(2000, 1, 1), '1.1.1.1', 111)

    def test_show_complaints(self):
        self.assertEqual(self.complaint_db, self.complaint_controller.show_complaints())

    def test_get_complaint(self):
        self.assertRaises(ValueError, self.complaint_controller.get_complaint, None)
        self.assertRaises(Exception, self.complaint_controller.get_complaint, self.fan)

    def test_new_complaint(self):
        self.assertRaises(ValueError, self.complaint_controller.new_complaint, 'messi isnt 12', None)
        self.assertRaises(TypeError, self.complaint_controller.new_complaint, None, self.fan)
        self.assertRaises(ValueError, self.complaint_controller.new_complaint, None, None)
        self.complaint_controller.new_complaint('messi isnt 12', self.fan)
        self.assertEqual(self.complaint_db.get_complaints(self.fan), self.complaint_controller.get_complaint(self.fan))

    def test_respond_to_complaint(self):
        pass



