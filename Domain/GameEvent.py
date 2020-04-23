# from Domain.ClassesTypeCheckImports import *
from Domain.Game import Game
from Domain.Referee import Referee
from Enums.EventTypeEnum import EventTypeEnum
import datetime as date
""" Dor """


class GameEvent:

    def __init__(self, game: Game, referee: Referee, event_type: EventTypeEnum, event_description: str,
                 datetime: date.datetime, min_in_game: int):

        self.__min_in_game = min_in_game
        self.__datetime = datetime
        self.__event_description = event_description
        self.__event_type = event_type
        self.__referee = referee
        self.__game = game

        self.__game.add_event(self)
        self.__referee.add_event(self)

    """ This method returns the game where the event has happened """

    @property
    def game(self):

        return self.__game

    """ This method returns the referee that called the event """

    @property
    def referee(self):

        return self.__referee

    """ This method returns the event type """

    @property
    def event_type(self):

        return self.__event_type

    """ This method returns the event description """

    @property
    def event_description(self):

        return self.__event_description

    """ This method returns the event date and time """

    @property
    def event_datetime(self):

        return self.__datetime

    """ This method return the event min in the game """

    @property
    def min_in_game(self):
        return self.__min_in_game

