
class LeagueDB:

    def __init__(self):

        self.__leagues = {}

    """ This method adds a new league to the data base """

    def add(self, league):

        if league.season.year not in self.__leagues.keys():
            self.__leagues[league.season.year] = []

        for l in self.__leagues[league.season.year]:
            if league.name == l.name:
                raise ValueError

        self.__leagues[league.season.year].append(league)

    """ This method deletes a league from the data base """

    def delete(self, league):

        if league.season.year in self.__leagues.keys():
            self.__leagues[league.season.year].remove(league)

    """ This method returns all the leagues in the same season """

    def get_leagues_by_season(self, year: int):

        if year not in self.__leagues.keys():
            return []

        return self.__leagues[year]

    """ This method returns the league in the given season year """

    def get(self, league_name: str, year: int):

        for league in self.get_leagues_by_season(year):
            if league.name == league_name:
                return league
