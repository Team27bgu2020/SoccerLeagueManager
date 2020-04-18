from unittest import TestCase
from Domain.Season import Season
from Domain.League import League
from Domain.GameSchedulePolicy import GameSchedulePolicy
from Domain.PointsCalculationPolicy import PointsCalculationPolicy

class TestSeason(TestCase):

    season = Season(2020)

    """ Testing add_league and remove_league methods """

    def test_add_league(self):

        l = League("Euro", Season(2020), PointsCalculationPolicy(), GameSchedulePolicy())
        self.assertRaises(TypeError, self.season.add_league, team=0)
        self.season.add_league(l)
        self.assertIn(l, self.season._Season__leagues)

        self.assertRaises(TypeError, self.season.remove_league, team=0)
        self.season.remove_league(l)
        self.assertNotIn(l, self.season._Season__leagues)

    """ Testing Getters """

    def test_getters(self):

        self.assertEqual(self.season.year, 2020)

