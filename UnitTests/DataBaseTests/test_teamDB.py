from unittest import TestCase

from DataBases.TeamDB import TeamDB
from Domain.Team import Team


class TestTeamDB(TestCase):
    db = TeamDB()
    team = Team("Real Madrid")
    team = Team("Barca")

    def test_add(self):
        self.db.add(self.team)
        self.assertEqual(1, self.db.teams.__len__())
        self.assertRaises(ValueError, self.db.add, self.team)

    def test_delete(self):
        self.db.add(self.team)
        self.assertEqual(1, self.db.teams.__len__())
        self.db.delete("Barca")
        self.assertEqual(0, self.db.teams.__len__())
        self.assertRaises(ValueError, self.db.delete,"Barca")

    def test_get(self):
        self.db.add(self.team)
        # containing the team
        self.assertEqual(self.db.get("Barca"), self.team)
        self.assertRaises(ValueError, self.db.get, "Real")
