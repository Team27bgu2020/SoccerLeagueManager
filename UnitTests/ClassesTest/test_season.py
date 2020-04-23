from unittest import TestCase
from Domain.Season import Season
from Domain.League import League
from Domain.GameSchedulePolicy import GameSchedulePolicy
from Domain.PointsCalculationPolicy import PointsCalculationPolicy
from Domain.TeamBudgetPolicy import TeamBudgetPolicy
from Enums.GameAssigningPoliciesEnum import GameAssigningPoliciesEnum


class TestSeason(TestCase):

    season = Season(2020)

    """ Testing add_league and remove_league methods """

    def test_add_league(self):

        league = League("Euro", Season(2020), PointsCalculationPolicy(3, 0, -3),
                        GameSchedulePolicy(1, GameAssigningPoliciesEnum.RANDOM, '', ''), TeamBudgetPolicy(50000))
        self.assertRaises(TypeError, self.season.add_league, team=0)
        self.season.add_league(league)
        self.assertIn(league, self.season._Season__leagues)

        self.assertRaises(TypeError, self.season.remove_league, team=0)
        self.season.remove_league(league)
        self.assertNotIn(league, self.season._Season__leagues)

    """ Testing Getters """

    def test_getters(self):

        self.assertEqual(self.season.year, 2020)

