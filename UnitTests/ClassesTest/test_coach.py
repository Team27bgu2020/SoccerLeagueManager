from unittest import TestCase
from Domain.Coach import Coach


class TestCoach(TestCase):
    coach = Coach(qualification='1')

    def test_set_qualification_name(self):
        self.assertEqual(self.coach.qualification, '1')
        self.coach.qualification = '2'
        self.assertEqual(self.coach.qualification, "2")
        self.assertRaises(TypeError, self.coach.qualification, 6)

