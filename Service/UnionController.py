from Domain.UnionOrganization import UnionOrganization
# from Service import Logger
from Log.Logger import *


class UnionController:
    """ Constructor for UnionController class """

    def __init__(self, union_organization, registration_fee=1000):
        self.__union_organization = union_organization
        self.registration_fee = registration_fee
        Logger.start_logger()

    """ Collects registration_fee amount of money from each team balance, adds it to UnionOrganization balance 
    and update incomes accordingly"""

    def collect_registration_fee(self, user_id=""):
        try:
            for team in self.__union_organization.teams_in_union:
                if team.add_expanse(self.__registration_fee, "Union registration fee"):
                    self.__union_organization. \
                        add_income(self.__registration_fee, 'registration_fee from {} team'.format(team.name))
                    Logger.info_log(
                        "{0}:".format(user_id) + "Team {0} paid registration fee".format(user_id, team.name))
                else:
                    self.__union_organization.remove_team_from_union(team)
                    Logger.info_log("{0}:".format(user_id) + "Team {0} have not paid registration fee was removed "
                                                             "from union".format(user_id, team.name))
        except Exception as err:
            Logger.error_log("{0}:".format(user_id) + err.__str__())
            raise err

    """ Reduce (num of employees)*(Their salary) money from the union organization balance 
    and adds expanses accordingly """

    def pay_employees(self, user_id=""):
        try:
            for employee in self.__union_organization.employees:
                self.__union_organization.add_expense(employee.salary, "Salary for {} employee".format(employee.name))
                Logger.info_log("{0}:".format(user_id) + "{0} have been payed".format(employee.name))
            Logger.info_log("{0}:".format(user_id) + "Employees were paid")
        except Exception as err:
            Logger.error_log("{0}:".format(user_id) + err.__str__())
            raise err

    """ Add expanse in the given amount and with the given description to union organization """

    def add_expense(self, amount: int, description: str, user_id=""):
        try:
            if amount <= 0:
                raise ValueError("Value less the 0")
            self.__union_organization.add_expense(amount, description)
            Logger.info_log("{0}:".format(user_id) + "Add expanse: {0},{1}".format(amount, description))
        except Exception as err:
            Logger.error_log("{0}:".format(user_id) + err.__str__())
            raise err

    """ Add income in the given amount and with the given description to union organization """

    def add_income(self, amount: int, description: str, user_id=""):
        try:
            if amount <= 0:
                raise ValueError
            self.__union_organization.add_income(amount, description)
            Logger.info_log("{0}:".format(user_id) + "Add income: {0},{1}".format(amount, description))
        except Exception as err:
            Logger.error_log("{0}:".format(user_id) + err.__str__())
            raise err

    def add_team_to_union(self, team, user_id=""):
        try:
            self.__union_organization.add_team_to_union(team)
            Logger.info_log("{0}:".format(user_id) + "Team {0} added to union".format(team.name))
        except Exception as err:
            Logger.error_log("{0}:".format(user_id) + err.__str__())
            raise err

    def add_union_employee_to_union(self, employee, user_id=""):
        try:
            self.__union_organization.add_employee_to_union(employee)
            Logger.info_log("{0}:".format(user_id) + "Employee {0} added to union".format(employee.name))
        except Exception as err:
            Logger.error_log("{0}:".format(user_id) + err.__str__())
            raise err

    def remove_team_from_union(self, team, user_id=""):
        try:
            self.__union_organization.remove_team_from_union(team)
            Logger.info_log("{0}:".format(user_id) + "Team {0} removed to union".format(team.name))
        except Exception as err:
            Logger.warning_log(
                "{0}:".format(user_id) + "Tried to remove team {0} from union-team not in union".format(team.name))
            raise err

    """ Getter for registration_fee field """

    @property
    def registration_fee(self):
        return self.__registration_fee

    """ Setter for registration_fee field """

    @registration_fee.setter
    def registration_fee(self, fee):
        if fee < 0:
            raise ValueError
        self.__registration_fee = fee
