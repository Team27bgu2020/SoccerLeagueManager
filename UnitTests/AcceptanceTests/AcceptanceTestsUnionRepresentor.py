from unittest import TestCase
from Domain.Team import Team
from Domain.League import League
from Domain.Season import Season
from DataBases.LeagueDB import LeagueDB
from DataBases.SeasonDB import SeasonDB
from Service.LeagueController import LeagueController
from Domain.PointsCalculationPolicy import PointsCalculationPolicy
from Domain.TeamBudgetPolicy import TeamBudgetPolicy
from Domain.GameSchedulePolicy import GameSchedulePolicy
from Enums.GameAssigningPoliciesEnum import GameAssigningPoliciesEnum


class AcceptanceTestsUnionRepresentor(TestCase):

    league_controller = LeagueController(LeagueDB(), SeasonDB())

    def test_create_new_league(self):

        teams = [Team('Real Madrid'), Team('Barcelona'), Team('Liverpool'), Team('Manchester')]
        pcp = PointsCalculationPolicy(3, 0, -3)
        gsp = GameSchedulePolicy(2, 4, ['S', 'M'], GameAssigningPoliciesEnum.EQUAL_HOME_AWAY)
        tbp = TeamBudgetPolicy(50000)
        season = Season(2020)

        league = self.league_controller.create_new_league('Euro', season, pcp, gsp, tbp)
        league.add_teams(teams)

        self.assertIsInstance(league, League)

    def test_create_new_season(self):

        pcp = PointsCalculationPolicy(3, 0, -3)
        gsp = GameSchedulePolicy(2, 4, ['S', 'M'], GameAssigningPoliciesEnum.EQUAL_HOME_AWAY)
        tbp = TeamBudgetPolicy(50000)
        season = Season(2020)

        league = League('Euro', season, pcp, gsp, tbp)

        season = self.league_controller.create_new_season(2020)
        leagues = [league]
        self.assertIsInstance(season, Season)
        self.league_controller.add_leagues_to_season(season, leagues)
        self.assertIn(league, self.league_controller.get_season(2020)[0].leagues)