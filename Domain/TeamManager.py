__author__ = 'Oscar Epshtein'

from Domain.Role import Role


class TeamManager(Role):

    def __init__(self, assigned_by=None, bool_open_close=False, bool_accounting=False, bool_add_rem=False,
                 bool_set_permission=False):
        super().__init__(assigned_by)

        self.__roles = []
        self.__bool_approval_open_close = bool_open_close
        self.__bool_approval_accounting = bool_accounting
        self.__bool_approval_add_remove = bool_add_rem
        self.__bool_approval_set_permission = bool_set_permission

    """  Method to get approve to all options of owner"""

    def approve_all(self):
        self.approval_open_close()
        self.approval_accounting()
        self.approval_add_rem()
        self.approval_set_permission()

    """  Method to get approve to open or close team"""

    def approval_open_close(self):
        self.__bool_approval_open_close = True

    """  Method to get approval to add expanse and incomes"""

    def approval_accounting(self):
        self.__bool_approval_accounting = True

    """  Method to get approval add or remove asset from team"""

    def approval_add_remove(self):
        self.__bool_approval_add_remove = True

    """  Method to get approval to set other team mate manger permission"""

    def approval_set_permission(self):
        self.__bool_approval_set_permission = True

    """  Method to block approve to all options of owner"""

    def disapprove_all(self):
        self.disapproval_open_close()
        self.disapproval_accounting()
        self.disapproval_add_rem()
        self.disapproval_set_permission()

    """  Method to block approve to open or close team"""

    def disapproval_open_close(self):
        self.__bool_approval_open_close = False

    """  Method to block approve to open or close team"""

    def disapproval_accounting(self):
        self.__bool_approval_accounting = False

    """  Method to block approve add or remove asset from team"""

    def disapproval_add_remove(self):
        self.__bool_approval_add_remove = False

    """  Method to block approval to set other team mate manger permission"""

    def disapproval_set_permission(self):
        self.__bool_approval_set_permission = False

    """ Getter to get boolean value of open close approval"""

    def get_bool_approval_open_close(self):
        return self.__bool_approval_open_close

    """ Getter to get boolean value of accounting approval"""

    def get_bool_approval_accounting(self):
        return self.__bool_approval_accounting

    """ Getter to get boolean value of add remove approval"""

    def get_bool_approval_add_remove(self):
        return self.__bool_approval_add_remove

    """ Getter to get boolean value of set permission approval"""

    def get_bool_approval_open_close(self):
        return self.__bool_approval_open_close

