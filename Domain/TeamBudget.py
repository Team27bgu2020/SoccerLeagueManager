"""Oscar"""

"""This class is the team budget object"""
"""Each team will have this class """
"""We will have list of expanse/income(strings) and total budget(integer)"""


class TeamBudget:

    def __init__(self, transactions=[], income_transactions=[], expanses_transactions=[], current_balance=0):
        self.__transactions = transactions
        self.__income_transactions = income_transactions
        self.__expanses_transactions = expanses_transactions
        self.__current_balance = current_balance

    """ Add income to team, use positive numbers"""

    def add_income(self, amount: int, description: str):

        if amount <= 0:
            raise ValueError("Income amount can't be negative")

        self.__current_balance += amount
        transaction = "+," + str(amount) + ", " + description
        self.transactions.append(transaction)
        self.incomes.append(transaction)

    """ Add expanse to team, use positive numbers"""

    def add_expanse(self, amount: int, description: str):

        if amount <= 0:
            raise ValueError("Expanse amount can't be negative")
        if self.__current_balance < amount:
            return False

        self.__current_balance -= amount
        transaction = "-,"+str(amount)+", "+description
        self.transactions.append(transaction)
        self.expanses.append(transaction)
        return True

    """Getter to the current budget value"""

    @property
    def current_budget(self):
        return self.__current_balance

    """Getter to the all transactions"""

    @property
    def transactions(self):
        return self.__transactions

    """Getter to all expanses"""

    @property
    def expanses(self):
        return self.__expanses_transactions

    """Getter to all incomes"""

    @property
    def incomes(self):
        return self.__income_transactions

