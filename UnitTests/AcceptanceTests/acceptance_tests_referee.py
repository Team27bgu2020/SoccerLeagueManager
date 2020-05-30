from unittest import TestCase

from Service.MatchController import MatchController
from Service.TeamManagementController import TeamManagementController
from Service.SignedUserController import SignedUserController

from DataBases.MongoDB.MongoGameDB import MongoGameDB
from DataBases.MongoDB.MongoUsersDB import MongoUserDB
from DataBases.MongoDB.MongoGameEventDB import MongoGameEventDB
from DataBases.MongoDB.MongoTeamDB import MongoTeamDB

from Domain.Team import Team
from Domain.Referee import Referee

from Enums.RefereeQualificationEnum import RefereeQualificationEnum
from Enums.EventTypeEnum import EventTypeEnum

from datetime import datetime


class AcceptanceTestsReferee(TestCase):
    # Preparation
    game_db = MongoGameDB()
    user_db = MongoUserDB()
    team_db = MongoTeamDB()
    game_event_db = MongoGameEventDB()

    match_controller = MatchController(game_db, user_db, game_event_db, team_db)
    team_controller = TeamManagementController(team_db, user_db)
    user_controller = SignedUserController(user_db)

    d_now = datetime.now()
    owner1 = None
    owner2 = None
    main_referee = None
    referee = None
    referee2 = None
    referee3 = None
    game1 = None
    game2 = None
    game_event = None

    def setUp(self):

        self.user_controller.add_team_owner('owner', '1234', 'owner', datetime.now())
        self.user_controller.add_team_owner('owner2', '1234', 'otherowner', datetime.now())
        self.owner1 = self.user_controller.get_user_by_name('owner')
        self.owner2 = self.user_controller.get_user_by_name('owner2')

        self.team_controller.open_new_team('team1', self.owner1.user_id)
        self.team_controller.open_new_team('team2', self.owner2.user_id)

        self.user_controller.add_referee(RefereeQualificationEnum.MAIN, 'S123', '12345678', 'Sas', datetime(1990, 8, 8))
        self.user_controller.add_referee(RefereeQualificationEnum.REGULAR, 'S12', '12345678', 'Sde', datetime(1990, 8, 8))
        self.user_controller.add_referee(RefereeQualificationEnum.MAIN, 'S13', '12345678', 'Swqed', datetime(1990, 8, 8))
        self.user_controller.add_referee(RefereeQualificationEnum.REGULAR, 'S23', '12345678', 'Saf', datetime(1990, 8, 8))

        self.main_referee = self.user_controller.get_user_by_name('S123')
        self.referee = self.user_controller.get_user_by_name('S12')
        self.referee2 = self.user_controller.get_user_by_name('S13')
        self.referee3 = self.user_controller.get_user_by_name('S23')

        self.match_controller.add_game('team1', 'team2', self.d_now, '', self.main_referee.user_id, [self.referee.user_id])
        self.game1 = self.match_controller.get_game(self.game_db.get_id_counter() - 1)
        self.match_controller.add_game('team1', 'team2', datetime(2021, 4, 23), '', self.referee2.user_id, [])
        self.game2 = self.match_controller.get_game(self.game_db.get_id_counter() - 1)

        self.match_controller.start_game(self.game1.game_id)
        self.match_controller.add_event(self.game1.game_id, self.main_referee.user_id, EventTypeEnum.GOAL,
                                        'Goal to home team', datetime(2020, 4, 4), 90)
        self.game_event = self.match_controller.get_event(self.game_event_db.get_id_counter()-1)

    def tearDown(self):

        self.match_controller.remove_event(self.game_event.event_id)
        self.match_controller.remove_game(self.game2.game_id)
        self.match_controller.remove_game(self.game1.game_id)
        self.user_controller.delete_signed_user(self.referee3.user_id)
        self.user_controller.delete_signed_user(self.referee2.user_id)
        self.user_controller.delete_signed_user(self.referee.user_id)
        self.user_controller.delete_signed_user(self.main_referee.user_id)
        self.team_controller.delete_team('team1')
        self.team_controller.delete_team('team2')
        self.user_controller.delete_signed_user(self.owner1.user_id)
        self.user_controller.delete_signed_user(self.owner2.user_id)

    # UC 10.2
    def test_watch_games(self):
        # --- Referee want to see future assigned games ---
        game_list = self.match_controller.show_ongoing_games_by_referee(self.main_referee.user_id)
        self.assertEqual(game_list[-1].game_id, self.game1.game_id)

        # --- Referee want to see future assigned games without having any ---
        game_list = self.match_controller.show_games_by_referee(self.referee3.user_id)
        self.assertEqual(len(game_list), 0)

    # UC 10.3
    def test_update_ongoing_game_events(self):

        # Referee get list of games to choose from
        game_list = self.match_controller.show_ongoing_games_by_referee(self.main_referee.user_id)
        game_chosen = game_list[0]

        # Referee gets a list of game events to choose from
        game_events_list = game_chosen.events
        self.assertEqual(len(game_events_list), 1)
        game_event_chosen = self.match_controller.get_event(game_events_list[0])

        # Update game event by user input
        self.match_controller.edit_event(game_event_chosen.event_id, event_description='Red card for Oscar', event_type=EventTypeEnum.RED_CARD, date=datetime.now(), min_in_game=20)

        self.assertEqual(self.match_controller.get_event(self.game_event.event_id).event_description, 'Red card for Oscar')
        self.assertEqual(self.match_controller.get_event(self.game_event.event_id).min_in_game, 20)

        # --- Referee trying to add game event to ongoing game without being assigned to one ---

        # Referee get list of games to choose from
        game_list = self.match_controller.show_ongoing_games_by_referee(self.referee2.user_id)
        self.assertEqual(len(game_list), 0)

    # UC 10.4
    def test_update_finished_game_events(self):
        self.match_controller.end_game(self.game1.game_id)

        # Main referee get list of games to choose from
        game_list = self.match_controller.show_games_by_referee(self.main_referee.user_id)
        game_chosen = game_list[0]

        # Main referee gets a list of game events to choose from
        game_events_list = game_chosen.events
        self.assertEqual(len(game_events_list), 1)
        game_event_chosen = self.match_controller.get_event(game_events_list[0])

        # Update game event by user input
        self.match_controller.edit_event(game_event_chosen.event_id, event_type=EventTypeEnum.YELLOW_CARD, event_description='Yellow card for Shahar', date=self.d_now, min_in_game=50)
        self.assertEqual(self.match_controller.get_event(game_event_chosen.event_id).event_description, 'Yellow card for Shahar')
        self.assertEqual(self.match_controller.get_event(game_event_chosen.event_id).min_in_game, 50)

        # --- Normal referee trying to edit finished game events ---

        # Referee get list of games to choose from
        game_list = self.match_controller.show_games_by_referee(self.referee.user_id)
        self.assertEqual(len(game_list), 0)
