from unittest import TestCase
from Service.NotificationsController import NotificationController
from Domain.Fan import Fan
from Domain.Team import Team
from Domain.Referee import Referee
from Enums.RefereeQualificationEnum import RefereeQualificationEnum
from Enums.EventTypeEnum import EventTypeEnum
from datetime import datetime
from Domain.Game import Game
from Domain.GameEvent import GameEvent


class TestNotifications(TestCase):
    not_cont = NotificationController()
    fan1 = Fan("user1", "123", "nameOne", datetime(1993, 1, 1), "1.1.1.1", "1")
    fan2 = Fan("user2", "123", "nameTwo", datetime(1993, 1, 1), "1.1.1.1", "2")
    fan3 = Fan("user3", "123", "nameThree", datetime(1993, 1, 1), "1.1.1.1", "3")
    team1 = Team("team1")
    team2 = Team("team2")
    game1 = Game(team1, team2, datetime.today(), "field1")
    game2 = Game(team1, team2, datetime.today(), "field2")
    referee1 = Referee(RefereeQualificationEnum.MAIN, "user4", "123", "userFour", datetime.today(), "1", "4")
    referee2 = Referee(RefereeQualificationEnum.MAIN, "user5", "123", "userFive", datetime.today(), "1", "5")

    not_cont.add_fan_follower_to_game(fan1, game1)
    not_cont.add_fan_follower_to_game(fan2, game1)
    not_cont.add_fan_follower_to_game(fan2, game2)

    game1.add_referee(referee1)
    game2.add_referee(referee2)
    game_event1 = GameEvent(game1, referee1, EventTypeEnum.YELLOW_CARD, "desc", datetime.today(), 5)
    game_event2 = GameEvent(game2, referee2, EventTypeEnum.GOAL, "desc", datetime.today(), 5)

    def test_add_follower(self):
        self.assertEqual(len(self.fan1.notifications), 2)
        self.assertEqual(len(self.fan2.notifications), 4)
        self.assertEqual(len(self.fan3.notifications), 0)

    def test_remove_follower(self):
        self.not_cont.remove_fan_follower_from_game(self.fan2, self.game1)
        self.game1.remove_referee(self.referee1)
        self.assertEqual(len(self.fan1.notifications), 3)
        self.assertEqual(len(self.fan2.notifications), 4)
        self.assertEqual(len(self.fan3.notifications), 0)
