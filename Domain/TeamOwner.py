__author__ = 'Oscar Epshtein'

from Domain.Role import Role


class TeamOwner(Role):

    def __init__(self, assigned_by=None, additional_roles=None):
        super().__init__(assigned_by)
        if additional_roles is None:
            additional_roles = []
        self.roles = additional_roles

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
            raise ValueError("Reached maximum numbers of roles")
        else:
            for owner_role in self.roles:
                if type(owner_role) is type(role):
                    raise ValueError('Owner already have this role')
            self.__roles.append(role)

    """ Remove existing role to Team Owner"""

    def remove_role(self, role):

        if role in self.__roles:
            self.__roles.remove(role)
        else:
            raise ValueError("Owner does not assigned to this role")

    """ Remove all roles from Team Owner"""

    def remove_roles(self):
        self.roles.clear()
