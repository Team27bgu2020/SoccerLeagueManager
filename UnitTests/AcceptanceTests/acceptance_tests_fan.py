from unittest import TestCase
from Service.SignedUserController import SignedUserController
from Service.PageController import PageController
from Service.MatchController import MatchController
from Service.ComplaintController import ComplaintController
from DataBases.UserDB import UserDB
from DataBases.PageDB import PageDB
from DataBases.GameDB import GameDB
from DataBases.ComplaintDB import ComplaintDB
from Domain.Fan import Fan
from Domain.Team import Team
from Domain.Game import Game
import datetime as date


class AcceptanceTestsFan(TestCase):
    # Preparation
    ip = '1.1.1.1'
    user_name = 'idan'
    password = '1234'
    name = 'idanAlbi'
    birth_date = date.datetime(1993, 1, 9)
    user_id = 111

    team1 = Team('Hapoel beer sheva', [])
    team2 = Team('Maccabi Tel Aviv', [])
    game = Game(team1, team2, date.datetime(2020, 4, 23), 'TernerStadium')

    def setUp(self):
        self.user_db = UserDB()
        self.user_controller = SignedUserController(self.user_db)
        self.user_controller.add_signed_user(self.user_name, self.password, self.name, self.birth_date, self.ip)

        self.fan = Fan(self.user_name, self.password, self.name, self.birth_date, self.ip, self.user_id)

        self.page_db = PageDB()
        self.page_controller = PageController(self.page_db)
        self.page_controller.add_page('MaorMelikson')

        self.game_db = GameDB()
        self.match_controller = MatchController(self.game_db)
        self.game_db.add(self.game)

        self.complaint_db = ComplaintDB()
        self.complaint_controller = ComplaintController(self.complaint_db)

    # UC 3.2
    def test_follow_page(self):
        # fan looks for the page MaorMelikson and the system retrieves it
        page = self.page_controller.search_personal_page('MaorMelikson')
        # fan follows the page
        self.fan.follow_page(page)
        self.assertEqual(page, self.fan.followed_pages[0])

        # the fan looks for the page GilSasover which is not in the page DB
        self.assertRaises(ValueError, self.page_controller.search_personal_page, 'GilSasover')

    # UC 3.3 -> game status is missing in order to check this UC
    def test_follow_game(self):
        # fan looks for a game to follow and the system retrieves it
        games = self.game_db.get_all_games()
        # fan follows the chosen game
        self.fan.follow_game(self.game_db.get(self.team1.name, self.team2.name, date.datetime(2020, 4, 23)))
        self.assertEqual(self.game, self.fan.followed_games[0])

    # UC 3.4
    def test_complain(self):
        # fan opens a complaint about incorrect data
        self.complaint_controller.new_complaint('RoniLevi page is not correct', self.fan)
        self.assertEqual(self.fan.complaints[0], self.complaint_controller.get_complaint(self.fan, 1))

        # fan wants to make a complaint without any description
        self.assertRaises(TypeError, self.complaint_controller.new_complaint, None, self.fan)

    # UC 3.5 -> no search history in fan yet
    def test_show_history(self):
        pass

    # UC 3.6
    def test_edit_personal_info(self):
        self.assertEqual(self.fan.user_name, 'idan')
        # fan wants to edit his personal information
        self.fan.edit_personal_data('new_user_name', 'new_pass', 'idan', self.birth_date)
        self.assertEqual(self.fan.user_name, 'new_user_name')
