import Domain.PersonalPage as PersonalPage

""" Idan """


class Complaint:

    def __init__(self, desc):
        self.__description = desc
        self.answer = "none"

    def set_answer(self, answer):
        self.answer = answer

    @property
    def description(self):
        return self.__description


def type_check(obj):
    if type(obj) is not Complaint:
        raise TypeError
