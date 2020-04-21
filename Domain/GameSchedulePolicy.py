from Domain.ClassesTypeCheckImports import *


""" Dor """


class GameSchedulePolicy:

    def __init__(self, team_games_num, games_stadium_assigning_policy):

        if type(team_games_num) is not int:
            raise TypeError
        if team_games_num < 0:
            raise ValueError

        self.__team_games_num = team_games_num
        self.__games_stadium_assigning_policy = games_stadium_assigning_policy

    """ Getter for the number of games that each team plays in the current policy """

    @property
    def team_games_num(self):

        return self.__team_games_num

    """ Getter for the assignment stadium games policy """

    @property
    def team_stadium_assignment_policy(self):

        return self.__games_stadium_assigning_policy


def type_check(obj):
    if type(obj) is not GameSchedulePolicy:
        raise TypeError
