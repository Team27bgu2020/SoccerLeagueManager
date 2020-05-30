import pymongo
from pymongo import errors
from Domain.League import League
from Domain.PointsCalculationPolicy import PointsCalculationPolicy
from Domain.GameSchedulePolicy import GameSchedulePolicy
from Domain.TeamBudgetPolicy import TeamBudgetPolicy

class MongoLeagueDB:

    HOST = "mongodb://localhost"
    PORT = 27017
    DB = "SoccerLeagueManagerDB"
    LEAGUE_COLLECTION = "Leagues"
    COUNTERS_COLLECTION = "Counters"

    def __init__(self):
        """ Constructor for MongoTeamDB """

        try:
            client = pymongo.MongoClient(self.HOST, self.PORT)
            self.__db = client[self.DB]
            self.__leagues_collection = self.__db[self.LEAGUE_COLLECTION]
            self.__counters_collection = self.__db[self.COUNTERS_COLLECTION]

        except errors.ConnectionFailure as err:
            raise ConnectionError("Connection Lost\n" + str(err))

    def add(self, league):

        if self.is_league_in_db(league.name):
            raise ValueError('League with the same name already exists')

        points_policy_dict = league.points_calculation_policy.__dict__
        games_schedule_policy_dict = league.game_schedule_policy.__dict__
        team_budget_policy_dict = league.team_budget_policy.__dict__
        policies = {'Points': points_policy_dict,
                    'Schedule': games_schedule_policy_dict,
                    'Budget': team_budget_policy_dict
                    }

        league_dict = league.__dict__
        league_dict.pop('_League__policies')
        league_dict['_League__policies'] = policies

        self.__leagues_collection.insert_one(league_dict)

    def delete(self, league_id):

        if not self.is_league_in_db(league_id):
            raise ValueError("League doesn't exists")

        query = {
            '_League__league_id': league_id
        }

        self.__leagues_collection.delete_one(query)

    def get(self, league_id):

        if not self.is_league_in_db(league_id):
            raise ValueError("League doesn't exists")

        query = {
            '_League__league_id': league_id
        }

        league_dict = self.__leagues_collection.find_one(query)
        return self.league_dict_to_object(league_dict)

    def get_all_leagues(self):

        leagues = self.__leagues_collection.find()

        res = []

        for league in leagues:
            res.append(self.league_dict_to_object(league))

        return res

    def update(self, league):

        old_league = self.get(league.league_id)
        self.delete(league.league_id)

        try:
            self.add(league)
        except Exception as err:
            self.add(old_league)
            raise err

    def league_dict_to_object(self, league_dict):

        policies = league_dict['_League__policies']
        points = PointsCalculationPolicy(policies['Points']['_PointsCalculationPolicy__win_points'],
                                         policies['Points']['_PointsCalculationPolicy__tie_points'],
                                         policies['Points']['_PointsCalculationPolicy__lose_points'])
        schedule = GameSchedulePolicy(policies['Schedule']['_GameSchedulePolicy__team_games_num'],
                                      policies['Schedule']['_GameSchedulePolicy__games_per_week'],
                                      policies['Schedule']['_GameSchedulePolicy__chosen_days'],
                                      policies['Schedule']['_GameSchedulePolicy__games_stadium_assigning_policy'])
        budget = TeamBudgetPolicy(policies['Budget']['_TeamBudgetPolicy__min_amount'])

        league = League(league_dict['_League__name'], league_dict['_League__season'], points, schedule, budget, league_dict['_League__league_id'])
        league.referees = league_dict['_League__referees']
        league.teams = league_dict['_League__teams']

        return league

    def is_league_in_db(self, league_id):

        query = {
            '_League__league_id': league_id
        }

        if self.__leagues_collection.find_one(query) is None:
            return False
        return True

    def update_id_counter(self, counter):

        curr_count = self.get_id_counter()

        query = {
            'league_counter': curr_count
        }

        new_values = {
            "$set": {"league_counter": counter}
        }

        self.__counters_collection.update_one(query, new_values)

    def get_id_counter(self):

        curr_counter = self.__counters_collection.distinct('league_counter')
        return curr_counter[0]

    def reset_db(self):

        self.__leagues_collection.drop()
        self.update_id_counter(1)

