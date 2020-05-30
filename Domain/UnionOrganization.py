from DataBases.MongoDB.MongoUnionOrganizationDB import MongoUnionOrganizationDB

class UnionOrganization:

    def __init__(self):

        self.__union_DB = MongoUnionOrganizationDB()
        self.__teams_in_union = self.__union_DB.get_teams()
        self.__employees = self.__union_DB.get_employees()
        self.__incomes = self.__union_DB.get_incomes()
        self.__expenses = self.__union_DB.get_expenses()
        self.__balance = self.__union_DB.get_balance()

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
        return self.__expenses

    """ Adds team to union """

    def add_team_to_union(self, team_name):
        if team_name not in self.__teams_in_union:
            self.__teams_in_union.append(team_name)
            self.__union_DB.update_teams(self.__teams_in_union)
        else:
            raise ValueError('Team {} already in union'.format(team_name))

    """ Removes team from union """

    def remove_team_from_union(self, team_name):
        if team_name in self.__teams_in_union:
            self.__teams_in_union.remove(team_name)
            self.__union_DB.update_teams(self.__teams_in_union)
        else:
            raise ValueError("Team {} is not in the union".format(team_name))

    """ Add employee to union """

    def add_employee_to_union(self, employee):
        if employee not in self.__employees:
            self.__employees.append(employee)
            self.__union_DB.update_employees(self.__employees)
        else:
            raise ValueError('User {} is already an employee in the union'.format(employee))

    """ Remove employee from union """

    def remove_employee_from_union(self, employee):
        if employee in self.__employees:
            self.__employees.remove(employee)
            self.__union_DB.update_employees(self.__employees)
        else:
            raise ValueError('User {} is not an employee in the union'.format(employee))

    """ Add income to union budget """

    def add_income(self, amount, description):

        if amount <= 0:
            raise ValueError("income can't be a negative number")
        self.__incomes.append((description, amount))
        self.__balance += amount
        self.__union_DB.update_incomes(self.incomes)
        self.__union_DB.update_balance(self.balance)
        return True

    """ Add expanse to union budget """

    def add_expense(self, amount, description):

        if amount <= 0:
            raise ValueError("income can't be a negative number")
        self.__expenses.append((description, amount))
        self.__balance -= amount
        self.__union_DB.update_expenses(self.expenses)
        self.__union_DB.update_balance(self.balance)
        if self.__balance < 0:
            raise AssertionError("Union budget is negative.")

    """ Return true if team in union or false otherwise """

    def is_team_in_union(self, team):
        return team in self.__teams_in_union
