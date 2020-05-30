from Domain.GameEvent import GameEvent
from DataBases.GameDB import GameDB
from DataBases.MongoDB.MongoUsersDB import MongoUserDB
from Domain.Game import Game
from datetime import datetime
from Log.Logger import *


class MatchController:

    def __init__(self, game_db, user_db, game_event_db, team_db):
        self.__user_DB = user_db
        self.__game_DB = game_db
        self.__game_event_DB = game_event_db
        self.__team_DB = team_db
        self.__game_id_counter = self.__game_DB.get_id_counter()
        self.__game_event_id_counter = self.__game_event_DB.get_id_counter()
        Logger.start_logger()

    def add_game(self, home_team_name, away_team_name, match_time, field, main_referee_id, referees=[], user_id=""):
        try:
            home_team = self.__team_DB.get(home_team_name)
            away_team = self.__team_DB.get(away_team_name)
            # Checking for collision

            self.collision_game_check(home_team, match_time)
            self.collision_game_check(away_team, match_time)

            game = Game(self.__game_id_counter, home_team.name, away_team.name, match_time, field)

            home_team.add_game(game.game_id)
            away_team.add_game(game.game_id)

            for referee_id in referees:
                referee = self.__user_DB.get_signed_user(referee_id)
                game.add_referee(referee.user_id)
                referee.add_game(game.game_id)
                self.__user_DB.update_signed_user(referee)
            main_referee = self.__user_DB.get_signed_user(main_referee_id)
            game.main_referee = main_referee.user_id
            main_referee.add_game(game.game_id)

            self.__game_DB.add(game)
            self.update_game_counter()
            self.__team_DB.update(home_team)
            self.__team_DB.update(away_team)
            self.__user_DB.update_signed_user(main_referee)

            Logger.info_log("{0}:".format(user_id) + "Created new game between home:{0} and away:{1} ".format(home_team.name, away_team.name))
        except Exception as err:
            Logger.error_log("{0}:".format(user_id) + err.__str__())
            raise err

    def collision_game_check(self, team, game_time):
        for game_id in team.upcoming_games:
            game = self.__game_DB.get(game_id)
            if game.match_time.date() == game_time.date():
                raise ValueError('The game has collision with another team game')

    def remove_game(self, game_id, user_id=""):
        try:
            self.__game_DB.delete(game_id)
            Logger.info_log("{0}:".format(user_id) + "Deleted game {} ".format(game_id))
        except Exception as err:
            Logger.error_log("{0}:".format(user_id) + err.__str__())
            raise err

    def get_game(self, game_id, user_id=""):
        try:
            return self.__game_DB.get(game_id)
        except Exception as err:
            Logger.error_log("{0}:".format(user_id) + err.__str__())
            raise err

    def all_games(self, user_id=""):
        try:
            return self.__game_DB.get_all()
        except Exception as err:
            Logger.error_log("{0}:".format(user_id) + err.__str__())
            raise err

    """ This function create and adds new game event """

    def add_event(self, game_id, referee_id, event_type, event_description, date, min_in_game, user_id=""):
        try:
            event = GameEvent(self.__game_event_id_counter, game_id, referee_id, event_type, event_description, date, min_in_game)

            game = self.__game_DB.get(game_id)

            if referee_id not in game.referees and referee_id != game.main_referee:
                raise ValueError('{}: User is not a referee in this game')

            game.add_event(event.event_id)
            self.__game_DB.update(game)

            referee = self.__user_DB.get_signed_user(referee_id)
            referee.add_event(event.event_id)
            self.__user_DB.update_signed_user(referee)

            self.__game_event_DB.add(event)
            self.update_game_event_counter()
            self.notify_followers(game, '{} just added as game event by referee {}'.
                                  format(event.event_type, referee.name))
            Logger.info_log("{0}:".format(user_id) + "add event {0} in min {1} ".format(event_description, min_in_game))
        except Exception as err:
            game.remove_event(event.event_id)
            referee.remove_event(event.event_id)
            self.__user_DB.update_signed_user(referee)
            self.__game_DB.update(game)
            Logger.error_log("{0}:".format(user_id) + err.__str__())
            raise err

    """ This function removes the game event """

    def remove_event(self, game_event_id, user_id=""):
        try:
            game_event = self.__game_event_DB.get(game_event_id)
            game_id = game_event.game
            referee_id = game_event.referee
            game = self.__game_DB.get(game_id)
            referee = self.__user_DB.get_signed_user(referee_id)
            game.remove_event(game_event.event_id)
            referee.remove_event(game_event.event_id)
            self.__game_DB.update(game)
            self.__user_DB.update_signed_user(referee)
            self.__game_event_DB.delete(game_event_id)
            Logger.info_log("{0}:".format(user_id) + "removed event {0} ".format(game_event.event_description))
        except Exception as err:
            Logger.error_log("{0}:".format(user_id) + err.__str__())
            raise err

    def get_event(self, game_event_id, user_id=""):
        game_event = self.__game_event_DB.get(game_event_id)
        Logger.info_log("{}: Asked for game event {}".format(user_id, game_event_id))
        return game_event

    """ This function updates an event """

    def edit_event(self, game_event_id, event_type=None, event_description=None, date=None, min_in_game=None, referee_id=None, user_id=""):

        try:
            game_event = self.__game_event_DB.get(game_event_id)

            if referee_id is not None:
                game_event.referee = referee_id
            if event_type is not None:
                game_event.event_type = event_type
            if event_description is not None:
                game_event.event_description = event_description
            if date is not None:
                game_event.event_datetime = date
            if min_in_game is not None:
                game_event.min_in_game = min_in_game

            self.__game_event_DB.update(game_event)
            Logger.info_log("{0}:".format(user_id) + "edited event {0} ".format(game_event_id))
        except Exception as err:
            Logger.error_log("{0}:".format(user_id) + err.__str__())
            raise err

    def start_game(self, game_id, user_id=""):
        try:
            game = self.__game_DB.get(game_id)
            check_time = datetime.now()
            if game.match_time.date() == check_time.date() and game.match_time.time() <= check_time.time():
                game.is_game_on = True
                self.__game_DB.update(game)
                Logger.info_log(
                    "{0}:".format(user_id) + "started game between {0} and {1} at the {2} ".format(game.home_team,
                                                                                               game.away_team,
                                                                                               game.match_time))
        except Exception as err:
            Logger.error_log("{0}:".format(user_id) + err.__str__())
            raise err

    def end_game(self, game_id, user_id=""):
        try:
            game = self.__game_DB.get(game_id)
            game.is_game_on = False
            game.is_game_finished = True
            self.__game_DB.update(game)
            Logger.info_log("{0}:".format(user_id) + "ended game between team {0} and team {1} at the {2} "
                            .format(game.home_team, game.away_team, game.match_time))

        except Exception as err:
            Logger.error_log("{0}:".format(user_id) + err.__str__())
            raise err

    def edit_game(self, game_id, home_team=None, away_team=None, match_time=None, field=None, referees=None, main_referee=None, user_id=""):

        try:
            is_match_time_changed = True
            is_field_changed = True

            old_game = self.__game_DB.get(game_id)
            if home_team is None:
                home_team = old_game.home_team
            if away_team is None:
                away_team = old_game.away_team
            if match_time is None or match_time == old_game.match_time:
                match_time = old_game.match_time
                is_match_time_changed = False
            if field is None or field == old_game.field:
                field = old_game.field
                is_field_changed = False
            if referees is None:
                referees = old_game.referees
            if main_referee is None:
                main_referee = old_game.main_referee

            new_game = Game(game_id, home_team, away_team, match_time, field)
            new_game.referees = referees
            new_game.main_referee = main_referee

            self.__game_DB.delete(game_id)
            self.__game_DB.add(new_game)

            if is_match_time_changed:
                self.notify_referees(new_game, 'Game date and time changed to {}'.format(match_time))
            if is_field_changed:
                self.notify_referees(new_game, 'Game location changed to {} field'.format(field))

        except Exception as err:
            try:
                self.__game_DB.get(game_id)
                self.__game_DB.delete(game_id)
                self.__game_DB.add(old_game)
            except ValueError as err2:
                self.__game_DB.add(old_game)
            finally:
                Logger.error_log('{}:' + str(err))

    def add_referee_to_game(self, game_id, referee_id, user_id=""):

        try:
            game = self.__game_DB.get(game_id)
            game.add_referee(referee_id)

            referee = self.__user_DB.get_signed_user(referee_id)
            referee.add_game(game_id)

            self.notify_followers(game, '{} added as a referee to {}-{} game'
                                  .format(referee.name, game.home_team, game.away_team))

            self.__game_DB.update(game)
            self.__user_DB.update_signed_user(referee)

        except Exception as err:
            Logger.error_log('{}:'.format(user_id) + str(err))
            raise err

    def remove_referee_from_game(self, game_id, referee_id, user_id=""):

        try:
            game = self.__game_DB.get(game_id)
            game.remove_referee(referee_id)

            referee = self.__user_DB.get_signed_user(referee_id)
            referee.remove_game(game_id)

            self.notify_followers(game, '{} removed as a referee from {}-{} game'.
                                  format(referee.name, game.home_team, game.away_team))

            self.__game_DB.update(game)
            self.__user_DB.update_signed_user(referee)

        except Exception as err:
            Logger.error_log('{}:'.format(user_id) + str(err))
            raise err

    def show_games_by_referee(self, referee_id):

        result = []
        referee = self.__user_DB.get_signed_user(referee_id)
        for game_id in referee.referee_in_games:
            game = self.__game_DB.get(game_id)
            if (referee.user_id in game.referees and not game.is_game_finished) or referee.user_id == game.main_referee:
                result.append(game)
        return result

    def show_ongoing_games_by_referee(self, referee_id):

        referee_games = self.show_games_by_referee(referee_id)
        result = []
        for game in referee_games:
            if game.is_game_on:
                result.append(game)
        return result

    """ Notify all followers about game notification """
    def notify_followers(self, game, notification):
        for follower_id in game.fan_following:
            follower = self.__user_DB.get_signed_user(follower_id)
            follower.notify(notification)
            self.__user_DB.update_signed_user(follower)

    """ Notify referees about given notification """
    def notify_referees(self, game, notification):
        for referee_id in game.referees:
            referee = self.__user_DB.get_signed_user(referee_id)
            referee.notify(notification)
            self.__user_DB.update_signed_user(referee)

        main_referee = self.__user_DB.get_signed_user(game.main_referee)
        main_referee.notify(notification)
        self.__user_DB.update_signed_user(main_referee)

    def update_game_counter(self):
        self.__game_id_counter += 1
        self.__game_DB.update_id_counter(self.__game_id_counter)

    def update_game_event_counter(self):
        self.__game_event_id_counter += 1
        self.__game_event_DB.update_id_counter(self.__game_event_id_counter)

