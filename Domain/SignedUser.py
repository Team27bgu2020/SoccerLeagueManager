__author__ = 'Shahar Freiman'

import datetime as date
from Domain.User import User


# noinspection PyAttributeOutsideInit
class SignedUser(User):

    """ Constructor for SignedUser class """
    def __init__(self, user_name, password, name, birth_date):

        self.edit_personal_data(user_name, password, name, birth_date)

    """ Edit the personal data of the user """
    def edit_personal_data(self, user_name, password, name, birth_date):

        self.birth_date(birth_date)
        self.name(name)
        self.password(password)
        self.user_name(user_name)

    """ Getter for birth_date field """
    @property
    def birth_date(self):
        return self.__birth_date

    """ Setter for birth_date field """
    @birth_date.setter
    def birth_date(self, birth_date: date.datetime):
        if type(birth_date) is not date.datetime:
            raise TypeError
        self.__birth_date = birth_date

    """ Getter for name field """
    @property
    def name(self):
        return self.__name

    """ Setter for name field """
    @name.setter
    def name(self, name: str):
        if not str.isalpha(name):
            raise ValueError
        self.__name = name

    """ Getter for user_name field """
    @property
    def user_name(self):
        return self.__user_name

    """ Setter for user_name field """
    @user_name.setter
    def user_name(self, user_name: str):
        self.__user_name = user_name

    """ Getter for password field """
    @property
    def password(self):
        return self.__password

    """ Setter for password field """
    @password.setter
    def password(self, password: str):
        self.__password = password
