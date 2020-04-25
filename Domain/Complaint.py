""" Idan """


class Complaint:

    def __init__(self, desc, complainer, complaint_ID):

        if type(desc) is not str:
            return ValueError
        if type(complaint_ID) is not int:
            return ValueError

        self.__complainer = complainer
        self.__description = desc
        self.__answer = "none"
        self.__complaint_ID = complaint_ID

    def set_answer(self, answer):
        if type(answer) is not str:
            return ValueError
        self.__answer = answer

    @property
    def answer(self):
        return self.__answer

    @property
    def complaint_ID(self):
        return self.__complaint_ID

    @property
    def description(self):
        return self.__description

    @property
    def complainer(self):
        return self.__complainer


