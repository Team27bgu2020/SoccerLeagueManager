import pymongo
import hashlib
from pymongo import errors
import Factories.UserFactory as UserFactory
import Factories.UserDocFactory as UserDocFactory


class MongoUserDB:

    HOST = "mongodb://localhost"
    PORT = 27017
    DB = "SoccerLeagueManagerDB"
    SIGNED_COLLECTION = "SignedUsers"
    NUM_OF_ADMINS = "NumOfAdmins"
    COUNTERS_COLLECTION = "Counters"

    def __init__(self):
        """ Constructor for MongoUserDB """

        try:
            client = pymongo.MongoClient(self.HOST, self.PORT)
            self.__db = client[self.DB]
            self.__signed_user_collection = self.__db[self.SIGNED_COLLECTION]
            self.__num_of_admins_collection = self.__db[self.NUM_OF_ADMINS]
            self.__counters_collection = self.__db[self.COUNTERS_COLLECTION]

        except errors.ConnectionFailure as err:
            raise ConnectionError("Connection Lost\n" + str(err))

    def get_all_signed_users(self):
        """
        @return: Returns all the signed users in the db
        """

        signed_users = self.__signed_user_collection.find()

        signed_users_objects_list = []

        for user in signed_users:
            signed_user_object = UserFactory.user_dictionary[user['role']](user)
            signed_users_objects_list.append(signed_user_object)

        return signed_users_objects_list

    def get_signed_user(self, user_id):
        """
        Return the signed user object that match the user id given
        @param user_id: id of the desired user
        @return: SignedUser object
        """

        query = {
            'user_id': user_id
        }

        signed_user_doc = self.__signed_user_collection.find_one(query)

        if signed_user_doc is None:
            raise Exception("User doesn't exist")

        return UserFactory.doc_to_user(signed_user_doc)

    def get_signed_user_by_user_name(self, user_name):
        """
        Return the signed user object that match the user id given
        @param user_name: id of the desired user
        @return: SignedUser object
        """

        query = {
            'user_name': user_name
        }

        signed_user_doc = self.__signed_user_collection.find_one(query)

        if signed_user_doc is None:
            raise Exception("User doesn't exist")

        return UserFactory.doc_to_user(signed_user_doc)

    def delete_user(self, user_id):
        """
        Remove a user with the given user id from the db
        @param user_id: user id of the user to delete
        """
        query = {
            'user_id': user_id
        }

        user_to_delete = self.__signed_user_collection.find_one(query)

        if user_to_delete is None:
            raise ValueError('User doesnt exists')

        if user_to_delete['role'] == 'system_admin':
            self.remove_from_system_admin_count()

        self.__signed_user_collection.delete_one(query)

    def add_signed_user(self, user_to_add, role_to_add):

        if self.is_sign_user(user_to_add.user_id):
            raise ValueError("User id already exist in the db")

        if self.is_user_name_exist(user_to_add.user_name):
            raise ValueError("User name already taken")

        hash_password = str(hashlib.sha256(user_to_add.password.encode()).hexdigest())
        user_to_add.password = hash_password
        to_add = UserDocFactory.user_to_doc(user_to_add, role_to_add)
        self.__signed_user_collection.insert_one(to_add)

        if role_to_add is 'system_admin':
            self.add_to_system_admin_count()

    def update_signed_user(self, new_user):

        query = {
            'user_id': new_user.user_id
        }

        old_user = self.__signed_user_collection.find_one(query)
        if old_user is None:
            raise ValueError('User doesnt exists')

        self.__signed_user_collection.delete_one(query)

        try:
            self.add_signed_user(new_user, old_user['role'])
        except Exception as err:
            self.__signed_user_collection.insert_one(old_user)
            raise err

    def add_to_system_admin_count(self):
        curr_num_of_admins = self.get_number_of_admins()
        query = {"num_of_admins": curr_num_of_admins}
        new_value = {"$set": {"num_of_admins": (curr_num_of_admins + 1)}}
        self.__num_of_admins_collection.update_one(query, new_value)

    def remove_from_system_admin_count(self):
        curr_num_of_admins = self.get_number_of_admins()
        query = {"num_of_admins": curr_num_of_admins}
        if curr_num_of_admins > 0:
            curr_num_of_admins = curr_num_of_admins - 1
        new_value = {"$set": {"num_of_admins": curr_num_of_admins}}
        self.__num_of_admins_collection.update_one(query, new_value)

    def is_sign_user(self, user_id):
        query = {
            'user_id': user_id
        }

        signed_user_doc = self.__signed_user_collection.find_one(query)

        if signed_user_doc is None:
            return False
        return True

    def is_user_name_exist(self, user_name):

        query = {
            'user_name': user_name
        }

        signed_user_doc = self.__signed_user_collection.find_one(query)

        if signed_user_doc is None:
            return False
        return True

    def get_number_of_admins(self):
        return int(self.__num_of_admins_collection.find()[0]['num_of_admins'])

    def update_id_counter(self, counter):

        curr_count = self.get_id_counter()

        query = {
            'user_counter': curr_count
        }

        new_values = {
            "$set": {"user_counter": counter}
        }

        self.__counters_collection.update_one(query, new_values)

    def get_id_counter(self):

        curr_counter = self.__counters_collection.distinct('user_counter')
        return curr_counter[0]

    def reset_db(self):

        self.__signed_user_collection.drop()
        self.update_id_counter(1)
        self.__num_of_admins_collection.drop()
        self.__num_of_admins_collection.insert_one({"num_of_admins": 0})
