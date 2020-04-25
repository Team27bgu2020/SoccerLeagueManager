from Domain.UnionOrganization import UnionOrganization


class UnionController:

    """ Constructor for UnionController class """
    def __init__(self, union_organization, registration_fee=1000):
        self.__union_organization = union_organization
        self.registration_fee = registration_fee

    """ Collects registration_fee amount of money from each team balance, adds it to UnionOrganization balance 
    and update incomes accordingly"""
    def collect_registration_fee(self):
        for team in self.__union_organization.teams_in_union:
            if team.add_expanse(self.__registration_fee, "Union registration fee"):
                self.__union_organization.\
                    add_income(self.__registration_fee, 'registration_fee from {} team'.format(team.name))
            else:
                self.__union_organization.remove_team_from_union(team)

    """ Reduce (num of employees)*(Their salary) money from the union organization balance 
    and adds expanses accordingly """
    def pay_employees(self):
        for employee in self.__union_organization.employees:
            self.__union_organization.add_expense(employee.salary, "Salary for {} employee".format(employee.name))

    """ Add expanse in the given amount and with the given description to union organization """
    def add_expense(self, amount: int, description: str):
        if amount <= 0:
            raise ValueError
        self.__union_organization.add_expense(amount, description)

    """ Add income in the given amount and with the given description to union organization """
    def add_income(self, amount: int, description: str):
        if amount <= 0:
            raise ValueError
        self.__union_organization.add_income(amount, description)

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
