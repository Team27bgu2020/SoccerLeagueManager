import pymongo
from pymongo import errors
from Domain.GameSchedulePolicy import GameSchedulePolicy
from Domain.PointsCalculationPolicy import PointsCalculationPolicy
from Domain.TeamBudgetPolicy import TeamBudgetPolicy
from Enums.GameAssigningPoliciesEnum import GameAssigningPoliciesEnum


class MongoPolicyDB:

    HOST = "mongodb://localhost"
    PORT = 27017
    DB = "SoccerLeagueManagerDB"
    POINT_POLICY_COLLECTION = "PointsPolicy"
    SCHEDULE_POLICY_COLLECTION = "SchedulePolicy"
    BUDGET_POLICY_COLLECTION = "BudgetPolicy"
    COUNTERS_COLLECTION = "Counters"

    def __init__(self):
        """ Constructor for MongoTeamDB """

        try:
            client = pymongo.MongoClient(self.HOST, self.PORT)
            self.__db = client[self.DB]
            self.__point_policy_collection = self.__db[self.POINT_POLICY_COLLECTION]
            self.__schedule_policy_collection = self.__db[self.SCHEDULE_POLICY_COLLECTION]
            self.__budget_policy_collection = self.__db[self.BUDGET_POLICY_COLLECTION]
            self.__counters_collection = self.__db[self.COUNTERS_COLLECTION]

        except errors.ConnectionFailure as err:
            raise ConnectionError("Connection Lost\n" + str(err))

    def add_point_policy(self, points_policy):

        points_policy_dict = points_policy.__dict__

        self.__point_policy_collection.insert_one(points_policy_dict)

    def add_schedule_policy(self, schedule_policy):

        assign_policy = str(schedule_policy.games_stadium_assigning_policy).split('.')[1]

        policy_dict = schedule_policy.__dict__

        policy_dict.pop('_GameSchedulePolicy__assigning_policy')

        policy_dict['_GameSchedulePolicy__games_stadium_assigning_policy'] = assign_policy

        self.__schedule_policy_collection.insert_one(policy_dict)

    def add_budget_policy(self, budget_policy):

        self.__budget_policy_collection.insert_one(budget_policy.__dict__)

    def delete_points_policy(self, policy_id):

        if not self.is_points_policy_in_db(policy_id):
            raise ValueError("Policy doesn't exists")

        query = {
            '_PointsCalculationPolicy__policy_id': policy_id
        }

        self.__point_policy_collection.delete_one(query)

    def delete_schedule_policy(self, policy_id):

        if not self.is_schedule_policy_in_db(policy_id):
            raise ValueError("Policy doesn't exists")

        query = {
            '_GameSchedulePolicy__policy_id': policy_id
        }

        self.__schedule_policy_collection.delete_one(query)

    def delete_budget_policy(self, policy_id):

        if not self.is_budget_policy_in_db(policy_id):
            raise ValueError("Policy doesn't exists")

        query = {
            '_TeamBudgetPolicy__policy_id': policy_id
        }

        self.__budget_policy_collection.delete_one(query)

    def get_points_policy(self, policy_id):

        if not self.is_points_policy_in_db(policy_id):
            raise ValueError("Policy doesn't exists")

        query = {
            '_PointsCalculationPolicy__policy_id': policy_id
        }

        return self.points_dict_to_object(self.__point_policy_collection.find_one(query))

    def get_schedule_policy(self, policy_id):

        if not self.is_schedule_policy_in_db(policy_id):
            raise ValueError("Policy doesn't exists")

        query = {
            '_GameSchedulePolicy__policy_id': policy_id
        }

        return self.schedule_dict_to_object(self.__schedule_policy_collection.find_one(query))

    def get_budget_policy(self, policy_id):

        if not self.is_budget_policy_in_db(policy_id):
            raise ValueError("Policy doesn't exists")

        query = {
            '_TeamBudgetPolicy__policy_id': policy_id
        }

        return self.budget_dict_to_object(self.__budget_policy_collection.find_one(query))

    def get_all_points_policy(self):

        points_policies = self.__point_policy_collection.find()

        res = []

        for policy in points_policies:
            res.append(self.points_dict_to_object(policy))

        return res

    def get_all_schedule_policy(self):

        schedule_policies = self.__point_schedule_collection.find()

        res = []

        for policy in schedule_policies:
            res.append(self.schedule_dict_to_object(policy))

        return res

    def get_all_budget_policy(self):

        budget_policies = self.__point_budget_collection.find()

        res = []

        for policy in budget_policies:
            res.append(self.budget_dict_to_object(policy))

        return res

    def points_dict_to_object(self, dict):

        return PointsCalculationPolicy(dict['_PointsCalculationPolicy__win_points'],
                                       dict['_PointsCalculationPolicy__tie_points'],
                                       dict['_PointsCalculationPolicy__lose_points'],
                                       dict['_PointsCalculationPolicy__policy_id'])

    def schedule_dict_to_object(self, dict):

        policy_enum_dict = {
            'EQUAL': GameAssigningPoliciesEnum.EQUAL_HOME_AWAY,
            'RANDOM': GameAssigningPoliciesEnum.RANDOM
        }

        stadium_assigning = policy_enum_dict[dict['_GameSchedulePolicy__games_stadium_assigning_policy']]

        return GameSchedulePolicy(dict['_GameSchedulePolicy__team_games_num'],
                                  dict['_GameSchedulePolicy__games_per_week'],
                                  stadium_assigning,
                                  dict['_GameSchedulePolicy__policy_id'])

    def budget_dict_to_object(self, dict):

        return TeamBudgetPolicy(dict['_TeamBudgetPolicy__min_amount'], dict['_TeamBudgetPolicy__policy_id'])

    def is_points_policy_in_db(self, policy_id):

        query = {
            '_PointsCalculationPolicy__policy_id': policy_id
        }

        if self.__point_policy_collection.find_one(query) is None:
            return False
        return True

    def is_schedule_policy_in_db(self, policy_id):

        query = {
            '_GameSchedulePolicy__policy_id': policy_id
        }

        if self.__schedule_policy_collection.find_one(query) is None:
            return False
        return True

    def is_budget_policy_in_db(self, policy_id):

        query = {
            '_TeamBudgetPolicy__policy_id': policy_id
        }

        if self.__budget_policy_collection.find_one(query) is None:
            return False
        return True

    def get_points_id_counter(self):

        curr_counter = self.__counters_collection.distinct('points_policy_counter')
        return curr_counter[0]

    def get_schedule_id_counter(self):

        curr_counter = self.__counters_collection.distinct('schedule_policy_counter')
        return curr_counter[0]

    def get_budget_id_counter(self):

        curr_counter = self.__counters_collection.distinct('budget_policy_counter')
        return curr_counter[0]

    def update_points_id_counter(self, counter):

        curr_count = self.get_points_id_counter()

        query = {
            'points_policy_counter': curr_count
        }

        new_values = {
            "$set": {"points_policy_counter": counter}
        }

        self.__counters_collection.update_one(query, new_values)

    def update_schedule_id_counter(self, counter):

        curr_count = self.get_schedule_id_counter()

        query = {
            'schedule_policy_counter': curr_count
        }

        new_values = {
            "$set": {"schedule_policy_counter": counter}
        }

        self.__counters_collection.update_one(query, new_values)

    def update_budget_id_counter(self, counter):

        curr_count = self.get_budget_id_counter()

        query = {
            'budget_policy_counter': curr_count
        }

        new_values = {
            "$set": {"budget_policy_counter": counter}
        }

        self.__counters_collection.update_one(query, new_values)

    def reset_db(self):

        self.__point_policy_collection.drop()
        self.__schedule_policy_collection.drop()
        self.__budget_policy_collection.drop()
        self.update_points_id_counter(1)
        self.update_budget_id_counter(1)
        self.update_schedule_id_counter(1)