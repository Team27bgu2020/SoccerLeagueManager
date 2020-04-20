from Domain.Team import Team
from Domain.Role import Role


# noinspection PyAttributeOutsideInit
class TeamUser:

    """ Constructor checking the given args and updates the relevant fields accordingly """
    def __init__(self, team, role):

        self.set_team(team)
        self.set_role(role)

    """ Setter for team field """
    def set_team(self, team):

        Team.type_check(team)
        self.__team = team

    """ Setter for role field """
    def set_role(self, role):

        Role.type_check(role)
        self.__role = role


def type_check(obj):

    if type(obj) is not TeamUser:
        raise TypeError
