from Domain.PointsCalculationPolicy import PointsCalculationPolicy
from Domain.GameSchedulePolicy import GameSchedulePolicy
from Domain.TeamBudgetPolicy import TeamBudgetPolicy


class PolicyDB:

    POINTS_KEY = 'Points'
    SCHEDULE_KEY = 'Schedule'
    BUDGET_KEY = 'budget'

    def __init__(self):

        self.__policies = {
                            self.POINTS_KEY: [],
                            self.SCHEDULE_KEY: [],
                            self.BUDGET_KEY: [],
                           }

    """ This method adds a new policy to the data base """

    def add(self, policy):

        if type(policy) is PointsCalculationPolicy and policy not in self.__policies[self.POINTS_KEY]:
            self.__policies[self.POINTS_KEY].append(policy)

        elif type(policy) is GameSchedulePolicy and policy not in self.__policies[self.SCHEDULE_KEY]:
            self.__policies[self.SCHEDULE_KEY].append(policy)

        elif type(policy) is TeamBudgetPolicy and policy not in self.__policies[self.BUDGET_KEY]:
            self.__policies[self.BUDGET_KEY].append(policy)

        else:
            raise ValueError

    """ This method deletes a policy from the data base """

    def delete(self, policy):

        if policy in self.__policies[self.POINTS_KEY]:
            self.__policies[self.POINTS_KEY].remove(league)

        elif policy in self.__policies[self.SCHEDULE_KEY]:
            self.__policies[self.SCHEDULE_KEY].remove(league)

        elif policy in self.__policies[self.BUDGET_KEY]:
            self.__policies[self.BUDGET_KEY].remove(league)

    """ This method returns all the points calculation policies """

    @property
    def points_calculation_policies(self):

        return self.__policies[self.POINTS_KEY]

    """ This method returns all the game Schedule policies """

    @property
    def game_schedule_policies(self):

        return self.__policies[self.SCHEDULE_KEY]

    """ This method returns all the team budget policies """

    @property
    def team_budget_policies(self):

        return self.__policies[self.BUDGET_KEY]
