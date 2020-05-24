class NotificationController:

    """ Add fan to the followers list of a given game """
    def add_fan_follower_to_game(self, fan, game):
        game.add_follower(fan)

    """ Remove fan from the followers list of a certain game"""
    def remove_fan_follower_from_game(self, fan, game):
        game.remove_follower(fan)
