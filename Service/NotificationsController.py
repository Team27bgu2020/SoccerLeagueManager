from Log.Logger import *


class NotificationController:

    Logger.start_logger()

    """ Add fan to the followers list of a given game """
    def add_fan_follower_to_game(self, fan, game, user_id=""):
        try:
            game.add_follower(fan)
            Logger.info_log("{0}: ".format(user_id) + "Add {0} to game ".format(fan.user_id))
        except Exception as err:
            Logger.error_log("{0}:".format(user_id) + err.__str__())
            raise err

    """ Remove fan from the followers list of a certain game"""
    def remove_fan_follower_from_game(self, fan, game, user_id=""):

        try:
            game.remove_follower(fan)
            Logger.info_log("{0}: ".format(user_id) + "Remove {0} from game ".format(fan.user_id))
        except Exception as err:
            Logger.error_log("{0}:".format(user_id) + err.__str__())
            raise err

    """ Checks if a given user has notifications waiting """
    def check_user_notifications(self, user, user_id=""):
        if len(user.notifications) == 0:
            return False
        return user.notifications.copy()