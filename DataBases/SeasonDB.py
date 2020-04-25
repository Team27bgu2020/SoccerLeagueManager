class SeasonDB:

    def __init__(self):

        self.__seasons = {}

    """ This method adds a new season to the data base """

    def add(self, season):

        if season.year in self.__seasons.keys():
            raise ValueError

        self.__seasons[season.year] = season

    """ This method deletes a season from the data base """

    def delete(self, season):

        if season.year in self.__seasons.keys():
            del self.__seasons[season.year]

    """ This method returns the season in the given year """

    def get(self, year: int):

        if year in self.__seasons.keys():
            return self.__seasons[year]