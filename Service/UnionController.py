from Domain.UnionOrganization import UnionOrganization
# from Service import Logger
from Log.Logger import *
from DataBases.MongoDB.MongoUsersDB import MongoUserDB


class UnionController:
    """ Constructor for UnionController class """

    def __init__(self, union_organization, user_db, team_db, registration_fee=1000):
        self.__union_organization = union_organization
        self.__user_DB = user_db
        self.__team_DB = team_db
        self.registration_fee = registration_fee
        Logger.start_logger()

    """ Collects registration_fee amount of money from each team balance, adds it to UnionOrganization balance 
    and update incomes accordingly"""

    def collect_registration_fee(self, user_id=""):
        try:
            for team_name in self.__union_organization.teams_in_union:
                team = self.__team_DB.get(team_name)
                if team.add_expense(self.__registration_fee, "Union registration fee"):
                    self.__union_organization. \
                        add_income(self.__registration_fee, 'registration_fee from {} team'.format(team.name))
                    self.__team_DB.update(team)
                    Logger.info_log(
                        "{0}:".format(user_id) + "Team {0} paid registration fee".format(user_id, team.name))
                else:
                    self.__union_organization.remove_team_from_union(team_name)
                    Logger.info_log("{0}:".format(user_id) + "Team {0} have not paid registration fee was removed "
                                                             "from union".format(user_id, team.name))
        except Exception as err:
            Logger.error_log("{0}:".format(user_id) + err.__str__())
            raise err

    """ Reduce (num of employees)*(Their salary) money from the union organization balance 
    and adds expanses accordingly """

    def pay_employees(self, user_id=""):
        try:
            for employee_id in self.__union_organization.employees:
                employee = self.__user_DB.get_signed_user(employee_id)
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
        except AssertionError as err:
            self.notify_employees(str(err))
            Logger.info_log("{0}:".format(user_id) + "negative budget on Union Organization - notification sent to employees")
        except Exception as err:
            Logger.error_log("{0}:".format(user_id) + err.__str__())
            raise err

    """ Notify all employees about given notification"""
    def notify_employees(self, notification):
        for employee_id in self.__union_organization.employees:
            employee = self.__user_DB.get_signed_user(employee_id)
            employee.notify(notification)
            self.__user_DB.update_signed_user(employee)

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

    def add_team_to_union(self, team_name, user_id=""):
        try:
            self.__team_DB.get(team_name)
            if self.is_team_in_union(team_name):
                raise ValueError('Team is already in union')
            self.__union_organization.add_team_to_union(team_name)
            Logger.info_log("{0}:".format(user_id) + "Team {0} added to union".format(team_name))
        except Exception as err:
            Logger.error_log("{0}:".format(user_id) + err.__str__())
            raise err

    def add_union_employee_to_union(self, employee_id, user_id=""):
        try:
            self.__user_DB.get_signed_user(employee_id)
            if self.is_user_in_union(employee_id):
                raise ValueError("User is already an employee in union")
            self.__union_organization.add_employee_to_union(employee_id)
            Logger.info_log("{0}:".format(user_id) + "Employee {0} added to union".format(employee_id))
        except Exception as err:
            Logger.error_log("{0}:".format(user_id) + err.__str__())
            raise err

    def remove_team_from_union(self, team, user_id=""):
        try:
            if not self.is_team_in_union(team):
                'Team is already not in union'
            self.__union_organization.remove_team_from_union(team)
            Logger.info_log("{0}:".format(user_id) + "Team {0} removed to union".format(team))
        except Exception as err:
            Logger.warning_log(
                "{0}:".format(user_id) + "Tried to remove team {0} from union-team not in union".format(team))
            raise err

    def remove_employee_from_union(self, employee_id, user_id=""):
        try:
            if not self.is_user_in_union(employee_id):
                raise ValueError("Employee is already not in union")
            self.__union_organization.remove_employee_from_union(employee_id)
            Logger.info_log("{0}:".format(user_id) + "User {0} removed from union".format(employee_id))
        except Exception as err:
            Logger.warning_log(
                "{0}:".format(user_id) + "Tried to remove User {0} from union - User not in union".format(employee_id))
            raise err

    def is_team_in_union(self, team_name, user_id=""):
        Logger.info_log('{}: Checked if team {} is in union'.format(user_id, team_name))
        return team_name in self.__union_organization.teams_in_union

    def is_user_in_union(self, union_rep_id, user_id=""):
        Logger.info_log(('{}: Checked if user {} is in union'.format(user_id, union_rep_id)))
        return union_rep_id in self.__union_organization.employees

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
