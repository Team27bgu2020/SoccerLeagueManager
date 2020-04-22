__author__ = 'Shahar Freiman'


# noinspection PyAttributeOutsideInit
class TeamUser:

    """ Constructor checking the given args and updates the relevant fields accordingly """
    def __init__(self, team, role):

        self.team(team)
        self.role(role)

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
