from unittest import TestCase
from Service.MatchController import MatchController
from DataBases.GameDB import GameDB
from Domain.Team import Team
from Domain.Referee import Referee
from Enums.RefereeQualificationEnum import RefereeQualificationEnum
from Enums.EventTypeEnum import EventTypeEnum
from datetime import datetime


class AcceptanceTestsReferee(TestCase):
    # Preparation
    team1 = Team('team1', [])
    team2 = Team('team2', [])
    main_referee = Referee(RefereeQualificationEnum.MAIN)
    referee = Referee(RefereeQualificationEnum.REGULAR)
    referee2 = Referee(RefereeQualificationEnum.MAIN)
    referee3 = Referee(RefereeQualificationEnum.REGULAR)

    def setUp(self):
        self.db = GameDB()
        self.match_controller = MatchController(self.db)
        self.match_controller.add_game(self.team1, self.team2, datetime(2020, 4, 23), '',
                                       [self.referee], self.main_referee)
        self.match_controller.add_game(self.team1, self.team2, datetime(2021, 4, 23), '', [],
                                       self.referee2)
        self.game_created = self.match_controller.get_game(self.team1, self.team2, datetime(2020, 4, 23))
        self.match_controller.start_game(self.game_created)
        self.match_controller.add_event(self.game_created, self.main_referee,
                                        EventTypeEnum.GOAL, 'Goal to home team', 90)

    # UC 10.2
    def test_watch_games(self):
        # --- Referee want to see future assigned games ---
        game_list = self.main_referee.show_ongoing_games_by_referee()
        self.assertEqual(game_list[0], self.game_created)

        # --- Referee want to see future assigned games without having any ---
        game_list = self.referee3.show_games_by_referee()
        self.assertEqual(len(game_list), 0)

    # UC 10.3
    def test_update_ongoing_game_events(self):
        # Referee get list of games to choose from
        game_list = self.main_referee.show_ongoing_games_by_referee()
        game_chosen = game_list[0]

        # Referee gets a list of game events to choose from
        game_events_list = game_chosen.events
        self.assertEqual(len(game_events_list), 1)
        game_event_chosen = game_events_list[0]

        # Update game event by user input
        self.assertEqual(self.match_controller.get_game(self.team1, self.team2, datetime(2020, 4, 23)).events[
                             0].event_description, 'Goal to home team')
        self.assertEqual(self.match_controller.get_game(self.team1, self.team2, datetime(2020, 4, 23)).events[
                             0].min_in_game, 90)
        self.referee_controller.edit_event(game_event_chosen, game_chosen, self.main_referee,
                                           EventTypeEnum.RED_CARD, 'Red card for Oscar', 20)
        self.assertEqual(self.match_controller.get_game(self.team1, self.team2, datetime(2020, 4, 23)).events[
                             0].event_description, 'Red card for Oscar')
        self.assertEqual(self.match_controller.get_game(self.team1, self.team2, datetime(2020, 4, 23)).events[
                             0].min_in_game, 20)

        # --- Referee trying to add game event to ongoing game without being assigned to one ---

        # Referee get list of games to choose from
        game_list = self.referee2.show_ongoing_games_by_referee()
        self.assertEqual(len(game_list), 0)

    # UC 10.4
    def test_update_finished_game_events(self):
        self.match_controller.end_game(self.game_created)

        # Main referee get list of games to choose from
        game_list = self.main_referee.show_games_by_referee()
        game_chosen = game_list[0]

        # Main referee gets a list of game events to choose from
        game_events_list = game_chosen.events
        self.assertEqual(len(game_events_list), 1)
        game_event_chosen = game_events_list[0]

        # Update game event by user input
        self.assertEqual(self.match_controller.get_game(self.team1, self.team2, datetime(2020, 4, 23)).events[
                             0].event_description, 'Goal to home team')
        self.assertEqual(self.match_controller.get_game(self.team1, self.team2, datetime(2020, 4, 23)).events[
                             0].min_in_game, 90)
        self.match_controller.edit_event(game_event_chosen, game_chosen, self.main_referee,
                                         EventTypeEnum.YELLOW_CARD, 'Yellow card for Shahar', 50)
        self.assertEqual(self.match_controller.get_game(self.team1, self.team2, datetime(2020, 4, 23)).events[
                             0].event_description, 'Yellow card for Shahar')
        self.assertEqual(self.match_controller.get_game(self.team1, self.team2, datetime(2020, 4, 23)).events[
                             0].min_in_game, 50)

        # --- Normal referee trying to edit finished game events ---

        # Referee get list of games to choose from
        game_list = self.referee.show_games_by_referee()
        self.assertEqual(len(game_list), 0)
