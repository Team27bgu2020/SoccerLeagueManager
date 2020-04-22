from abc import ABC

from Domain.Role import Role


class Coach(Role):

    def __init__(self, assigned_by, qualification: str):
        super().__init__(assigned_by)
        self.__qualification = qualification

    """  method to set position """

    def set_qualification_name(self, qualification):
        self.__qualification = qualification

    """  method to get position"""

    def to_string(self):
        print("I am a " + self.get_role_name(), "with " + self.get_qualification_name() + " qualification")

    def get_qualification_name(self):
        return self.__qualification
