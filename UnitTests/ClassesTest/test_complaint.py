from unittest import TestCase
from Domain.Fan import Fan
from Domain.Complaint import Complaint
import datetime as date


class TestComplaint(TestCase):
    description = 'complaint desc'
    complaint_id = 1
    answer = 'complaint ans'
    complainer = Fan('default', 'default', 'default', date.datetime(2000, 1, 1), '1.1.1.1', 111)
    complaint = Complaint(description, complainer, complaint_id)


    def test_set_answer(self):
        self.complaint.set_answer(self.answer)
        self.assertEqual(self.complaint.answer, 'complaint ans')

    def test_getters(self):
        self.assertEqual(self.complaint.complaint_ID, 1)
        self.assertEqual(self.complaint.description, 'complaint desc')
        self.assertEqual(self.complaint.complainer, self.complainer)
