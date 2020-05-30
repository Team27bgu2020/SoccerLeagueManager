from Enums.GameAssigningPoliciesEnum import GameAssigningPoliciesEnum
""" Dor """


class GameSchedulePolicy:

    def __init__(self, team_games_num: int, games_per_week: int, games_stadium_assigning: GameAssigningPoliciesEnum):

        if type(team_games_num) is not int:
            raise TypeError
        if team_games_num < 0:
            raise ValueError

        self.__team_games_num = team_games_num
        self.__games_per_week = games_per_week
        self.__games_stadium_assigning_policy = games_stadium_assigning

    """ Getter for the number of games that each team plays in the current policy against each of the other teams """

    @property
    def team_games_num(self):

        return self.__team_games_num

    """ Getter for the assignment stadium games policy """

    @property
    def team_stadium_assignment_policy(self):

        return self.__games_stadium_assigning_policy

    """ Getter for the number of games per week """

    @property
    def games_per_week(self):

        return self.__games_per_week

    """ Getter for the desired week days (sunday, monday, ...) for the games """

    # @property
    # def chosen_days(self):
    #
    #     return self.__chosen_days

    """ This method checks if 2 Policies are the same """

    def __eq__(self, other):

        if self.team_games_num != other.team_games_num or \
                self.games_per_week != other.games_per_week or \
                self.team_stadium_assignment_policy != other.team_stadium_assignment_policy:
                # len(self.chosen_days) != len(other.chosen_days):
            return False

        # for day in self.chosen_days:
        #     if day not in other.chosen_days:
        #         return False

        return True


