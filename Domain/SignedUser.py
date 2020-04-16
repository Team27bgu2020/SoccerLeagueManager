import datetime as date


# noinspection PyAttributeOutsideInit
class SignedUser:

    def __init__(self, user_name='default', password='default', name='default', birth_date=date.datetime(2000, 1, 1)):

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


def type_check(obj):

    if type(obj) is not SignedUser:
        raise TypeError
