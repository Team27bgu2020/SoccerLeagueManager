from datetime import datetime
from unittest import TestCase
from Domain.Game import Game
from Domain.Referee import Referee
from Domain.GameEvent import GameEvent
from Domain.Team import Team
from Enums.RefereeQualificationEnum import RefereeQualificationEnum
from Enums.EventTypeEnum import EventTypeEnum


class TestGame(TestCase):

    home_team = Team("Barcelona")
    away_team = Team("Real Madrid")
    d = datetime(2020, 5, 5)
    field = "Camp Nou"
    game = Game(home_team, away_team, d, field)

    """ Testing the set main referee method """

    def test_set_main_referee(self):

        referee = Referee(RefereeQualificationEnum.MAIN, 'Dor123', '12345678', 'Dor', datetime(1990, 8, 8), '1.1.1.1', '')
        self.assertRaises(TypeError, self.game.main_referee, main_referee=self.home_team)
        self.game.main_referee = referee
        self.assertEqual(referee, self.game._Game__main_referee)

    """ Testing the set match time method """

    def test_set_match_time(self):

        self.assertRaises(TypeError, self.game.match_time, match_time=[])
        self.assertEqual(datetime(2020, 5, 5), self.game._Game__match_time)

    """ Testing the set field method """

    def test_set_field(self):

        self.assertRaises(TypeError, self.game.field, match_time=0)
        self.assertEqual(self.field, self.game._Game__field)

    """ Testing the set team method """

    def test_set_team(self):

        self.assertRaises(TypeError, self.game.home_team, match_time=0)
        self.assertIsInstance(self.game._Game__home_team, Team)
        self.assertEqual(self.game._Game__home_team, self.home_team)
        self.assertRaises(TypeError, self.game.away_team, match_time=0)
        self.assertIsInstance(self.game._Game__away_team, Team)
        self.assertEqual(self.game._Game__away_team, self.away_team)

    """ Testing the add referee and remove referee methods """

    def test_add_remove_referee(self):

        m_r = Referee(RefereeQualificationEnum.MAIN, 'Dor123', '12345678', 'Dor', datetime(1990, 8, 8), '1.1.1.1', '')
        r = Referee(RefereeQualificationEnum.REGULAR, 'Dor12', '12345678', 'Dor', datetime(1990, 8, 8), '1.1.1.1', '')

        self.game.main_referee = m_r

        self.game.add_referee(r)
        self.assertIn(r, self.game._Game__referees)

        self.game.remove_referee(r)
        self.assertNotIn(r, self.game._Game__referees)

    """ Testing the add event and remove event methods """

    def test_add_remove_event(self):

        r = Referee(RefereeQualificationEnum.MAIN, 'Dor123', '12345678', 'Dor', datetime(1990, 8, 8), '1.1.1.1', '')
        self.game.add_referee(r)
        game_event = GameEvent(self.game, r, "type", "des", datetime(2020, 5, 5), 89)
        g = Game(self.home_team, self.away_team, self.d, self.field)
        g.main_referee = Referee(RefereeQualificationEnum.MAIN, 'Dor12', '12345678', 'Dor', datetime(1990, 8, 8),
                                 '1.1.1.1', '')
        not_game_event = GameEvent(g, g.main_referee,
                                   EventTypeEnum.GOAL, "des", datetime(2020, 5, 5), 89)

        self.assertRaises(ValueError, self.game.add_event, event=not_game_event)
        self.assertNotIn(not_game_event, self.game._Game__events)

        self.assertIn(game_event, self.game._Game__events)
        self.assertRaises(ValueError, self.game.add_event, event=game_event)

        self.game.remove_event(r)
        self.assertNotIn(r, self.game._Game__events)
        self.game.remove_event(game_event)
        self.assertNotIn(game_event, self.game._Game__events)

    """ Testing the team goals methods """

    def test_team_goal(self):

        self.assertEqual(self.game._Game__home_score, 0)
        self.assertEqual(self.game._Game__away_score, 0)
        self.game.home_team_goal()
        self.game.home_team_goal()
        self.game.away_team_goal()
        self.assertEqual(self.game._Game__home_score, 2)
        self.assertEqual(self.game._Game__away_score, 1)

    """ Testing all the class getters """

    def test_getters(self):

        self.assertEqual(self.game.home_team, self.home_team)
        self.assertEqual(self.game.away_team, self.away_team)
        self.assertEqual(self.game.field, self.field)
        self.assertEqual(self.game.match_time, self.d)
        main_ref = self.game.main_referee
        refs = self.game.referees
        self.assertEqual(main_ref, self.game._Game__main_referee)
        self.assertEqual(refs, self.game._Game__referees)
        self.assertEqual(self.game.score['home'], self.game._Game__home_score)
        self.assertEqual(self.game.score['away'], self.game._Game__away_score)






