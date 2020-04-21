import Domain.PersonalPage as PersonalPage


class Complaint:

    def __init__(self, by_user_id, desc, page):
        self.__by_user_name = by_user_id
        self.__description = desc
        self.set_page(page)

    def set_page(self, page):
        PersonalPage.type_check(page)
        self.__page = page

    @property
    def page(self):
        return self.__page

    @property
    def by_user_id(self):
        return self.__by_user_id

    @property
    def description(self):
        return self.__description


def type_check(obj):
    if type(obj) is not Complaint:
        raise TypeError