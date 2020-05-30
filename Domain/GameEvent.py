# from Domain.ClassesTypeCheckImports import *
from Domain.Game import Game
from Domain.Referee import Referee
from Enums.EventTypeEnum import EventTypeEnum
from datetime import datetime
""" Dor """


class GameEvent:

    def __init__(self, event_id, game, referee, event_type: EventTypeEnum, event_description: str,
                 date: datetime, min_in_game: int):

        self.__event_id = event_id
        self.__min_in_game = min_in_game
        self.__datetime = date
        self.__event_description = event_description
        self.__event_type = event_type
        self.__referee = referee
        self.__game = game

    """ This method returns the event id"""

    @property
    def event_id(self):
        return self.__event_id

    """ This method sets the event id to the received value"""

    @event_id.setter
    def event_id(self, value):
        self.__event_id = value

    """ This method returns the game where the event has happened """

    @property
    def game(self):

        return self.__game

    @game.setter
    def game(self, value):
        self.__game = value

    """ This method returns the referee that called the event """

    @property
    def referee(self):

        return self.__referee

    @referee.setter
    def referee(self, value):
        self.__referee = value

    """ This method returns the event type """

    @property
    def event_type(self):

        return self.__event_type

    @event_type.setter
    def event_type(self, value):
        self.__event_type = value

    """ This method returns the event description """

    @property
    def event_description(self):

        return self.__event_description

    @event_description.setter
    def event_description(self, value):
        self.__event_description = value

    """ This method returns the event date and time """

    @property
    def event_datetime(self):

        return self.__datetime

    @event_datetime.setter
    def event_datetime(self, value):
        self.__datetime = value

    """ This method return the event min in the game """

    @property
    def min_in_game(self):
        return self.__min_in_game

    @min_in_game.setter
    def min_in_game(self, value):
        self.__min_in_game = value

