
class UserDB:

    def __init__(self):

        """ Key = User Name : Value = Obj """
        self.__signed_users = {}

        """ Key = IP Address?? : Value = Obj """
        """self.__guest_id = 0"""
        self.__guest = {}

    @property
    def signed_users(self):
        return self.__signed_users

    @property
    def guests(self):
        return self.__guest

    @signed_users.setter
    def signed_users(self, signed_users):
        self.__signed_users = signed_users

    def set_guest(self, guest):
        self.__guest = guest
