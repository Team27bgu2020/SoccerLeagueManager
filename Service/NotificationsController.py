from Log.Logger import *


# noinspection PyMethodMayBeStatic
class NotificationController:

    Logger.start_logger()

    def __init__(self, user_db, game_db):
        self.__user_DB = user_db
        self.__game_DB = game_db


    """ Add fan to the followers list of a given game """
    def add_fan_follower_to_game(self, fan_id, game_id, user_id=""):
        try:
            fan = self.__user_DB.get_signed_user(fan_id)
            game = self.__game_DB.get(game_id)
            game.add_follower(fan_id)
            fan.follow_game(game_id)
            self.__user_DB.update_signed_user(fan)
            self.__game_DB.update(game)
            Logger.info_log("{0}: ".format(user_id) + "Add {0} to game ".format(fan.user_id))
        except Exception as err:
            Logger.error_log("{0}:".format(user_id) + err.__str__())
            raise err

    """ Remove fan from the followers list of a certain game"""
    def remove_fan_follower_from_game(self, fan_id, game_id, user_id=""):

        try:
            fan = self.__user_DB.get_signed_user(fan_id)
            game = self.__game_DB.get(game_id)
            game.remove_follower(fan_id)
            fan.unfollow_game(game_id)
            self.__user_DB.update_signed_user(fan)
            self.__game_DB.update(game)
            Logger.info_log("{0}: ".format(user_id) + "Remove {0} from game ".format(fan.user_id))
        except Exception as err:
            Logger.error_log("{0}:".format(user_id) + err.__str__())
            raise err

    """ Checks if a given user has notifications waiting """
    def check_user_notifications(self, to_check_user_id, user_id=""):
        user = self.__user_DB.get_signed_user(to_check_user_id)
        if len(user.notifications) == 0:
            return False
        notifications = user.notifications.copy()
        self.clear_seen_notifications_from_user(user, notifications)
        self.__user_DB.update_signed_user(user)
        return notifications

    def clear_seen_notifications_from_user(self, user, notifications):
        for notification in user.notifications:
            if notification in notifications:
                user.notifications.remove(notification)
