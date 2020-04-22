
class UserDB:

    def __init__(self):

        """ Key = User Name : Value = Obj """
        self.__signed_users = {}

        """ Key = IP Address?? : Value = Obj """
        """self.__guest_id = 0"""
        self.__guests = {}

    @property
    def signed_users(self):
        return self.__signed_users

    @property
    def guests(self):
        return self.__guests

    @signed_users.setter
    def signed_users(self, signed_user):
        self.__signed_users[signed_user.user_name] = signed_users

    @guests.setter
    def guests(self, guest):
        self.__guests[guest.get_user_id] = guest

    def get_signed_user(self, user_name):

        return self.__signed_users[user_name]
