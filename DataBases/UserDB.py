import hashlib
from Domain.SystemAdmin import SystemAdmin

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
        self.__signed_users = signed_user

    @guests.setter
    def guests(self, guests):
        self.__guests = guests

    def get_guest(self, ip):
        return self.__guests[ip]

    def get_signed_user(self, user_name):
        return self.__signed_users.get(user_name)

    def delete_signed_user(self, user_name):
        del self.__signed_users[user_name]

    def delete_guest(self, ip_address):
        del self.__guests[ip_address]

    def add_sign_user(self, user):
        hash_password = str(hashlib.sha256(user.password.encode()).hexdigest())
        user.password = hash_password
        self.__signed_users[user.user_name] = user

    def add_guest(self, guest):
        self.__guests[guest.user_ip] = guest

    def add_search(self, user_name, massage):
        if user_name in self.__search_history:
            self.__search_history[user_name].append(massage)
        else:
            self.__search_history[user_name] = []
            self.__search_history[user_name].append(massage)

    def is_sign_user(self, user_name):
        return user_name in self.__signed_users.keys()

    def is_guest_in_data(self, ip):
        return ip in self.__guests.keys()

    def get_number_of_admins_in_system(self):
        dict1_cond = {k: v for (k, v) in self.__signed_users.items() if type(v) is SystemAdmin}
        if dict1_cond is None:
            return 0
        return len(dict1_cond)

    def is_in_data(self, ip):
        return ip in self.__guests.keys()

