from typing import Any

from Domain.SystemAdmin import SystemAdmin
from Domain.SignedUser import SignedUser
from Domain.Guest import Guest
from DataBases.UserDB import UserDB

""" Created By Roman"""

class SignedUserController:

    def __init__(self):
        self.__user_data_base = UserDB.__init__()

    """ When we init the signed controller the first user is system admin """
    def add_system_admin(self, user_name, password, name, birth_date):
        admin = SystemAdmin(user_name, password, name, birth_date)
        self.add_user_to_data_base(admin)

    """ Add new user to DB """
    def add_signed_user(self, user_name, password, name, birth_date):
        new_signed_user = SignedUser()
        new_signed_user.edit_personal_data(user_name, password, name, birth_date)
        self.add_user_to_data_base(new_signed_user)

    """ delete user by user name """
    def delete_user(self, user_name):
        user_data = self.__user_data_base.get_signed_users
        if user_name in user_data:
            del user_data[user_name]
            self.__user_data_base.set_signed_users(user_data)
        else:
            print("no such user")


    """ @return 2 values: 1. signed users  2. guests """
    def show_all_users(self):
        return self.__user_data_base.get_signed_users, self.__user_data_base.get_guest

    def add_user_to_data_base(self, user):
        """
        Adding users to dictionary by type
        @param user: can be guest or signed user
        """
        if type(user) is SignedUser:
            signed_user_data = self.__user_data_base.get_signed_users
            signed_user_data.update({user.get_user_name: user})
            self.__user_data_base.set_guest(signed_user_data)

        elif type(user) is Guest:
            guest_data = self.__user_data_base.get_guest
            guest_data.update({user.get_user_name: user})
            self.__user_data_base.set_guest(guest_data)
            """self.__guest_id = self.__guest_id + 1"""
        else:
            """ Not a guest and not a signed user """
            raise TypeError

    def add_guest(self):
        pass

    def confirm_user(self, user: SignedUser, password):
        pass

    def edit_personal_name(self, user: SignedUser, new_name):
        pass

    def edit_personal_birth_date(self, user: SignedUser, new_birth_date):
        pass

    def edit_personal_password(self, user: SignedUser, new_password):
        pass
