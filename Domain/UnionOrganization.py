class UnionOrganization:

    def __init__(self):
        self.__teams_in_union = []
        self.__employees = []
        self.__incomes = []
        self.__expanses = []
        self.__balance = 0

    """ Getter for balance """

    @property
    def balance(self):
        return self.__balance

    """ Getter for teams in union """

    @property
    def teams_in_union(self):
        return self.__teams_in_union

    """ Getter for union employees """

    @property
    def employees(self):
        return self.__employees

    """ Getter for union incomes """

    @property
    def incomes(self):
        return self.__incomes

    """ Getter for union expanses """

    @property
    def expenses(self):
        return self.__expanses

    """ Adds team to union """

    def add_team_to_union(self, team):
        if team not in self.__teams_in_union:
            self.__teams_in_union.append(team)
        else:
            raise ValueError('Team {} already in union'.format(team.name))

    """ Removes team from union """

    def remove_team_from_union(self, team):
        if team in self.__teams_in_union:
            self.__teams_in_union.remove(team)
        else:
            raise ValueError("Team {} is not in the union".format(team.name))

    """ Add employee to union """

    def add_employee_to_union(self, employee):
        if employee not in self.__employees:
            self.__employees.append(employee)
        else:
            raise ValueError('User {} is already an employee in the union'.format(employee.user_name))

    """ Remove employee from union """

    def remove_employee_from_union(self, employee):
        if employee in self.__employees:
            self.__employees.remove(employee)
        else:
            raise ValueError('User {} is not an employee in the union'.format(employee.user_name))

    """ Add income to union budget """

    def add_income(self, amount, description):

        if amount <= 0:
            raise ValueError("income can't be a negative number")
        self.__incomes.append((description, amount))
        self.__balance += amount
        return True

    """ Add expanse to union budget """

    def add_expense(self, amount, description):

        if amount <= 0:
            raise ValueError("income can't be a negative number")
        if amount > self.__balance:
            self.notify_employees("Union budget is negative.")
        self.__expanses.append((description, amount))
        self.__balance -= amount

    """ Return true if team in union or false otherwise """

    def is_team_in_union(self, team):
        return team in self.__teams_in_union

    """ Notify all employees about given notification"""
    def notify_employees(self, notification):
        for employee in self.employees:
            employee.notify(notification)
