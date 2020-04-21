from enum import Enum


""" Enum for possible policies for assigning the stadium for the games """


class RefereeQualificationEnum(Enum):
    MAIN = 'Main'
    REGULAR = 'Regular'


def type_check(obj):

    if not isinstance(obj, RefereeQualificationEnum):
        raise TypeError


