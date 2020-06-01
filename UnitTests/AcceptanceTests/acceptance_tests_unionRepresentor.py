from unittest import TestCase
from datetime import datetime

from DataBases.MongoDB.MongoPolicyDB import MongoPolicyDB
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
    policy_db = MongoPolicyDB()
    league_controller = LeagueController(league_db, season_db, user_db, policy_db)
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
        self.season = self.league_controller.get_season(2020)

        self.league_controller.create_points_policy(3, 0, -3)
        self.points_policy = self.league_controller.get_all_points_policies()[0]
        self.league_controller.create_game_schedule_policy(2, 4, GameAssigningPoliciesEnum.EQUAL_HOME_AWAY)
        self.schedule_policy = self.league_controller.get_all_schedule_policies()[0]
        self.league_controller.create_team_budget_policy(50000)
        self.budget_policy = self.league_controller.get_all_budget_policies()[0]

        self.league_controller.create_new_league('Euro', 2020, self.points_policy.policy_id, self.schedule_policy.policy_id, self.budget_policy.policy_id)
        self.league = self.league_controller.get_league(self.league_db.get_id_counter()-1)

    def tearDown(self):

        self.league_db.reset_db()
        self.league_controller.delete_points_calculation_policy(self.points_policy.policy_id)
        self.league_controller.delete_schedule_calculation_policy(self.schedule_policy.policy_id)
        self.league_controller.delete_budget_calculation_policy(self.budget_policy.policy_id)
        self.season_db.reset_db()
        self.team_db.reset_db()
        self.user_db.reset_db()

    # U.C 9.1, 9.5
    def test_create_new_league(self):

        self.assertIsInstance(self.league, League)
        self.league.add_teams(['Real Madrid', 'Barcelona', 'Liverpool', 'Manchester'])
        # wrong values
        self.assertRaises(ValueError, self.league_controller.create_new_league,
                          'Euro', 2021, self.points_policy.policy_id+1, self.schedule_policy.policy_id, self.budget_policy.policy_id)

    # U.C 9.2, 9.4, 9.5
    def test_create_new_season(self):

        self.assertIsInstance(self.season, Season)
        self.assertIn(self.league.league_id, self.league_controller.get_season(2020).leagues)
        # wrong values
        self.assertRaises(ValueError, self.league_controller.create_new_season, 2020)

    # U.C 9.5
    def test_create_and_update_points_calculation_policy(self):

        self.assertIsInstance(self.points_policy, PointsCalculationPolicy)

        self.league_controller.create_points_policy(5, 0, -5)

        self.league_controller.update_points_calculation_policy_in_league(self.league.league_id, self.policy_db.get_points_id_counter()-1)
        self.league = self.league_controller.get_league(self.league.league_id)
        self.assertEqual(self.policy_db.get_points_id_counter()-1, self.league.points_calculation_policy)

        self.league_controller.delete_points_calculation_policy(self.policy_db.get_points_id_counter()-1)


    # U.C 9.6
    def test_create_and_update_game_schedule_policy(self):

        self.assertIsInstance(self.schedule_policy, GameSchedulePolicy)

        self.league_controller.create_game_schedule_policy(5, 5, GameAssigningPoliciesEnum.RANDOM)

        self.league_controller.update_game_schedule_policy_in_league(self.league.league_id, self.policy_db.get_schedule_id_counter()-1)
        self.league = self.league_controller.get_league(self.league.league_id)
        self.assertEqual(self.policy_db.get_schedule_id_counter()-1, self.league.game_schedule_policy)

        self.league_controller.delete_schedule_calculation_policy(self.policy_db.get_schedule_id_counter()-1)

    # U.C 9.8
    def test_create_and_update_team_budget_policy(self):

        self.assertIsInstance(self.budget_policy, TeamBudgetPolicy)

        self.league_controller.create_team_budget_policy(10000)

        self.league_controller.update_team_budget_policy_in_league(self.league.league_id, self.policy_db.get_budget_id_counter() - 1)
        self.league = self.league_controller.get_league(self.league.league_id)
        self.assertEqual(self.policy_db.get_budget_id_counter()-1, self.league.team_budget_policy)

        self.league_controller.delete_budget_calculation_policy(self.policy_db.get_budget_id_counter()-1)

    # U.U 9.9
    def test_manage_union_budget(self):

        self.team_controller.add_income_to_team('Real Madrid', 10000, 'income')
        t1 = self.team_controller.get_team('Real Madrid')
        self.team_controller.add_income_to_team("Barcelona", 2000, 'income')
        t2 = self.team_controller.get_team("Barcelona")

        organization = UnionOrganization()
        union_controller = UnionController(organization, self.user_db, self.team_db, 5000)
        union_controller.add_team_to_union(t1.name)
        union_controller.add_team_to_union(t2.name)

        union_controller.add_income(10000, '')
        self.assertEqual(10000, organization.balance)
        # wrong value
        self.assertRaises(ValueError, union_controller.add_income, -10000, '')

        union_controller.add_expense(10000, '')
        self.assertEqual(0, organization.balance)
        # wrong value
        self.assertRaises(ValueError, union_controller.add_expense, -10000, '')

        self.assertIn(t2.name, organization.teams_in_union)
        union_controller.collect_registration_fee()
        self.assertEqual(5000, organization.balance)
        self.assertIn(t1.name, organization.teams_in_union)
        self.assertNotIn(t2.name, organization.teams_in_union)

        self.user_controller.add_union_representor('Dor123', '12345678', 'Dor', datetime(1990, 8, 8), 2000)
        representor = self.user_controller.get_user_by_name('Dor123')
        organization.add_employee_to_union(representor.user_id)
        union_controller.pay_employees()
        self.assertEqual(3000, organization.balance)
        union_controller.remove_employee_from_union(representor.user_id)
        union_controller.remove_team_from_union(t1.name)
        self.user_controller.delete_signed_user(representor.user_id)
        organization.reset_organization()