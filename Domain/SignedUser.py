import datetime as date
from Domain.User import User


# noinspection PyAttributeOutsideInit
class SignedUser(User):

    def __init__(self, user_name, password, name, birth_date):

        self.edit_personal_data(user_name, password, name, birth_date)

    def edit_personal_data(self, user_name, password, name, birth_date):

        if type(birth_date) is not date.datetime:
            raise TypeError

        if not name.isalpha():
            raise ValueError

        self.__birth_date = birth_date
        self.__name = name
        self.__password = password
        self.__user_name = user_name

    @property
    def birth_date(self):
        return self.__birth_date

    @birth_date.setter
    def birth_date(self, birth_date: date.datetime):
        self.__birth_date = birth_date

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        if not str.isalpha(name):
            raise ValueError
        self.__name = name

    @property
    def user_name(self):
        return self.__user_name

    @user_name.setter
    def user_name(self, user_name: str):
        self.__user_name = user_name

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, password: str):
        self.__password = password


def type_check(obj):

    if type(obj) is not SignedUser:
        raise TypeError
