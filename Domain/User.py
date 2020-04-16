import socket


class User:

    """ Default constructor for User class"""
    def __init__(self):

        self.__ip_address = '0.0.0.0'
        self.__user_id = -1

    """ Constructor getting an ip address and user id, checks the given args and update the relevant fields """
    def __init__(self, ip_address, user_id):

        self.set_ip_address(ip_address)
        self.set_user_id(user_id)

    """ If ip_address is a valid ip address, updates self.ip_address field with it, otherwise raise ValueError"""
    def set_ip_address(self, ip_address):

        try:
            socket.inet_aton(ip_address)
            self.__ip_address = ip_address
        except socket.error:
            raise ValueError

    """ Updates self.user_id field with the given user_id """
    def set_user_id(self, user_id):

        self.__user_id = user_id