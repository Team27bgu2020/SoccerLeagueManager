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

    """ Removes team from union """

    def remove_team_from_union(self, team):
        self.__teams_in_union.remove(team)

    """ Add employee to union """

    def add_employee_to_union(self, employee):
        if employee not in self.__employees:
            self.__employees.append(employee)

    """ Remove employee from union """

    def remove_employee_from_union(self, employee):
        self.__employees.remove(employee)

    """ Add income to union budget """

    def add_income(self, amount, description):
        if type(amount) is not int or type(description) is not str:
            raise TypeError
        if amount <= 0:
            raise ValueError
        self.__incomes.append((description, amount))
        self.__balance += amount
        return True

    """ Add expanse to union budget """

    def add_expense(self, amount, description):
        if type(amount) is not int or type(description) is not str:
            raise TypeError
        if amount <= 0:
            raise ValueError
        if amount > self.__balance:
            raise ValueError
        self.__expanses.append((description, amount))
        self.__balance -= amount

    """ Return true if team in union or false otherwise """

    def is_team_in_union(self, team):
        return team in self.__teams_in_union
