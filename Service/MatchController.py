from Domain.GameEvent import GameEvent
from DataBases.GameDB import GameDB
from Domain.Game import Game
from datetime import datetime


class MatchController:

    def __init__(self, game_db: GameDB):

        self.__game_DB = game_db

    def add_game(self, home_team, away_team, match_time, field, referees=[], main_referee=None):
        game = Game(home_team, away_team, match_time, field)
        for referee in referees:
            game.add_referee(referee)
            referee.add_game(game)
        game.main_referee = main_referee
        main_referee.add_game(game)
        self.__game_DB.add(game)

    def remove_game(self, game):
        self.__game_DB.delete(game)

    def get_game(self, team1, team2, date):
        return self.__game_DB.get(team1.name, team2.name, date)

    def all_games(self):
        return self.__game_DB.get_all_games()

    """ This function create and adds new game event """

    def add_event(self, game, referee, event_type, event_description, min_in_game):
        GameEvent(game, referee, event_type, event_description, min_in_game)

    """ This function removes the game event """

    def remove_event(self, game_event: GameEvent):
        game = game_event.game
        referee = game_event.referee
        game.remove_event(game_event)
        referee.remove_event(game_event)

    """ This function updates an event """

    def edit_event(self, game_event, game, referee, event_type, event_description, min_in_game):
        self.remove_event(game_event)
        self.add_event(game, referee, event_type, event_description, min_in_game)

    def start_game(self, game):
        check_time = datetime.now()
        if game.match_time.date() == check_time.date() and game.match_time.time() <= check_time.time():
            game.is_game_on = True

    def end_game(self, game):
        game.is_game_on = False
        game.is_game_finished = True

