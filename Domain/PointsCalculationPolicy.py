""" Dor """


class PointsCalculationPolicy:

    def __init__(self, win_points: int, tie_points: int, lose_points: int, policy_id):

        self.__policy_id = policy_id
        self.__win_points = win_points
        self.__tie_points = tie_points
        self.__lose_points = lose_points

    """ Getter for win points """

    @property
    def win_points(self):

        return self.__win_points

    """ Getter for tie points """

    @property
    def tie_points(self):

        return self.__tie_points

    """ Getter for lose points """

    @property
    def lose_points(self):

        return self.__lose_points

    @property
    def policy_id(self):
        return self.__policy_id

    """ This method checks if 2 Policies are the same """

    def __eq__(self, other):

        if self.win_points != other.win_points or \
                self.lose_points != other.lose_points or \
                self.tie_points != other.tie_points:
            return False

        return True