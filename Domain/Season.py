import Domain.League as League


class Season:

    def __init__(self, year):

        if type(year) is not int:
            raise TypeError

        self.__year = year
        self.__leagues = []

    """ This method adds a new league to the season """

    def add_league(self, league):

        League.type_check(league)
        if league in self.__leagues:
            raise ValueError

        self.__leagues.append(league)

    """ This method removes the given league from the season """

    def remove_league(self, league):

        League.type_check(league)
        self.__leagues.remove(league)

    """ This methods returns the seasons year """

    @property
    def year(self):

        return self.__year

    """ This method returns the seasons leagues """

    @property
    def leagues(self):

        return self.__leagues


def type_check(obj):

    if type(obj) is not Season:
        raise TypeError