class SeasonDB:

    def __init__(self):

        self.__seasons = {}

    """ This method adds a new season to the data base """

    def add(self, season):

        if season.year not in self.__seasons.keys():
            self.__seasons[season.year] = []

        self.__seasons[season.year].append(season)

    """ This method deletes a season from the data base """

    def delete(self, season):

        if season.year in self.__seasons.keys():
            self.__seasons[season.year].remove(season)

    """ This method returns the season in the given year """

    def get(self, year: int):

        if year in self.__seasons.keys():
            return self.__seasons[year]