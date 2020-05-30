import socket


# noinspection PyAttributeOutsideInit
class User:

    """ Constructor getting an ip address and user id, checks the given args and update the relevant fields """
    def __init__(self, user_id):
        self.__user_id = user_id

    """ If the user_id only made of numbers, updates self.user_id with it. otherwise raise ValueError"""

    def set_user_id(self, user_id: int):
        if type(user_id) is not int or user_id < 0:
            raise ValueError("Invalid user id. Expected positive integer, received {}".format(user_id))
        self.__user_id = user_id

    """ Returns the user id of the user"""

    @property
    def user_id(self):
        return self.__user_id
