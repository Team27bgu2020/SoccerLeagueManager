import pymongo
from pymongo import errors

from Domain.GameEvent import GameEvent
from Enums.EventTypeEnum import EventTypeEnum
from datetime import datetime


class MongoGameEventDB:

    HOST = "mongodb://localhost"
    PORT = 27017
    DB = "SoccerLeagueManagerDB"
    GAME_EVENTS_COLLECTION = "GameEvents"
    COUNTERS_COLLECTION = "Counters"

    def __init__(self):
        """ Constructor for MongoUserDB """

        try:
            client = pymongo.MongoClient(self.HOST, self.PORT)
            self.__db = client[self.DB]
            self.__game_event_collection = self.__db[self.GAME_EVENTS_COLLECTION]
            self.__counters_collection = self.__db[self.COUNTERS_COLLECTION]

        except errors.ConnectionFailure as err:
            raise ConnectionError("Connection Lost\n" + str(err))

    def add(self, game_event):

        if self.is_game_event_in_db(game_event.event_id):
            raise ValueError("Game Event with the same id already exists")

        date_str = str(game_event.event_datetime.day) + '.' + str(game_event.event_datetime.month) + '.' + str(game_event.event_datetime.year)

        event_type_str = game_event.event_type.name

        game_event_dict = game_event.__dict__

        game_event_dict.pop('_GameEvent__datetime')
        game_event_dict.pop('_GameEvent__event_type')

        game_event_dict['_GameEvent__datetime'] = date_str
        game_event_dict['_GameEvent__event_type'] = event_type_str

        self.__game_event_collection.insert_one(game_event_dict)

    def delete(self, game_event_id):

        if not self.is_game_event_in_db(game_event_id):
            raise ValueError("Game Event doesn't exist")

        query = {
            '_GameEvent__event_id': game_event_id
        }

        self.__game_event_collection.delete_one(query)

    def get(self, game_event_id):

        if not self.is_game_event_in_db(game_event_id):
            raise ValueError("Game Event doesn't exist")

        query = {
            '_GameEvent__event_id': game_event_id
        }

        game_event_dict = self.__game_event_collection.find_one(query)

        return self.game_event_dict_to_object(game_event_dict)

    def get_all(self):

        game_events = self.__game_event_collection.find()

        res = []

        for game_event in game_events:
            res.append(self.game_event_dict_to_object(game_event))

        return res

    def update(self, game_event):

        old_game_event = self.get(game_event.event_id)

        self.delete(game_event.event_id)

        try:
            self.add(game_event)
        except Exception as err:
            self.add(old_game_event)
            raise err

    def game_event_dict_to_object(self, ge_dict):

        date_split = ge_dict['_GameEvent__datetime'].split('.')
        date = datetime(int(date_split[2]), int(date_split[1]), int(date_split[0]))

        event_type_dict = {
            'GOAL': EventTypeEnum.GOAL,
            'YELLOW_CARD': EventTypeEnum.YELLOW_CARD,
            'RED_CARD': EventTypeEnum.RED_CARD
        }

        event_type = event_type_dict[ge_dict['_GameEvent__event_type']]

        return GameEvent(ge_dict['_GameEvent__event_id'], ge_dict['_GameEvent__game'],
                               ge_dict['_GameEvent__referee'], event_type,
                               ge_dict['_GameEvent__event_description'],
                               date, ge_dict['_GameEvent__min_in_game'])

    def is_game_event_in_db(self, game_event_id):

        query = {
            '_GameEvent__event_id': game_event_id
        }

        if self.__game_event_collection.find_one(query) is None:
            return False
        return True

    def update_id_counter(self, counter):

        curr_count = self.get_id_counter()

        query = {
            'game_event_counter': curr_count
        }

        new_values = {
            "$set": {"game_event_counter": counter}
        }

        self.__counters_collection.update_one(query, new_values)

    def get_id_counter(self):

        curr_counter = self.__counters_collection.distinct('game_event_counter')
        return curr_counter[0]

    def reset_db(self):

        self.__game_event_collection.drop()
        self.update_id_counter(1)
