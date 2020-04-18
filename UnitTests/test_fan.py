import datetime as date
from unittest import TestCase

from Domain.Fan import Fan
from Domain.SignedUser import SignedUser
from Domain.PersonalPage import PersonalPage
from Domain.Game import Game
from Domain.Team import Team


class TestFan(TestCase):


    home_team = Team("Barcelona")
    away_team = Team("Real Madrid")
    d = date.datetime(2020, 5, 5)
    field = "Camp Nou"
    game = Game(home_team, away_team, d, field)

    page = PersonalPage()

    def setUp(self):
        user_name = 'default'
        password = 'default'
        name = 'default'
        birth_date = date.datetime(2000, 1, 1)
        self.fan = Fan(user_name, password, name, birth_date)

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



