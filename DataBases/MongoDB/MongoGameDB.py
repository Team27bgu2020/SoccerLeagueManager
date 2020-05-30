import pymongo
from pymongo import errors
from Domain.Game import Game
from datetime import datetime


class MongoGameDB:

    HOST = "mongodb://localhost"
    PORT = 27017
    DB = "SoccerLeagueManagerDB"
    GAMES_COLLECTION = "Games"
    COUNTERS_COLLECTION = "Counters"

    def __init__(self):
        """ Constructor for MongoUserDB """

        try:
            client = pymongo.MongoClient(self.HOST, self.PORT)
            self.__db = client[self.DB]
            self.__games_collection = self.__db[self.GAMES_COLLECTION]
            self.__counters_collection = self.__db[self.COUNTERS_COLLECTION]

        except errors.ConnectionFailure as err:
            raise ConnectionError("Connection Lost\n" + str(err))

    def add(self, game):

        if self.is_game_in_db(game.game_id):
            raise ValueError("Game with the same game id already exists")

        match_time_str = str(game.match_time.day) + '.' + \
                         str(game.match_time.month)+'.' + \
                         str(game.match_time.year)

        game_dict = game.__dict__

        game_dict.pop('_Game__match_time')
        game_dict['_Game__match_time'] = match_time_str

        self.__games_collection.insert_one(game_dict)

    def delete(self, game_id):

        if not self.is_game_in_db(game_id):
            raise ValueError("Game doesn't exists")

        query = {
            '_Game__game_id': game_id
        }

        self.__games_collection.delete_one(query)

    def get(self, game_id):

        if not self.is_game_in_db(game_id):
            raise ValueError("Game doesn't exists")

        query = {
            '_Game__game_id': game_id
        }

        game_dict = self.__games_collection.find_one(query)
        return self.game_dict_to_object(game_dict)

    def get_all(self):

        games = self.__games_collection.find()

        res = []

        for game in games:
            res.append(self.game_dict_to_object(game))

        return res

    def update(self, game):

        old_game = self.get(game.game_id)

        self.delete(game.game_id)

        try:
            self.add(game)
        except Exception as err:
            self.add(old_game)
            raise err

    def is_game_in_db(self, game_id):

        query = {
            '_Game__game_id': game_id
        }

        if self.__games_collection.find_one(query) is None:
            return False
        return True

    def game_dict_to_object(self, game_dict):

        match_time_str = game_dict['_Game__match_time']
        date_split = match_time_str.split('.')
        match_time_object = datetime(int(date_split[2]), int(date_split[1]), int(date_split[0]))

        game_object = Game(game_dict['_Game__game_id'], game_dict['_Game__home_team'], game_dict['_Game__away_team'], match_time_object, game_dict['_Game__field'])

        game_object.home_score = game_dict['_Game__home_score']
        game_object.away_score = game_dict['_Game__away_score']
        game_object.main_referee = game_dict['_Game__main_referee']
        game_object.referees = game_dict['_Game__referees']
        game_object.events = game_dict['_Game__events']
        game_object.is_game_on = game_dict['_Game__is_game_on']
        game_object.is_game_finished = game_dict['_Game__is_game_finished']
        game_object.fan_following = game_dict['fan_following']

        return game_object

    def update_id_counter(self, counter):

        curr_count = self.get_id_counter()

        query = {
            'game_counter': curr_count
        }

        new_values = {
            "$set": {"game_counter": counter}
        }

        self.__counters_collection.update_one(query, new_values)

    def get_id_counter(self):

        curr_counter = self.__counters_collection.distinct('game_counter')
        return curr_counter[0]

    def reset_db(self):

        self.__games_collection.drop()
        self.update_id_counter(1)

