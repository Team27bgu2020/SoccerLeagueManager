from unittest import TestCase
from Domain.Team import Team
from Domain.Game import Game
from Domain.Season import Season
from Domain.Player import Player
from Domain.League import League
from Domain.TeamUser import TeamUser
from datetime import datetime as date
from Domain.GameSchedulePolicy import GameSchedulePolicy
from Domain.PointsCalculationPolicy import PointsCalculationPolicy


class TestTeam(TestCase):

    team = Team("Real Madrid")
    field = "Camp Nou"

    """ Testing the add league method """

    def test_add_league(self):

        league = League("Euro", Season(2020), PointsCalculationPolicy(), GameSchedulePolicy())

        self.assertRaises(TypeError, self.team.add_league, league=[])
        self.team.add_league(league)
        self.assertEqual(league, self.team._Team__leagues[2020][0])

    """ Testing the game over method """

    def test_game_over(self):

        g = Game(self.team, Team("Barcelona"), date(2020, 7, 7), self.field)
        self.team.add_game(g)
        self.team.game_over(g)
        self.assertIn(g, self.team._Team__past_games)
        self.assertNotIn(g, self.team._Team__upcoming_games)

    """ Testing methods:
        1. add_game
        2. add_games
        3. collision_game_check 
        4. remove_upcoming_game """

    def test_add_game(self):

        g = Game(self.team, Team("Barcelona"), date(2020, 5, 5), self.field)
        g_l = [g]
        self.assertRaises(TypeError, self.team.add_games, game={})
        self.team.add_games(g_l)
        self.assertIn(g, self.team._Team__upcoming_games)

        self.team.remove_upcoming_game(None)
        self.assertIn(g, self.team._Team__upcoming_games)
        self.team.remove_upcoming_game(g)
        self.assertNotIn(g, self.team._Team__upcoming_games)

        self.assertRaises(TypeError, self.team.add_game, game={})
        self.assertTrue(self.team.add_game(g))
        self.assertTrue(self.team.collision_game_check(g))
        self.assertFalse(self.team.add_game(g))
        self.assertIn(g, self.team._Team__upcoming_games)

    """ Testing methods:
        1. add_team_member 
        2. remove_team_member 
        3. add_team_members 
        4. remove_team_members """

    def test_team_members_management(self):

        u1 = TeamUser(self.team, Player())
        u2 = TeamUser(self.team, Player())
        u_l = [u1, u2]

        self.assertRaises(TypeError, self.team.add_team_member, team_member=0)
        self.team.add_team_member(u1)
        self.assertRaises(ValueError, self.team.add_team_member, team_member=u1)
        self.assertEqual(u1._TeamUser__team, self.team)
        self.assertIn(u1, self.team._Team__team_members)

        self.team.remove_team_member(0)
        self.assertIn(u1, self.team._Team__team_members)
        self.assertNotIn(0, self.team._Team__team_members)
        self.team.remove_team_member(u1)
        self.assertNotIn(u1, self.team._Team__team_members)

        self.assertRaises(TypeError, self.team.add_team_members, team_member=u1)
        self.team.add_team_members(u_l)
        self.assertIn(u1, self.team._Team__team_members)
        self.assertIn(u2, self.team._Team__team_members)

        self.assertRaises(TypeError, self.team.remove_team_members, team_members=0)
        self.team.remove_team_members(u_l)
        self.assertNotIn(u1, self.team._Team__team_members)
        self.assertNotIn(u2, self.team._Team__team_members)

    """ Testing methods:
        1. close_team
        2. open_team """

    def test_team_members_management(self):

        self.team.close_team()
        self.assertFalse(self.team._Team__is_open)

        self.team.open_team()
        self.assertTrue(self.team._Team__is_open)






