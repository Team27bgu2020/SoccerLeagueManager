# from Domain.ClassesTypeCheckImports import *
from Domain.League import League
""" Dor """


class Season:

    def __init__(self, year: int):

        if type(year) is not int:
            raise TypeError

        self.__year = year
        self.__leagues = []

    """ This method adds a new league to the season """

    def add_league(self, league):

        if league in self.__leagues:
            raise ValueError('League is already in this season')

        self.__leagues.append(league)

    """ This method adds a new league to the season """

    def add_leagues(self, leagues):

        exception = ''

        for league in leagues:
            try:
                self.add_league(league)
            except Exception as err:
                exception = exception + str(err) + '\n'

        if exception is not '':
            raise ValueError(exception)

    """ This method removes the given league from the season """

    def remove_league(self, league):

        if league in self.__leagues:
            self.__leagues.remove(league)
        else:
            raise ValueError('League is not in this season')

    """ This methods returns the seasons year """

    @property
    def year(self):

        return self.__year

    """ This method returns the seasons leagues """

    @property
    def leagues(self):

        return self.__leagues
