from Domain.Role import Role


class Coach(Role):

    def __init__(self, assigned_by=None, qualification: str = None):
        super().__init__(assigned_by)
        self.__qualification = qualification

    @property
    def qualification(self):
        return self.__qualification

    @qualification.setter
    def qualification(self, qualification):

        if type(qualification) is not str:
            raise TypeError
        self.__qualification = qualification
