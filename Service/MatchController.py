from Domain.GameEvent import GameEvent
from DataBases.GameDB import GameDB


class MathController:

    def __init__(self, game_db):

        self.__game_DB = game_db

    """ This function create and adds new game event """

    def add_event(self, game, referee, event_type, event_description, datetime, min_in_game):
        GameEvent(game, referee, event_type, event_description, datetime, min_in_game)

    """ This function removes the game event """

    def remove_event(self, game_event: GameEvent):
        game = game_event.game
        referee = game_event.referee
        game.remove_event(game_event)
        referee.remove_event(game_event)

    """ This function updates an event """

    def edit_event(self, game_event, game, referee, event_type, event_description, datetime, min_in_game):
        self.remove_event(game_event)
        add_event(game, referee, event_type, event_description, datetime, min_in_game)
