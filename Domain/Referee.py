from Domain.SignedUser import SignedUser
from Enums.RefereeQualificationEnum import RefereeQualificationEnum
""" Dor """


class Referee(SignedUser):

    def __init__(self, qualification: RefereeQualificationEnum, user_name, password, name, birth_date, ip_address, user_id):
        self.__events = []
        self.qualification = qualification
        super().__init__(user_name, password, name, birth_date, ip_address, user_id)

    """ This method adds new game event """

    def add_event(self, event):

        self.__events.append(event)

    """ This method removes game event """

    def remove_event(self, event):

        if event in self.__events:
            self.__events.remove(event)

    """ Getter for referee qualification """

    @property
    def qualification(self):

        return self.__qualification

    """ Setter for referee qualification """

    @qualification.setter
    def qualification(self, qualification: RefereeQualificationEnum):

        self.__qualification = qualification

