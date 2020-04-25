from unittest import TestCase
from Service.ComplaintController import ComplaintController
from DataBases.ComplaintDB import ComplaintDB
from Domain.Fan import Fan
import datetime as date



class TestComplaintController(TestCase):
    complaint_db = ComplaintDB()
    complaint_controller = ComplaintController(complaint_db)
    fan = Fan('TheKid', 'password', 'Name', date.datetime(2000, 1, 1), '1.1.1.1', 111)

    def setUp(self):
        pass

    def test_show_complaints(self):
        self.assertEqual(self.complaint_db, self.complaint_controller.show_complaints())
        self.complaint_controller.new_complaint('messi isnt 12', self.fan)
        self.assertEqual(self.complaint_db, self.complaint_controller.show_complaints())

    def test_get_complaint(self):
        self.assertRaises(ValueError, self.complaint_controller.get_complaint, None, 0)
        self.assertRaises(Exception, self.complaint_controller.get_complaint, self.fan, 0)

    def test_new_complaint(self):
        self.assertRaises(ValueError, self.complaint_controller.new_complaint, 'messi isnt 12', None)
        self.assertRaises(TypeError, self.complaint_controller.new_complaint, None, self.fan)
        self.assertRaises(ValueError, self.complaint_controller.new_complaint, None, None)
        self.complaint_controller.new_complaint('barda doesnt play anymore', self.fan)
        self.assertEqual(self.complaint_db.get_complaints(self.fan, 1), self.complaint_controller.get_complaint(self.fan, 1))

    def test_respond_to_complaint(self):
        self.assertRaises(ValueError, self.complaint_controller.respond_to_complaint, 'messi is 33', None, 0)
        self.assertRaises(TypeError, self.complaint_controller.respond_to_complaint, None, self.fan, 0)
        self.complaint_controller.new_complaint('messi isnt 12', self.fan)
        self.complaint_controller.respond_to_complaint('messi is 33', self.fan, 2)
        self.assertEqual(self.fan.complaints[1].answer, 'messi is 33')




