from Domain.GameEvent import GameEvent
from DataBases.GameDB import GameDB
from Domain.Game import Game
from datetime import datetime
from Log.Logger import *


class MatchController:

    def __init__(self, game_db: GameDB):

        self.__game_DB = game_db
        Logger.start_logger()

    def add_game(self, home_team, away_team, match_time, field, referees=[], main_referee=None, user_id=""):
        try:
            game = Game(home_team, away_team, match_time, field)
            for referee in referees:
                game.add_referee(referee)
                referee.add_game(game)
            game.main_referee = main_referee
            main_referee.add_game(game)
            self.__game_DB.add(game)
            Logger.info_log("{0}:".format(user_id) + "Created new game between home:{0} and away:{1} ".format(home_team.name, away_team.name))
        except Exception as err:
            Logger.error_log("{0}:".format(user_id) + err.__str__())
            raise err

    def remove_game(self, game, user_id=""):
        try:
            self.__game_DB.delete(game)
            Logger.info_log("{0}:".format(user_id) + "Deleted game between home:{0} and away:{1} ".format(game.home_team.name, game.away_team.name))
        except Exception as err:
            Logger.error_log("{0}:".format(user_id) + err.__str__())
            raise err

    def get_game(self, team1, team2, date, user_id=""):
        try:
            return self.__game_DB.get(team1.name, team2.name, date)
        except Exception as err:
            Logger.error_log("{0}:".format(user_id) + err.__str__())
            raise err

    def all_games(self, user_id=""):
        try:
            return self.__game_DB.get_all_games()
        except Exception as err:
            Logger.error_log("{0}:".format(user_id) + err.__str__())
            raise err

    """ This function create and adds new game event """

    def add_event(self, game, referee, event_type, event_description, date, min_in_game, user_id=""):
        try:
            GameEvent(game, referee, event_type, event_description, date, min_in_game)
            Logger.info_log("{0}:".format(user_id) + "add event {0} in min {1} ".format(event_description, min_in_game))
        except Exception as err:
            Logger.error_log("{0}:".format(user_id) + err.__str__())
            raise err

    """ This function removes the game event """

    def remove_event(self, game_event: GameEvent, user_id=""):
        try:
            game = game_event.game
            referee = game_event.referee
            game.remove_event(game_event)
            referee.remove_event(game_event)
            Logger.info_log("{0}:".format(user_id) + "removed event {0} ".format(game_event.event_description))
        except Exception as err:
            Logger.error_log("{0}:".format(user_id) + err.__str__())
            raise err

    """ This function updates an event """

    def edit_event(self, game_event, game, referee, event_type, event_description, date, min_in_game, user_id=""):

        try:
            self.remove_event(game_event)
            self.add_event(game, referee, event_type, event_description, date, min_in_game)
            Logger.info_log("{0}:".format(user_id) + "edit event to {0} ".format(game_event.event_description))
        except Exception as err:
            Logger.error_log("{0}:".format(user_id) + err.__str__())
            raise err

    def start_game(self, game, user_id=""):
        try:
            check_time = datetime.now()
            if game.match_time.date() == check_time.date() and game.match_time.time() <= check_time.time():
                game.is_game_on = True
            Logger.info_log(
                "{0}:".format(user_id) + "started game between {0} and {1} at the {2} ".format(game.home_team.name,
                                                                                             game.away_team.name,
                                                                                             game.match_time))
        except Exception as err:
            Logger.error_log("{0}:".format(user_id) + err.__str__())
            raise err

    def end_game(self, game, user_id=""):
        try:
            game.is_game_on = False
            game.is_game_finished = True
            Logger.info_log("{0}:".format(user_id) + "ended game between {0} and {1} at the {2} ".format(game.home_team.name, game.away_team.name, game.match_time))
        except Exception as err:
            Logger.error_log("{0}:".format(user_id) + err.__str__())
            raise err
