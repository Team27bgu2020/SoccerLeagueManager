from unittest import TestCase
from Domain.Team import Team
from Domain.League import League
from Domain.Season import Season
from DataBases.LeagueDB import LeagueDB
from DataBases.SeasonDB import SeasonDB
from DataBases.PolicyDB import PolicyDB
from Service.LeagueController import LeagueController
from Domain.PointsCalculationPolicy import PointsCalculationPolicy
from Domain.TeamBudgetPolicy import TeamBudgetPolicy
from Domain.GameSchedulePolicy import GameSchedulePolicy
from Enums.GameAssigningPoliciesEnum import GameAssigningPoliciesEnum


class AcceptanceTestsUnionRepresentor(TestCase):

    league_controller = LeagueController(LeagueDB(), SeasonDB(), PolicyDB())

    teams = [Team('Real Madrid'), Team('Barcelona'), Team('Liverpool'), Team('Manchester')]
    pcp = PointsCalculationPolicy(3, 0, -3)
    gsp = GameSchedulePolicy(2, 4, ['S', 'M'], GameAssigningPoliciesEnum.EQUAL_HOME_AWAY)
    tbp = TeamBudgetPolicy(50000)
    season = Season(2020)

    league = League('Euro', season, pcp, gsp, tbp)

    # U.C 9.1, 9.5
    def test_create_new_league(self):

        league = self.league_controller.create_new_league('Euro', self.season, self.pcp, self.gsp, self.tbp)
        league.add_teams(self.teams)
        self.assertIsInstance(league, League)

    # U.C 9.2, 9.4, 9.5
    def test_create_new_season(self):

        season = self.league_controller.create_new_season(2020)
        leagues = [self.league]
        self.assertIsInstance(season, Season)
        self.league_controller.add_leagues_to_season(season, leagues)
        self.assertIn(self.league, self.league_controller.get_season(2020)[0].leagues)

    # U.C 9.5
    def test_create_and_update_points_calculation_policy(self):

        pcp = self.league_controller.create_points_calculation_policy(3, 0, -3)
        self.assertIsInstance(pcp, PointsCalculationPolicy)

        self.league_controller.update_points_calculation_policy(self.league, pcp)
        self.assertEqual(pcp, self.league.points_calculation_policy)

    # U.C 9.6
    def test_create_and_update_game_schedule_policy(self):

        gsp = self.league_controller.create_game_schedule_policy(2, 4, ['S', 'M'], GameAssigningPoliciesEnum.RANDOM)
        self.assertIsInstance(gsp, GameSchedulePolicy)

        self.league_controller.update_game_schedule_policy(self.league, gsp)
        self.assertEqual(gsp, self.league.game_schedule_policy)

    # U.C 9.8
    def test_create_and_update_team_budget_policy(self):

        tbp = self.league_controller.create_team_budget_policy(10000)
        self.assertIsInstance(tbp, TeamBudgetPolicy)

        self.league_controller.update_team_budget_policy(self.league, tbp)
        self.assertEqual(tbp, self.league.team_budget_policy)

