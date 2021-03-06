
class TeamBudgetPolicy:

    def __init__(self, min_amount: int, policy_id):

        self.__policy_id = policy_id
        self.__min_amount = min_amount

    """ This method returns the min amount of budget a team should have to participate in the league """

    @property
    def min_amount(self):
        return self.__min_amount

    @property
    def policy_id(self):
        return self.__policy_id

    """ This method checks if 2 Policies are the same """

    def __eq__(self, other):

        if self.min_amount != other.min_amount:
            return False
        return True
