import Domain.League as League


class Season:

    def __init__(self, year):

        if type(year) is not int:
            raise TypeError

        self._year = year
        self._leagues = []

    """ This method adds a new league to the season """

    def add_league(self, league):

        League.type_check(league)
        if league in self._leagues:
            raise ValueError

        self._leagues.append(league)

    """ This method removes the given league from the season """

    def remove_league(self, league):

        League.type_check(league)
        self._leagues.remove(league)

    """ This methods returns the seasons year """

    def get_year(self):

        return self._year

    """ This method returns the seasons leagues """

    def get_leagues(self):

        return self._leagues



def type_check(obj):

    if type(obj) is not Season:
        raise TypeError