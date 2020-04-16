import Domain.Team
import Domain.Role


class TeamUser:

    """ Default constructor for TeamUser class """
    def __init__(self):
        self.__team = None
        self.__role = None

    """ Constructor checking the given args and updates the relevant fields accordingly """
    def __init__(self, team, role):

        self.set_team(team)
        self.set_role(role)

    """ Setter for team field """
    def set_team(self, team):

        Domain.Team.type_check(team)
        self.__team = team

    """ Setter for role field """
    def set_role(self, role):

        Domain.Role.type_check(role)
        self.__role = role


def type_check(obj):

    if type(obj) is not TeamUser:
        raise TypeError
