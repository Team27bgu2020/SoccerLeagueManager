from Service.LeagueController import LeagueController
from DataBases.MongoDB.MongoLeagueDB import MongoLeagueDB
from DataBases.MongoDB.MongoUsersDB import MongoUserDB
from DataBases.MongoDB.MongoTeamDB import MongoTeamDB
from DataBases.MongoDB.MongoPolicyDB import MongoPolicyDB
from DataBases.MongoDB.MongoSeasonDB import MongoSeasonDB
from Enums.GameAssigningPoliciesEnum import GameAssigningPoliciesEnum

user_db = MongoUserDB()
team_db = MongoTeamDB()
league_db = MongoLeagueDB()
policy_db = MongoPolicyDB()
season_db = MongoSeasonDB()

league_cont = LeagueController(league_db, season_db, user_db, policy_db)

league = league_cont.get_league(1)
print(league)