import hashlib
from typing import Any

from Domain.Fan import Fan
from Domain.Referee import Referee
from Domain.SystemAdmin import SystemAdmin
from Domain.SignedUser import SignedUser
from Domain.Guest import Guest
from DataBases.UserDB import UserDB

""" Created By Roman"""


class SignedUserController:

    def __init__(self, user_db):
        self.__user_data_base = user_db
        self.__ID = 0

    """ Add new signed user to DB """

    def add_signed_user(self, user_name, password, name, birth_date, ip_address):
        """

        @param user_name:
        @param password:
        @param name:
        @param birth_date:
        @param ip_address:
        @return: add signed user to DB
        """
        self.__ID = self.__ID + 1
        new_signed_user = SignedUser(user_name, password, name, birth_date, ip_address, self.__ID)
        self.add_user(new_signed_user)

    def add_guest(self, ip):
        self.__ID = self.__ID + 1
        new_guest = Guest(ip, self.__ID)
        self.add_user(new_guest)

    def add_Team_User(self, user_name, password, name, birth_date, ip_address):
        self.__ID = self.__ID + 1
        new_signed_user = SignedUser(user_name, password, name, birth_date, ip_address, self.__ID)
        self.add_user(new_signed_user)

    """ delete user by user name """

    def delete_signed_user(self, user_name):
        if self.__user_data_base.is_sign_user(user_name):
            if type(self.__user_data_base.get_signed_user(user_name)) is SystemAdmin:
                """Check if there is more admins in  system if no return false"""
                if(self.number_of_admins() < 2):
                    raise AssertionError
            self.__user_data_base.delete_signed_user(user_name)
            return True
        else:
            return False

    def delete_guest(self, ip):
        if self.__user_data_base.is_guest_in_data(ip):
            self.__user_data_base.delete_guest(ip)
            return True
        else:
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
            if self.__user_data_base.is_sign_user(user.user_name):
                self.__ID = self.__ID - 1
            else:
                self.__user_data_base.add_sign_user(user)

        elif type(user) is Guest:
            if self.__user_data_base.is_guest_in_data(user.user_ip):
                self.__ID = self.__ID - 1
            else:
                self.__user_data_base.add_guest(user)

        else:
            """ Not a guest and not a signed user """
            raise TypeError

    def confirm_user(self, user_name, password):
        """
        @param user_name: for confirm
        @param password: for confirm
        @return: if the user exist - the function will return the type of the user
        """
        user = self.__user_data_base.get_signed_user(user_name)
        if user is None:
            return False

        if user.password == str(hashlib.sha256(password.encode()).hexdigest()):
            return str(type(user).__name__)

        else:
            return False

    """ Edit all of the personal data of signed user """
    def edit_personal_data(self, user, user_name, password, name, birth_date):
        user.edit_personal_data(user_name, password, name, birth_date)


    """Editing personal info"""

    def edit_personal_name(self, user_name, new_name):
        if self.__user_data_base.is_sign_user(user_name):
            signed_user = self.__user_data_base.get_signed_user(user_name)
            signed_user.name = new_name
            return True
        else:
            return False

    def edit_personal_birth_date(self, user_name: str, new_birth_date):
        if self.__user_data_base.is_sign_user(user_name):
            signed_user = self.__user_data_base.get_signed_user(user_name)
            signed_user.birth_date = new_birth_date
            return True
        else:
            return False

    def edit_personal_password(self, user_name, old_password, new_password):
        if self.confirm_user(user_name, old_password):
            signed_user = self.__user_data_base.get_signed_user(user_name)
            signed_user.password = str(hashlib.sha256(new_password.encode()).hexdigest())
            return True
        else:
            return False

    def add_search(self, user_name, massage):
        self.__user_data_base.add_search(user_name, massage)

    def get_user(self, user_name):
        if user_name in self.__user_data_base.signed_users:
            return self.__user_data_base.signed_users[user_name]
        else:
            return None

    def get_signed_users(self):
        return self.__user_data_base.signed_users

    def get_guests(self):
        return self.__user_data_base.guests

    @property
    def user_data_base(self):
        return self.__user_data_base

    """ Adding users by type =>"""

    def add_fan_to_data(self, user_name, password, name, birth_date, ip_address):
        """
        add`s fan to DB - the fan is signed user
        @param user_name: string
        @param password: given string before security algorithm
        @param name: name - no numbers
        @param birth_date: date Type only!
        @param ip_address: ip of the user
        @return: no return
        """
        self.__ID = self.__ID + 1
        f = Fan(user_name, password, name, birth_date, ip_address, self.__ID)
        self.add_user(f)

    """ When we init the signed controller the first user is system admin """

    def add_system_admin(self, user_name, password, name, birth_date, ip_address):
        self.__ID = self.__ID + 1
        admin = SystemAdmin(user_name, password, name, birth_date, ip_address, self.__ID)
        self.add_user(admin)

    def add_referee_to_data(self, qualification, user_name, password, name, birth_date, ip_address):
        self.__ID = self.__ID + 1
        referee_user = Referee(qualification, user_name, password, name, birth_date, ip_address, self.__ID)
        self.add_user(referee_user)

    def number_of_admins(self):
        """

        @return: number of admins that in the system
        """
        return self.__user_data_base.get_number_of_admins_in_system()
