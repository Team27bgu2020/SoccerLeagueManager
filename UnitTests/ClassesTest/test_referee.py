from unittest import TestCase
import datetime as date
from Domain.Referee import Referee
from Domain.Game import Game
from Domain.Team import Team
from Domain.GameEvent import GameEvent
from Enums.RefereeQualificationEnum import RefereeQualificationEnum


class TestReferee(TestCase):

    ref = Referee(RefereeQualificationEnum.MAIN)
    game = Game(Team("Real Madrid"), Team("Barcelona"), date.datetime(2020, 7, 7), "Camp Nou")

    def test_add_event(self):

        self.game.add_referee(self.ref)
        event = GameEvent(self.game, self.ref, "", "", date.datetime(2020, 7, 7), 22)

        self.assertIn(event, self.ref._Referee__events)
