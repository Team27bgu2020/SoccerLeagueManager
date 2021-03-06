""" Idan """


class Complaint:

    def __init__(self, desc, complainer, complaint_id):

        self.__complainer = complainer
        self.__description = desc
        self.__answer = "none"
        self.__complaint_ID = complaint_id

    def set_answer(self, answer):
        if type(answer) is not str:
            return ValueError('{} is not a valid complaint answer'.format(answer))
        self.__answer = answer

    @property
    def answer(self):
        return self.__answer

    @property
    def complaint_id(self):
        return self.__complaint_ID

    @property
    def description(self):
        return self.__description

    @property
    def complainer(self):
        return self.__complainer


