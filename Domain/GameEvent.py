import Domain.Game as Game
import Domain.Referee as Referee


class GameEvent:

    def __init__(self, game, referee, event_type, event_description, datetime, min_in_game):
        Game.type_check(game)
        Referee.type_check(referee)

        # add argument check

        self.__min_in_game = min_in_game
        self.__datetime = datetime
        self.__event_description = event_description
        self.__event_type = event_type
        self.__referee = referee
        self.__game = game

        self.__game.add_event(self)
        self.__referee.add_event(self)

    """ This method returns the game where the event has happened """

    def get_game(self):

        return self.__game

    """ This method returns the referee that called the event """

    def get_referee(self):

        return self.__referee

    """ This method returns the event type """

    def get_event_type(self):

        return self.__event_type

    """ This method returns the event description """

    def get_event_description(self):

        return self.__event_description

    """ This method returns the event date and time """

    def get_event_datetime(self):

        return self.__datetime

    """ This method return the event min in the game """

    def get_min_in_game(self):
        return self.__min_in_game


def type_check(obj):
    if type(obj) is not GameEvent:
        raise TypeError
