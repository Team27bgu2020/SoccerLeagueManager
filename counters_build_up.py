import pymongo

HOST = "mongodb://localhost"
PORT = 27017
DB = "SoccerLeagueManagerDB"


client = pymongo.MongoClient(HOST, PORT)
db = client[DB]
counters_collection = db["Counters"]

counters_collection.insert_one({'game_counter': 1})
counters_collection.insert_one({'complaints_counter': 1})
counters_collection.insert_one({'game_event_counter': 1})
counters_collection.insert_one({'league_counter': 1})
counters_collection.insert_one({'page_counter': 1})
counters_collection.insert_one({'user_counter': 1})
counters_collection.insert_one({'points_policy_counter': 1})
counters_collection.insert_one({'schedule_policy_counter': 1})
counters_collection.insert_one({'budget_policy_counter': 1})
