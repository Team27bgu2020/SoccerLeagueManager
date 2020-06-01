from unittest import TestCase
from Service.SignedUserController import SignedUserController
from Service.PageController import PageController
from Service.MatchController import MatchController
from Service.ComplaintController import ComplaintController
from Service.TeamManagementController import TeamManagementController
from Service.NotificationsController import NotificationController
from DataBases.MongoDB.MongoUsersDB import MongoUserDB
from DataBases.MongoDB.MongoPageDB import MongoPageDB
from DataBases.MongoDB.MongoGameDB import MongoGameDB
from DataBases.MongoDB.MongoComplaintDB import MongoComplaintDB
from DataBases.MongoDB.MongoGameEventDB import MongoGameEventDB
from DataBases.MongoDB.MongoTeamDB import MongoTeamDB
from Domain.Fan import Fan
from Domain.Team import Team
from Domain.Game import Game
import datetime as date
from Enums.RefereeQualificationEnum import RefereeQualificationEnum


class AcceptanceTestsFan(TestCase):

    # Preparation

    user_db = MongoUserDB()
    user_controller = SignedUserController(user_db)
    page_db = MongoPageDB()
    page_controller = PageController(page_db)
    game_db = MongoGameDB()
    game_event_db = MongoGameEventDB()
    team_db = MongoTeamDB()
    team_controller = TeamManagementController(team_db, user_db)
    match_controller = MatchController(game_db, user_db, game_event_db, team_db)
    complaint_db = MongoComplaintDB()
    complaint_controller = ComplaintController(complaint_db, user_db)
    notification_controller = NotificationController(user_db, game_db)

    team_owner1 = None
    team_owner2 = None
    referee = None
    fan = None
    game = None
    page = None
    team1 = None
    team2 = None

    def setUp(self):

        self.user_controller.add_team_owner('owner', '1234', 'name', date.datetime.now())
        self.user_controller.add_team_owner('owner2', '1234', 'othername', date.datetime.now())
        self.user_controller.add_referee(RefereeQualificationEnum.MAIN, 'referee', '1234', 'referee', date.datetime.now())

        self.team_owner1 = self.user_controller.get_user_by_name('owner')
        self.team_owner2 = self.user_controller.get_user_by_name('owner2')
        self.referee = self.user_controller.get_user_by_name('referee')

        self.team_controller.open_new_team('Hapoel beer sheva', self.team_owner1.user_id)
        self.team_controller.open_new_team('Maccabi Tel Aviv', self.team_owner2.user_id)

        self.match_controller.add_game('Hapoel beer sheva', 'Maccabi Tel Aviv', date.datetime(2020, 4, 23), "", self.referee.user_id)
        self.game = self.match_controller.get_game(self.game_db.get_id_counter()-1)

        self.user_controller.add_fan('fan', '1234', 'fan', date.datetime(2020, 4, 23))
        self.fan = self.user_controller.get_user_by_name('fan')

        self.page_controller.add_page('MaorMelikson')
        self.page = self.page_controller.get_page(self.page_db.get_id_counter()-1)

    def tearDown(self):

        self.team_controller.delete_team('Hapoel beer sheva')
        self.team_controller.delete_team('Maccabi Tel Aviv')
        self.user_controller.delete_signed_user(self.fan.user_id)
        self.match_controller.remove_game(self.game.game_id)
        self.page_controller.remove_page(self.page.page_id)
        self.user_controller.delete_signed_user(self.team_owner1.user_id)
        self.user_controller.delete_signed_user(self.team_owner2.user_id)
        self.user_controller.delete_signed_user(self.referee.user_id)


    # UC 3.2
    # TODO: Implement and test
    # def test_follow_page(self):
    #     # fan looks for the page MaorMelikson and the system retrieves it
    #     page = self.page_controller.search_personal_page('MaorMelikson')
    #     # fan follows the page
    #     self.fan.follow_page(page.page_id)
    #     self.assertEqual(page.page_id, self.fan.followed_pages[0])
    #
    #     # the fan looks for the page GilSasover which is not in the page DB
    #     self.assertRaises(ValueError, self.page_controller.search_personal_page, 'GilSasover')

    # UC 3.3 -> game status is missing in order to check this UC
    def test_follow_game(self):
        # fan looks for a game to follow and the system retrieves it
        games = self.match_controller.all_games()
        self.assertEqual(1, len(games))

        # fan follows the chosen game
        self.notification_controller.add_fan_follower_to_game(self.fan.user_id, self.game.game_id)

        # trying to follow same game twice
        self.assertRaises(ValueError, self.notification_controller.add_fan_follower_to_game, self.fan.user_id, self.game.game_id)

        self.fan = self.user_controller.get_user_by_id(self.fan.user_id)
        self.assertEqual(self.game.game_id, self.fan.followed_games[0])

    # UC 3.4
    def test_complain(self):

        self.complaint_controller.new_complaint('RoniLevi page is not correct', self.fan.user_id)
        self.fan = self.user_controller.get_user_by_id(self.fan.user_id)
        self.assertEqual(self.fan.complaints[0], self.complaint_db.get_id_counter()-1)

    # UC 3.5 -> no search history in fan yet
    def test_show_history(self):
        pass

    # UC 3.6
    def test_edit_personal_info(self):

        # fan wants to edit his personal information
        self.user_controller.edit_personal_data(self.fan.user_id, 'new_user_name', 'new_pass', 'idan', date.datetime(2000, 1, 1))
        self.fan = self.user_controller.get_user_by_id(self.fan.user_id)
        self.assertEqual(self.fan.user_name, 'new_user_name')
        self.assertEqual(self.fan.name, 'idan')
        self.assertEqual(self.fan.birth_date, date.datetime(2000, 1, 1))
