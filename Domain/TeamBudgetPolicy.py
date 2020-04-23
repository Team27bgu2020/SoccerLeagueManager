
class TeamBudgetPolicy:

    def __init__(self, min_amount: int):

        self.__min_amount = min_amount

    """ This method returns the min amount of budget a team should have to participate in the league """

    @property
    def min_amount(self):
        return self.__min_amount