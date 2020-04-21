""" Dor """


class PointsCalculationPolicy:

    def __init__(self, win_points, tie_points, lose_points):

        if type(win_points) or type(tie_points) or type(lose_points) is not int:
            raise TypeError

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

def type_check(obj):
    if type(obj) is not PointsCalculationPolicy:
        raise TypeError
