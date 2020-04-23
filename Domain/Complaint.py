
""" Idan """


class Complaint:

    def __init__(self, desc, complainer):
        self.__complainer = complainer
        self.__description = desc
        self.answer = "none"

    def set_answer(self, answer):
        self.answer = answer

    @property
    def description(self):
        return self.__description

    @complainer.setter
    def complainer(self, complainer):
        self.complainer = complainer


