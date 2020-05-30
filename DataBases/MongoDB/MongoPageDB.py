import pymongo
from pymongo import errors

from Domain.PersonalPage import PersonalPage

class MongoPageDB:

    HOST = "mongodb://localhost"
    PORT = 27017
    DB = "SoccerLeagueManagerDB"
    PERSONAL_PAGE_COLLECTION = "PersonalPage"
    COUNTERS_COLLECTION = "Counters"

    def __init__(self):
        """ Constructor for MongoTeamDB """

        try:
            client = pymongo.MongoClient(self.HOST, self.PORT)
            self.__db = client[self.DB]
            self.__page_collection = self.__db[self.PERSONAL_PAGE_COLLECTION]
            self.__counters_collection = self.__db[self.COUNTERS_COLLECTION]

        except errors.ConnectionFailure as err:
            raise ConnectionError("Connection Lost\n" + str(err))

    def add(self, page):

        if self.is_page_in_db(page.page_id):
            raise ValueError("Page with the same page id already exists")

        page_dict = page.__dict__

        self.__page_collection.insert_one(page_dict)

    def delete(self, page_id):

        if not self.is_page_in_db(page_id):
            raise ValueError("Page doesn't exist")

        query = {
            '_PersonalPage__page_id': page_id
        }

        self.__page_collection.delete_one(query)

    def get(self, page_id):

        if not self.is_page_in_db(page_id):
            raise ValueError("Page doesn't exist")

        query = {
            '_PersonalPage__page_id': page_id
        }

        page_dict = self.__page_collection.find_one(query)

        return PersonalPage(page_dict['_PersonalPage__page_id'], page_dict['_PersonalPage__title'])

    def get_all(self):

        pages = self.__page_collection.find()

        res = []

        for page_dict in pages:
            res.append(PersonalPage(page_dict['_PersonalPage__page_id'], page_dict['_PersonalPage__title']))

        return res

    def update(self, page):

        old_page = self.get(page.page_id)

        self.delete(page.page_id)

        try:
            self.add(page)
        except Exception as err:
            self.add(old_page)
            raise err

    def is_page_in_db(self, page_id):

        query = {
            '_PersonalPage__page_id': page_id
        }

        if self.__page_collection.find_one(query) is None:
            return False
        return True

    def update_id_counter(self, counter):

        curr_count = self.get_id_counter()

        query = {
            'page_counter': curr_count
        }

        new_values = {
            "$set": {"page_counter": counter}
        }

        self.__counters_collection.update_one(query, new_values)

    def get_id_counter(self):

        curr_counter = self.__counters_collection.distinct('page_counter')
        return curr_counter[0]

    def reset_db(self):

        self.__page_collection.drop()
        self.update_id_counter(1)
