
class UserDB:

    def __init__(self):

        """ Key = User Name : Value = Obj """
        self.__signed_users = {}

        """ Key = IP Address?? : Value = Obj """
        """self.__guest_id = 0"""
        self.__guest = {}

    @property
    def get_signed_users(self):
        return self.__signed_users

    @property
    def get_guest(self):
        return self.__guest

    def set_signed_users(self, signed_users):
        self.__signed_users = signed_users

    def set_guest(self, guest):
        self.__guest = guest
