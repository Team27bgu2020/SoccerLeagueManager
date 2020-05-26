from unittest import TestCase
from Domain.Team import Team
from Domain.Game import Game
from Domain.Season import Season
from Domain.Player import Player
from Domain.League import League
from datetime import datetime as date
from Domain.GameSchedulePolicy import GameSchedulePolicy
from Domain.PointsCalculationPolicy import PointsCalculationPolicy
from Domain.TeamBudgetPolicy import TeamBudgetPolicy
from Domain.TeamUser import TeamUser
from Enums.GameAssigningPoliciesEnum import GameAssigningPoliciesEnum


class TestTeam(TestCase):
    team = Team("Real Madrid")
    field = "Camp Nou"

    def setUp(self):
        self.team = Team("Real Madrid")
        self.field = "Camp Nou"

    """ Testing the arguments of init"""

    def test_init(self):
        self.assertRaises(TypeError, Team, 4)

    """ Testing the add league method """

    def test_add_league(self):
        league = League("Euro", Season(2020), PointsCalculationPolicy(3, 0, -3),
                        GameSchedulePolicy(1, GameAssigningPoliciesEnum.RANDOM, '', ''), TeamBudgetPolicy(1000))

        self.team.add_league(league)
        self.assertEqual(league, self.team._Team__leagues[2020][0])

    """ Testing the game over method """

    def test_game_over(self):
        g = Game(self.team, Team("Barcelona"), date(2020, 7, 7), self.field)
        g_error = Game(self.team, Team("RealMadrid"), date(2020, 7, 7), self.field)
        self.team.add_game(g)
        self.team.game_over(g)
        self.assertIn(g, self.team.past_games)
        self.assertNotIn(g, self.team.upcoming_games)
        self.assertRaises(ValueError,self.team.game_over, g_error)

    """ Testing methods:
        1. add_game
        2. add_games
        3. collision_game_check 
        4. remove_upcoming_game """

    def test_add_game(self):
        g = Game(self.team, Team("Barcelona"), date(2020, 5, 5), self.field)
        g_l = [g]
        self.team.add_games(g_l)
        self.assertRaises(TypeError,self.team.add_games, g)
        self.assertIn(g, self.team.upcoming_games)
        self.assertIn(g, self.team.upcoming_games)
        self.team.remove_upcoming_game(g)
        self.assertNotIn(g, self.team.upcoming_games)

        self.team.add_game(g)
        self.assertEqual(1, len(self.team.upcoming_games))
        self.assertTrue(self.team.collision_game_check(g))
        self.assertRaises(ValueError, self.team.add_game, g)
        self.assertIn(g, self.team.upcoming_games)

    """ Testing methods:
        1. add_team_member 
        2. remove_team_member 
        3. add_team_members 
        4. remove_team_members """

    def test_team_members_management(self):

        u1 = TeamUser('user_nam3', 'password', 'NameC', date(1993, 1, 12), "0.0.0.3", 3,team=None, role=Player())
        u2 = TeamUser('user_nam4', 'password', 'NameD', date(1993, 1, 12), "0.0.0.4", 3, team=None, role=Player())
        u_l = [u1, u2]

        self.team.add_team_member(u1)
        self.assertRaises(ValueError, self.team.add_team_member, team_member=u1)
        self.assertEqual(u1.team, self.team)
        self.assertIn(u1, self.team.team_members)

        self.team.remove_team_member(u1)
        self.assertNotIn(u1, self.team.team_members)

        self.assertRaises(TypeError, self.team.add_team_members, team_member=u1)
        self.team.add_team_members(u_l)
        self.assertIn(u1, self.team.team_members)
        self.assertIn(u2, self.team.team_members)

        self.assertRaises(TypeError, self.team.remove_team_members, team_members=0)
        self.team.remove_team_members(u_l)
        self.assertNotIn(u1, self.team.team_members)
        self.assertNotIn(u2, self.team.team_members)

    """ Testing methods:
        1. close_team
        2. open_team """

    def test_open_close(self):
        self.team.close_team()
        self.assertFalse(self.team.is_open)

        self.team.open_team()
        self.assertTrue(self.team.is_open)
