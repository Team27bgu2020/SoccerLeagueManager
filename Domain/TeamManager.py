__author__ = 'Oscar Epshtein'

from Domain.Role import Role

""" This class has 4 different booleans to describe the functionality that is available to the manager"""


class TeamManager(Role):

    def __init__(self, assigned_by=None, bool_open_close=False, bool_accounting=False, bool_add_remove=False,
                 bool_set_permission=False):
        super().__init__(assigned_by)

        self.roles = []
        self.__approval_open_close = bool_open_close
        self.__approval_accounting = bool_accounting
        self.__approval_add_remove = bool_add_remove
        self.__approval_set_permission = bool_set_permission

    """  Method to get approve to all options of owner"""

    def approve_all(self):
        self.set_approval_open_close(True)
        self.set_approval_accounting(True)
        self.set_approval_add_remove(True)
        self.set_approval_set_permission(True)

    """  Method to get approve to open or close team"""

    @property
    def approval_open_close(self):
        return self.__approval_open_close

    """  Method to get approval to add expanse and incomes"""

    @property
    def approval_accounting(self):
        return self.__approval_accounting

    """  Method to get approval add or remove asset from team"""

    @property
    def approval_add_remove(self):
        return self.__approval_add_remove

    """  Method to get approval to set other team mate manger permission"""

    @property
    def approval_set_permission(self):
        return self.__approval_set_permission

    def set_approval_open_close(self, value: bool):
        if value is not False and value is not True:
            raise TypeError
        self.__approval_open_close = value

    """  Method to get approval to add expanse and incomes"""

    def set_approval_accounting(self, value: bool):
        if value is not False and value is not True:
            raise TypeError
        self.__approval_accounting = value

    """  Method to get approval add or remove asset from team"""

    def set_approval_add_remove(self, value: bool):
        if value is not False and value is not True:
            raise TypeError
        self.__approval_add_remove = value

    """  Method to get approval to set other team mate manger permission"""

    def set_approval_set_permission(self, value: bool):
        if value is not False and value is not True:
            raise TypeError
        self.__approval_set_permission = value
