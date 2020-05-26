# noinspection PyMethodMayBeStatic
class NotificationController:

    """ Add fan to the followers list of a given game """
    def add_fan_follower_to_game(self, fan, game):
        game.add_follower(fan)
        fan.follow_game(game)

    """ Remove fan from the followers list of a certain game"""
    def remove_fan_follower_from_game(self, fan, game):
        game.remove_follower(fan)
        fan.unfollow_game(game)

    """ Checks if a given user has notifications waiting """
    def check_user_notifications(self, user):
        if len(user.notifications) == 0:
            return False
        return user.notifications.copy()

    def clear_seen_notifications_from_user(self, user, notifications):
        for notification in user.notifications:
            if notification in notifications:
                user.notifications.remove(notification)
