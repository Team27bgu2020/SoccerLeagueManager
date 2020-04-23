from typing import Any

from Domain.SystemAdmin import SystemAdmin
from Domain.SignedUser import SignedUser
from Domain.Guest import Guest
from DataBases.UserDB import UserDB

""" Created By Roman"""

""" Change set and get """


class SignedUserController:

    def __init__(self):
        self.__user_data_base = UserDB()
        self.__ID = 0

    """ When we init the signed controller the first user is system admin """

    def add_system_admin(self, user_name, password, name, birth_date):
        admin = SystemAdmin(user_name, password, name, birth_date)
        self.__ID = self.__ID + 1
        admin.set_user_id(self.__ID)
        self.add_user(admin)

    """ Add new user to DB """

    def add_signed_user(self, user_name, password, name, birth_date):
        new_signed_user = SignedUser(user_name, password, name, birth_date)
        self.__ID = self.__ID + 1
        new_signed_user.set_user_id(self.__ID)
        self.add_user(new_signed_user)

    def add_guest(self, ip):
        self.__ID = self.__ID + 1
        new_guest = Guest(ip, self.__ID)
        self.add_user(new_guest)

    """ delete user by user name """

    def delete_signed_user(self, user_name):
        user_data = self.__user_data_base.signed_users.get(user_name)
        if user_data is not None:
            self.__user_data_base.delete_signed_user(user_data.user_name)
            return True
        else:
            print("no such user: " + user_name)
            return False

    def delete_guest(self, ip):
        guest_data = self.__user_data_base.guests.get(ip)
        if guest_data is not None:
            self.__user_data_base.delete_guest(guest_data.user_ip)
            return True
        else:
            print("no such guest: " + ip)
            return False

    def show_all_users(self):
        """

        @return: 2 values: 1. signed users  2. guests
        """
        return self.get_signed_users(), self.get_guests()

    def add_user(self, user):
        """
        Adding users to dictionary by type
        @param user: can be guest or signed user
        """
        if isinstance(user, SignedUser):
            if self.__user_data_base.signed_users.get(user.user_name) is None:
                self.__user_data_base.signed_users[user.user_name] = user
            else:
                self.__ID = self.__ID - 1

        elif type(user) is Guest:
            if self.__user_data_base.guests.get(user.user_ip) is None:
                self.__user_data_base.guests[user.user_ip] = user
            else:
                self.__ID = self.__ID - 1
        else:
            """ Not a guest and not a signed user """
            raise TypeError

    def confirm_user(self, user_name, password):
        user = self.__user_data_base.signed_users.get(user_name)
        if user is None:
            print("User is not in data base")
            return False

        if user.password == password:
            print("User is in data base")
            return True

        else:
            print(" Something Wrong ")

    def edit_personal_name(self, user: SignedUser, new_name):
        user.name = new_name

    def edit_personal_birth_date(self, user: SignedUser, new_birth_date):
        user.birth_date = new_birth_date

    def edit_personal_password(self, user: SignedUser, old_password, new_password):
        if self.confirm_user(user.user_name, old_password):
            user.password = new_password
            print("Password has been changed \n")
            return True
        else:
            print("old password is not match to registered password\n")
            return False

    def add_search(self, user_name, massage):
        self.__user_data_base.add_search(user_name, massage)

    def get_user(self, user_name):
        return self.__user_data_base.signed_users[user_name]

    def get_signed_users(self):
        return self.__user_data_base.signed_users

    def get_guests(self):
        return self.__user_data_base.guests

    @property
    def user_data_base(self):
        return self.__user_data_base
