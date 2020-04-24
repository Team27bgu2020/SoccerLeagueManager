import datetime as date
from unittest import TestCase

from Domain.Fan import Fan
from Domain.PersonalPage import PersonalPage
from Domain.Game import Game
from Domain.Team import Team
from Domain.RecommendationSystem import RecommendationSystem

""" Idan """

class TestFan(TestCase):

    home_team = Team("Barcelona")
    away_team = Team("Real Madrid")
    d = date.datetime(2020, 5, 5)
    field = "Camp Nou"
    game = Game(home_team, away_team, d, field)

    page = PersonalPage("Messi")

    recommend_me = RecommendationSystem()

    def setUp(self):
        user_name = 'default'
        password = 'default'
        name = 'default'
        birth_date = date.datetime(2000, 1, 1)
        ip = '1.1.1.1'
        user_id = 111
        self.fan = Fan(user_name, password, name, birth_date, ip, user_id)

    def tearDown(self):
        pass

    """ Testing the follow personal page method """

    def test_follow_page(self):
        self.assertRaises(TypeError, self.fan.follow_page, self.home_team)
        self.fan.follow_page(self.page)
        self.assertRaises(ValueError, self.fan.follow_page, self.page)
        self.assertIn(self.page, self.fan._Fan__followed_pages)

    """ Testing the unfollow personal page method """

    def test_unfollow_page(self):
        self.assertRaises(TypeError, self.fan.unfollow_page, self.home_team)
        self.assertRaises(ValueError, self.fan.unfollow_page, self.page)
        self.fan.follow_page(self.page)
        self.assertIn(self.page, self.fan._Fan__followed_pages)
        self.fan.unfollow_page(self.page)
        self.assertNotIn(self.page, self.fan._Fan__followed_pages)

    """ Testing the follow game method """

    def test_follow_game(self):
        self.assertRaises(TypeError, self.fan.follow_game, self.home_team)
        self.fan.follow_game(self.game)
        self.assertRaises(ValueError, self.fan.follow_game, self.game)
        self.assertIn(self.game, self.fan._Fan__followed_games)

    """ Testing the unfollow game method """

    def test_unfollow_game(self):
        self.assertRaises(TypeError, self.fan.unfollow_game, self.home_team)
        self.assertRaises(ValueError, self.fan.unfollow_game, self.game)
        self.fan.follow_game(self.game)
        self.assertIn(self.game, self.fan._Fan__followed_games)
        self.fan.unfollow_game(self.game)
        self.assertNotIn(self.game, self.fan._Fan__followed_games)

    """ Testing for set recommendation system method"""

    def test_set_recommendation_system(self):
        self.assertRaises(TypeError, self.fan.set_recommendation_system, self.home_team)
        self.fan.set_recommendation_system(self.recommend_me)
        self.assertIs(self.recommend_me, self.fan._Fan__recommendation_system)

    def test_complain(self):
        pass




