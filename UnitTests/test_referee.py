from unittest import TestCase
import datetime as date
from Domain.Referee import Referee
from Domain.Game import Game
from Domain.Team import Team
from Domain.GameEvent import GameEvent
from Domain.Enums import RefereeQualification


class TestReferee(TestCase):

    ref = Referee(RefereeQualification.MAIN)
    game = Game(Team("Real Madrid"), Team("Barcelona"), date.datetime(2020, 7, 7), "Camp Nou")

    def test_add_event(self):

        event = GameEvent(self.game, self.ref, "", "", date(2020, 7, 7), 22)
        self.assertRaises(TypeError, self.ref.add_event, event=[])
        self.assertIn(event, self.ref._Referee__events)

    def test_qualification(self):
        self.fail()
