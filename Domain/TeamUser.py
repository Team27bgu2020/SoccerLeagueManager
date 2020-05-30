from Domain.SignedUser import SignedUser

__author__ = 'Shahar Freiman'


# noinspection PyAttributeOutsideInit
class TeamUser(SignedUser):

    """ Constructor checking the given args and updates the relevant fields accordingly """
    def __init__(self, user_name, password, name, birth_date, user_id, team=None, role=None):

        super().__init__(user_name, password, name, birth_date, user_id)
        self.team = team
        self.role = role

    """ Setter for team field """
    @property
    def team(self):
        return self.__team

    """ Getter for team field """
    @team.setter
    def team(self, team):
        self.__team = team

    """ Setter for role field """
    @property
    def role(self):
        return self.__role

    """ Getter for role field """
    @role.setter
    def role(self, role):
        self.__role = role
