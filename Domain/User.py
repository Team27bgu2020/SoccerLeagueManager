import socket


# noinspection PyAttributeOutsideInit
class User:

    """ Constructor getting an ip address and user id, checks the given args and update the relevant fields """
    def __init__(self, ip_address, user_id):
        self.__ip_address = ip_address
        self.__user_id = user_id

    """ If ip_address is a valid ip address, updates self.ip_address field with it, otherwise raise ValueError"""

    def set_ip_address(self, ip_address):
        try:
            socket.inet_aton(ip_address)
            self.__ip_address = ip_address
        except socket.error:
            raise ValueError

    """ Returns the ip address of the user"""
    def get_ip_address(self):
        return self.__ip_address

    """ If the user_id only made of numbers, updates self.user_id with it. otherwise raise ValueError"""
    def set_user_id(self, user_id):
        if not type(user_id) == int or user_id <= 0:
            raise ValueError
        self.__user_id = user_id

    """ Returns the user id of the user"""
    def get_user_id(self):
        return self.__user_id

    @property
    def user_id(self):
        return self.__user_id

    @property
    def user_ip(self):
        return self.__ip_address
