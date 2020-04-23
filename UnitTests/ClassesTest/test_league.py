from unittest import TestCase
from Domain.Team import Team
from Domain.Referee import Referee
from Domain.Season import Season
from Domain.League import League
from Domain.GameSchedulePolicy import GameSchedulePolicy
from Domain.PointsCalculationPolicy import PointsCalculationPolicy
from Domain.TeamBudgetPolicy import TeamBudgetPolicy
from Enums.GameAssigningPoliciesEnum import GameAssigningPoliciesEnum
from Enums.RefereeQualificationEnum import RefereeQualificationEnum


class TestLeague(TestCase):

    season = Season(2020)
    pcp = PointsCalculationPolicy(3, 0, -3)
    gsp = GameSchedulePolicy(1, GameAssigningPoliciesEnum.RANDOM, '', '')
    tbp = TeamBudgetPolicy()
    league = League("Euro", season, pcp, gsp, tbp)

    """ Testing add_team and remove_team method """

    def test_add_remove_team(self):

        team = Team("Real Madrid")
        self.league.add_team(team)
        self.assertIn(team, self.league._League__teams[team.name])

        self.league.remove_team(team.name)
        self.assertNotIn(team.name, self.league._League__teams.keys())

    """ Testing add_referee and remove_referee method """

    def test_add_remove_referee(self):

        ref = Referee(RefereeQualificationEnum.MAIN)
        self.league.add_referee(ref)
        self.assertIn(ref, self.league._League__referees)

        self.league.remove_referee(ref)
        self.assertNotIn(ref, self.league._League__referees)

    """ Testing Getters """

    def test_getters(self):

        self.assertEqual(self.league.name, "Euro")
        self.assertEqual(self.league.season, self.season)
        self.assertEqual(self.league.points_calculation_policy, self.pcp)
        self.assertEqual(self.league.game_schedule_policy, self.gsp)

    """ Testing set_points_calculation_policy method """

    def test_set_points_calculation_policy(self):

        p = PointsCalculationPolicy(1, 0, -1)
        self.league.points_calculation_policy = p
        self.assertEqual(p, self.league._League__policies['Points'])
        self.league.points_calculation_policy = self.pcp

    """ Testing set_game_schedule_policy method """

    def test_set_game_schedule_policy(self):

        p = GameSchedulePolicy(1, GameAssigningPoliciesEnum.EQUAL_HOME_AWAY, '', '')
        self.league.game_schedule_policy = p
        self.assertEqual(p, self.league._League__policies['Schedule'])
        self.league.game_schedule_policy = self.gsp
