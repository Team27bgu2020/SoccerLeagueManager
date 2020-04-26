__author__ = 'Oscar Epshtein'

from Domain.Role import Role


class TeamOwner(Role):

    def __init__(self, assigned_by=None, roles=None):
        super().__init__(assigned_by)
        if roles is None:
            roles = []
        self.roles = roles

    """ Getter for Roles"""
    @property
    def roles(self):
        return self.__roles

    """ Getter for Roles"""

    @roles.setter
    def roles(self, value):
        self.__roles = value

    """ Add role to Team Owner"""

    def add_role(self, role):

        if len(self.roles) == 3:
            raise ValueError("Reached Maximum numbers of roles")
        else:
            self.__roles.append(role)

    """ Remove existing role role to Team Owner"""

    def remove_role(self, role):

        if role in self.__roles:
            self.__roles.remove(role)
        else:
            raise ValueError("role doesnt exist")

    """ Remove existing role role to Team Owner"""

    def remove_roles(self):
        self.roles.clear()
