import pymongo
from pymongo import errors

from Domain.Season import Season

class MongoSeasonDB:

    HOST = "mongodb://localhost"
    PORT = 27017
    DB = "SoccerLeagueManagerDB"
    SEASONS_COLLECTION = "Seasons"

    def __init__(self):
        """ Constructor for MongoUserDB """

        try:
            client = pymongo.MongoClient(self.HOST, self.PORT)
            self.__db = client[self.DB]
            self.__seasons_collection = self.__db[self.SEASONS_COLLECTION]

        except errors.ConnectionFailure as err:
            raise ConnectionError("Connection Lost\n" + str(err))

    def add(self, season):

        if self.is_season_in_db(season.year):
            raise ValueError("Season with the same season id already exists")

        season_dict = season.__dict__

        self.__seasons_collection.insert_one(season_dict)

    def delete(self, season_year):

        if not self.is_season_in_db(season_year):
            raise ValueError("Season doesn't exist")

        query = {
            '_Season__year': season_year
        }

        self.__seasons_collection.delete_one(query)

    def get(self, season_year):

        if not self.is_season_in_db(season_year):
            raise ValueError("Season doesn't exist")

        query = {
            '_Season__year': season_year
        }

        season_dict = self.__seasons_collection.find_one(query)

        return self.season_dict_to_object(season_dict)

    def get_all_seasons(self):

        seasons = self.__seasons_collection.find()

        res = []

        for season in seasons:
            res.append(self.season_dict_to_object(season))

        return res

    def update(self, season):

        old_season = self.get(season.year)
        self.delete(season.year)

        try:
            self.add(season)
        except Exception as err:
            self.add(old_season)
            raise err

    def season_dict_to_object(self, season_dict):

        season = Season(season_dict['_Season__year'])
        season.leagues = season_dict['_Season__leagues']
        return season

    def is_season_in_db(self, season_year):

        query = {
            '_Season__year': season_year
        }

        if self.__seasons_collection.find_one(query) is None:
            return False
        return True

    def reset_db(self):

        self.__seasons_collection.drop()
