from unittest import TestCase
from Domain.Coach import Coach


class TestCoach(TestCase):
    coach = Coach("1")

    def test_set_qualification_name(self):
        self.coach.to_string()
        self.assertEqual(self.coach.get_qualification_name(), "1")
        self.coach.set_qualification_name("2")
        self.assertEqual(self.coach.get_qualification_name(), "2")
