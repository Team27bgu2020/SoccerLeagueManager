import pymongo
from pymongo import errors
from Domain.Complaint import Complaint

class MongoComplaintDB:

    HOST = "mongodb://localhost"
    PORT = 27017
    DB = "SoccerLeagueManagerDB"
    COMPLAINTS_COLLECTION = "Complaints"
    COUNTERS_COLLECTION = "Counters"

    def __init__(self):
        """ Constructor for MongoUserDB """

        try:
            client = pymongo.MongoClient(self.HOST, self.PORT)
            self.__db = client[self.DB]
            self.__complaints_collection = self.__db[self.COMPLAINTS_COLLECTION]
            self.__counters_collections = self.__db[self.COUNTERS_COLLECTION]

        except errors.ConnectionFailure as err:
            raise ConnectionError("Connection Lost\n" + str(err))

    def add(self, complaint):

        if self.is_complaint_in_db(complaint.complaint_id):
            raise ValueError("Complaint with the same id already exists")

        complaint_dict = complaint.__dict__

        self.__complaints_collection.insert_one(complaint_dict)

    def delete(self, complaint_id):

        if not self.is_complaint_in_db(complaint_id):
            raise ValueError("Complaint doesn't exist")

        query = {
            '_Complaint__complaint_ID': complaint_id
        }

        self.__complaints_collection.delete_one(query)

    def get(self, complaint_id):

        if not self.is_complaint_in_db(complaint_id):
            raise ValueError("Complaint doesn't exist")

        query = {
            '_Complaint__complaint_ID': complaint_id
        }

        complaint_dict = self.__complaints_collection.find_one(query)

        return self.complaint_dict_to_object(complaint_dict)

    def get_all(self):

        complaints = self.__complaints_collection.find()

        res = []

        for complaint in complaints:
            res.append(self.complaint_dict_to_object(complaint))

        return res

    def update(self, complaint):

        old_complaint = self.get(complaint.complaint_id)
        self.delete(complaint.complaint_id)
        try:
            self.add(complaint)
        except Exception as err:
            self.add(old_complaint)
            raise err

    def complaint_dict_to_object(self, complaint_dict):

        complaint = Complaint(complaint_dict['_Complaint__description'],
                              complaint_dict['_Complaint__complainer'],
                              complaint_dict['_Complaint__complaint_ID'])

        complaint.set_answer(complaint_dict['_Complaint__answer'])

        return complaint

    def is_complaint_in_db(self, complaint_id):

        query = {
            '_Complaint__complaint_ID': complaint_id
        }

        if self.__complaints_collection.find_one(query) is None:
            return False
        return True

    def update_id_counter(self, counter):

        curr_count = self.get_id_counter()

        query = {
            'complaints_counter': curr_count
        }

        new_values = {
            "$set": {"complaints_counter": counter}
        }

        self.__counters_collections.update_one(query, new_values)

    def get_id_counter(self):

        curr_counter = self.__counters_collections.distinct('complaints_counter')
        return curr_counter[0]

    def reset_db(self):

        self.__complaints_collection.drop()
        self.update_id_counter(1)
