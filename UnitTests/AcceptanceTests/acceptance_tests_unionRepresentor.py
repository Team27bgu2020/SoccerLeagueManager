from unittest import TestCase
from datetime import datetime
from Domain.Team import Team
from Domain.League import League
from Domain.Season import Season
from DataBases.MongoDB.MongoLeagueDB import MongoLeagueDB
from DataBases.MongoDB.MongoSeasonDB import MongoSeasonDB
from DataBases.MongoDB.MongoUsersDB import MongoUserDB
from DataBases.MongoDB.MongoTeamDB import MongoTeamDB
from Service.LeagueController import LeagueController
from Domain.PointsCalculationPolicy import PointsCalculationPolicy
from Domain.TeamBudgetPolicy import TeamBudgetPolicy
from Domain.GameSchedulePolicy import GameSchedulePolicy
from Enums.GameAssigningPoliciesEnum import GameAssigningPoliciesEnum
from Domain.UnionOrganization import UnionOrganization
from Service.UnionController import UnionController
from Service.TeamManagementController import TeamManagementController
from Service.SignedUserController import SignedUserController
from Domain.UnionRepresentor import UnionRepresentor


class AcceptanceTestsUnionRepresentor(TestCase):

    league_db = MongoLeagueDB()
    season_db = MongoSeasonDB()
    user_db = MongoUserDB()
    team_db = MongoTeamDB()
    league_controller = LeagueController(league_db, season_db, user_db)
    team_controller = TeamManagementController(team_db, user_db)
    user_controller = SignedUserController(user_db)

    pcp = {
        'win_points': 3,
        'tie_points': 0,
        'lose_points': -3
    }

    gsp = {
        'team_games_num': 2,
        'games_per_week': 4,
        'chosen_days': ['S', 'M'],
        'games_stadium_assigning': GameAssigningPoliciesEnum.EQUAL_HOME_AWAY
    }

    tbp = {
        'min_amount': 50000
    }

    def setUp(self):

        self.user_controller.add_team_owner('rm_owner', '1234', 'owner', datetime.now())
        self.rm_owner = self.user_controller.get_user_by_name('rm_owner')
        self.user_controller.add_team_owner('barca_owner', '1234', 'owner', datetime.now())
        self.barca_owner = self.user_controller.get_user_by_name('barca_owner')
        self.user_controller.add_team_owner('lp_owner', '1234', 'owner', datetime.now())
        self.lp_owner = self.user_controller.get_user_by_name('lp_owner')
        self.user_controller.add_team_owner('manch_owner', '1234', 'owner', datetime.now())
        self.manch_owner = self.user_controller.get_user_by_name('manch_owner')

        self.team_controller.open_new_team('Real Madrid', self.rm_owner.user_id)
        self.team_controller.open_new_team('Barcelona', self.barca_owner.user_id)
        self.team_controller.open_new_team('Liverpool', self.lp_owner.user_id)
        self.team_controller.open_new_team('Manchester', self.manch_owner.user_id)

        self.league_controller.create_new_season(2020)
        self.league_controller.create_new_league('Euro', 2020, self.pcp, self.gsp, self.tbp)

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

        representor = UnionRepresentor('Dor123', '12345678', 'Dor', datetime(1990, 8, 8), '', 2000)
        organization.add_employee_to_union(representor)
        union_controller.pay_employees()
        self.assertEqual(3000, organization.balance)