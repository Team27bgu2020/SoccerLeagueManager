from enum import Enum


""" Enum for possible policies for assigning the stadium for the games """


class EventTypeEnum(Enum):
    GOAL = 'Goal'
    YELLOW_CARD = 'Yellow card'
    RED_CARD = 'Red Card'