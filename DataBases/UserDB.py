class UserDB:

    def __init__(self):
        """ Key = User Name : Value = Obj """
        self.__signed_users = {}

        """ Key = IP Address?? : Value = Obj """
        """self.__guest_id = 0"""
        self.__guests = {}

        """ Key = user name: Value = string: what he search
            only for fans!"""
        self.__search_history = {}

    @property
    def signed_users(self):
        return self.__signed_users

    @property
    def guests(self):
        return self.__guests

    @property
    def user_data(self):
        return self.__signed_users, self.__guests

    @signed_users.setter
    def signed_users(self, signed_user):
        self.__signed_users[signed_user.user_name] = signed_user

    @guests.setter
    def guests(self, guest):
        self.__guests[guest.get_user_id] = guest

    def get_guest(self, ip):
        return self.__guests[ip]

    def get_signed_user(self, user_name):
        return self.__signed_users[user_name]

    def delete_signed_user(self, user_name):
        del self.__signed_users[user_name]

    def delete_guest(self, ip_address):
        del self.__guests[ip_address]

    def add_search(self, user_name, massage):
        if user_name in self.__search_history:
            self.__search_history[user_name].append(massage)
        else:
            self.__search_history[user_name] = []
            self.__search_history[user_name].append(massage)
