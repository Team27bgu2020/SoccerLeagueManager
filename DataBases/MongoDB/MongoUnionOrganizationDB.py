import pymongo
from pymongo import errors


class MongoUnionOrganizationDB:

    HOST = "mongodb://localhost"
    PORT = 27017
    DB = "SoccerLeagueManagerDB"
    UNION_ORGANIZATION_COLLECTION = "UnionOrganization"

    def __init__(self):
        """ Constructor for MongoTeamDB """

        try:
            client = pymongo.MongoClient(self.HOST, self.PORT)
            self.__db = client[self.DB]
            self.__union_collection = self.__db[self.UNION_ORGANIZATION_COLLECTION]

        except errors.ConnectionFailure as err:
            raise ConnectionError("Connection Lost\n" + str(err))

    def init_union(self):
        self.__union_collection.drop()
        self.__union_collection.insert_one({'teams_in_union': []})
        self.__union_collection.insert_one({'employees': []})
        self.__union_collection.insert_one({'incomes': []})
        self.__union_collection.insert_one({'expenses': []})
        self.__union_collection.insert_one({'balance': 0})

    def get_teams(self):
        teams = self.__union_collection.distinct('teams_in_union')
        return teams

    def get_employees(self):
        employees = self.__union_collection.distinct('employees')
        return employees

    def get_incomes(self):
        incomes = self.__union_collection.distinct('incomes')
        return incomes

    def get_expenses(self):
        expenses = self.__union_collection.distinct('expenses')
        return expenses

    def get_balance(self):
        balance = self.__union_collection.distinct('balance')
        return balance[0]

    def update_teams(self, teams):
        old_teams = self.get_teams()

        query = {
            'teams_in_union': old_teams
        }

        self.__union_collection.delete_one(query)
        self.__union_collection.insert_one({'teams_in_union': teams})

    def update_employees(self, employees):
        old_employees = self.get_employees()

        query = {
            'employees': old_employees
        }

        self.__union_collection.delete_one(query)
        self.__union_collection.insert_one({'employees': employees})

    def update_incomes(self, incomes):
        old_incomes = self.get_incomes()

        query = {
            'incomes': old_incomes
        }

        self.__union_collection.delete_one(query)
        self.__union_collection.insert_one({'incomes': incomes})

    def update_expenses(self, expenses):
        old_expenses = self.get_expenses()

        query = {
            'expenses': old_expenses
        }

        self.__union_collection.delete_one(query)
        self.__union_collection.insert_one({'expenses': expenses})

    def update_balance(self, balance):
        old_balance = self.get_balance()

        query = {
            'balance': old_balance
        }

        self.__union_collection.delete_one(query)
        self.__union_collection.insert_one({'balance': balance})

