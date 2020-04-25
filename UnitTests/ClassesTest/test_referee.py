from unittest import TestCase
import datetime
from Domain.Referee import Referee
from Domain.Game import Game
from Domain.Team import Team
from Domain.GameEvent import GameEvent
from Enums.EventTypeEnum import EventTypeEnum
from Enums.RefereeQualificationEnum import RefereeQualificationEnum


class TestReferee(TestCase):



    def test_add_game(self):
        d1 = datetime.datetime(2020, 4, 23)
        d2 = datetime.datetime(2001, 4, 23)
        ref = Referee(RefereeQualificationEnum.MAIN, "name_u1", "1234", "ro", d1, "0.0.0.5", 23)
        game = Game(Team("Real Madrid"), Team("Barcelona"), d2, "Camp Nou")
        ref.add_game(game)
        self.assertIn(game, ref.referee_in_games)

    def test_remove_game(self):
        d1 = datetime.datetime(2020, 4, 23)
        d2 = datetime.datetime(2001, 4, 23)
        ref = Referee(RefereeQualificationEnum.MAIN, "name_u1", "1234", "ro", d1, "0.0.0.5", 23)
        game1 = Game(Team("Real Madrid"), Team("Barcelona"), d2, "Camp Nou")
        game2 = Game(Team("Real Madrid2"), Team("Barcelona2"), d1, "Camp Nou2")
        ref.add_game(game1)
        ref.add_game(game2)
        self.assertIn(game1, ref.referee_in_games)
        self.assertIn(game2, ref.referee_in_games)
        ref.remove_game(game1)
        self.assertNotIn(game1, ref.referee_in_games)
        self.assertIn(game2, ref.referee_in_games)

    def test_add_event(self):
        d1 = datetime.datetime(2020, 4, 23)
        d2 = datetime.datetime(2001, 4, 23)
        ref = Referee(RefereeQualificationEnum.MAIN, "name_u1", "1234", "ro", d1, "0.0.0.5", 23)
        game1 = Game(Team("Real Madrid"), Team("Barcelona"), d2, "Camp Nou")
        game1.add_referee(ref)
        event1 = GameEvent(game1, ref, EventTypeEnum.GOAL, "Start!", d1, 22)
        self.assertIn(event1, ref.events)
        ref.remove_event(event1)
        self.assertNotIn(event1, ref.events)


    def test_show_games_by_referee(self):
        d1 = datetime.datetime(2020, 4, 23)
        d2 = datetime.datetime(2001, 4, 23)
        ref = Referee(RefereeQualificationEnum.MAIN, "name_u1", "1234", "ro", d1, "0.0.0.5", 23)
        game1 = Game(Team("Real Madrid"), Team("Barcelona"), d2, "Camp Nou")
        game2 = Game(Team("Real Madrid2"), Team("Barcelona2"), d1, "Camp Nou2")
        game1.add_referee(ref)
        ref.add_game(game1)
        self.assertIn(game1, ref.show_games_by_referee())
        self.assertNotIn(game2, ref.show_games_by_referee())
