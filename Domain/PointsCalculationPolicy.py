""" Dor """


class PointsCalculationPolicy:

    def __init__(self, win_points: int, tie_points: int, lose_points: int):

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


