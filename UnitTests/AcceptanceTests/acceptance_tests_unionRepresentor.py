from unittest import TestCase
from datetime import datetime
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
from Domain.UnionOrganization import UnionOrganization
from Service.UnionController import UnionController
from Domain.UnionRepresentor import UnionRepresentor


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
        # wrong values
        self.assertRaises(ValueError, self.league_controller.create_new_league,
                          'Euro', self.season, self.pcp, self.gsp, self.tbp)

    # U.C 9.2, 9.4, 9.5
    def test_create_new_season(self):

        season = self.league_controller.create_new_season(2020)
        leagues = [self.league]
        self.assertIsInstance(season, Season)
        self.league_controller.add_leagues_to_season(season, leagues)
        self.assertIn(self.league, self.league_controller.get_season(2020).leagues)
        # wrong values
        self.assertRaises(ValueError, self.league_controller.create_new_season, 2020)

    # U.C 9.5
    def test_create_and_update_points_calculation_policy(self):

        pcp = self.league_controller.create_points_calculation_policy(3, 0, -3)
        self.assertIsInstance(pcp, PointsCalculationPolicy)

        self.league_controller.update_points_calculation_policy(self.league, pcp)
        self.assertEqual(pcp, self.league.points_calculation_policy)
        # wrong values
        self.assertRaises(ValueError, self.league_controller.create_points_calculation_policy, 3, 0, -3)

    # U.C 9.6
    def test_create_and_update_game_schedule_policy(self):

        gsp = self.league_controller.create_game_schedule_policy(2, 4, ['S', 'M'], GameAssigningPoliciesEnum.RANDOM)
        self.assertIsInstance(gsp, GameSchedulePolicy)

        self.league_controller.update_game_schedule_policy(self.league, gsp)
        self.assertEqual(gsp, self.league.game_schedule_policy)
        # wrong values
        self.assertRaises(ValueError, self.league_controller.create_game_schedule_policy,
                          2, 4, ['S', 'M'], GameAssigningPoliciesEnum.RANDOM)

    # U.C 9.8
    def test_create_and_update_team_budget_policy(self):

        tbp = self.league_controller.create_team_budget_policy(10000)
        self.assertIsInstance(tbp, TeamBudgetPolicy)

        self.league_controller.update_team_budget_policy(self.league, tbp)
        self.assertEqual(tbp, self.league.team_budget_policy)
        # wrong values
        self.assertRaises(ValueError, self.league_controller.create_team_budget_policy, 10000)

    # U.U 9.9
    def test_manage_union_budget(self):

        t1 = Team("Real")
        t1.add_income(10000, '')
        t2 = Team("Barcelona")
        t2.add_income(2000, '')
        organization = UnionOrganization()
        organization.add_team_to_union(t1)
        organization.add_team_to_union(t2)
        union_controller = UnionController(organization, 5000)

        union_controller.add_income(10000, '')
        self.assertEqual(10000, organization.balance)
        # wrong value
        self.assertRaises(ValueError, union_controller.add_income, -10000, '')

        union_controller.add_expense(10000, '')
        self.assertEqual(0, organization.balance)
        # wrong value
        self.assertRaises(ValueError, union_controller.add_expense, -10000, '')

        self.assertIn(t2, organization.teams_in_union)
        union_controller.collect_registration_fee()
        self.assertEqual(5000, organization.balance)
        self.assertIn(t1, organization.teams_in_union)
        self.assertNotIn(t2, organization.teams_in_union)

        representor = UnionRepresentor('Dor123', '12345678', 'Dor', datetime(1990, 8, 8), '1.1.1.1', '', 2000)
        organization.add_employee_to_union(representor)
        union_controller.pay_employees()
        self.assertEqual(3000, organization.balance)