import pymongo
from pymongo import errors

from Domain.Team import Team
from Domain.TeamBudget import TeamBudget


class MongoTeamDB:

    HOST = "mongodb://localhost"
    PORT = 27017
    DB = "SoccerLeagueManagerDB"
    TEAM_COLLECTION = "Teams"

    def __init__(self):
        """ Constructor for MongoTeamDB """

        try:
            client = pymongo.MongoClient(self.HOST, self.PORT)
            self.__db = client[self.DB]
            self.__teams_collection = self.__db[self.TEAM_COLLECTION]

        except errors.ConnectionFailure as err:
            raise ConnectionError("Connection Lost\n" + str(err))

    def add(self, team):

        if self.is_name_taken(team.name):
            raise ValueError("Could not add team, {0} already taken".format(team.name))

        team_budget_dict = team.budget_manager.__dict__

        team_dict = team.__dict__

        team_dict.pop('_Team__budget_manager')

        team_dict['_Team__budget_manager'] = team_budget_dict

        self.__teams_collection.insert_one(team_dict)

    def delete(self, team_name):

        if not self.is_name_taken(team_name):
            raise ValueError("Team Doesnt exist")

        query = {
            '_Team__name': team_name
        }

        self.__teams_collection.delete_one(query)

    def get(self, team_name):

        if not self.is_name_taken(team_name):
            raise ValueError("Could not get team {0}, team does not exist".format(team_name))

        query = {
            '_Team__name': team_name
        }

        return self.team_dict_to_object(self.__teams_collection.find_one(query))

    def get_all(self):

        teams = self.__teams_collection.find()

        res = []

        for team in teams:
            res.append(self.team_dict_to_object(team))

        return res

    def update(self, team):

        old_team = self.get(team.name)

        self.delete(team.name)

        try:
            self.add(team)
        except Exception as err:
            self.add(old_team)
            raise err

    def is_name_taken(self, team_name):

        query = {
            '_Team__name': team_name
        }

        if self.__teams_collection.find_one(query) is None:
            return False
        return True

    def team_dict_to_object(self, team_dict):
        team_budget_dict = team_dict['_Team__budget_manager']
        team_budget = TeamBudget(team_budget_dict['_TeamBudget__transactions'],
                                 team_budget_dict['_TeamBudget__income_transactions'],
                                 team_budget_dict['_TeamBudget__expanses_transactions'],
                                 team_budget_dict['_TeamBudget__current_balance'])
        return Team(team_dict['_Team__name'], team_dict['_Team__team_members'], team_dict['_Team__stadium'],
                    team_dict['_Team__upcoming_games'], team_dict['_Team__past_games'],
                    team_dict['_Team__leagues'], team_dict['_Team__owners'],
                    team_dict['_Team__managers'], team_dict['_Team__is_open'], team_budget)

    def reset_db(self):

        self.__teams_collection.drop()

