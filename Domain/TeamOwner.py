__author__ = 'Oscar Epshtein'

from Domain.Role import Role


class TeamOwner(Role):

    def __init__(self, assigned_by):
        super().__init__(assigned_by)
        self.__roles = []

    """ Getter for Roles"""

    def get_roles(self):
        return self.__roles

    """ Getter for Roles"""

    def set_roles(self, new_roles):
        self.__roles = new_roles

    """ Add role to Team Owner"""

    def add_role(self, role):

        if self.__roles.__sizeof__() == 3:
            print("Already have 3 roles."
                  "Reached maximum amount of roles")
        else:
            self.__roles.append(role)
            print("Added successfully")
            self.print_rules()

    """ Remove existing role role to Team Owner"""

    def remove_role(self, role):

        if role in self.__roles:
            self.__roles.remove(role)
            print("Removed Role")
        else:
            print("Role doesnt exist")

    """ Print all roles the owner has"""

    def print_rules(self):
        if self.__roles == 0:
            print("Dont have extra role")
        else:
            print("Additional roles in the team: ")
            print(' ,'.join(map(str, self.__roles)))

    def to_string(self):
        print("I am a " + self.get_role_name())

