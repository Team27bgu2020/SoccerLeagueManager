from Service.LeagueController import LeagueController
from Service.MatchController import MatchController
from Service.SignedUserController import SignedUserController
from Service.TeamManagementController import TeamManagementController
from DataBases.MongoDB.MongoLeagueDB import MongoLeagueDB
from DataBases.MongoDB.MongoUsersDB import MongoUserDB
from DataBases.MongoDB.MongoTeamDB import MongoTeamDB
from DataBases.MongoDB.MongoPolicyDB import MongoPolicyDB
from DataBases.MongoDB.MongoSeasonDB import MongoSeasonDB
from DataBases.MongoDB.MongoGameDB import MongoGameDB
from DataBases.MongoDB.MongoGameEventDB import MongoGameEventDB
from Enums.GameAssigningPoliciesEnum import GameAssigningPoliciesEnum
from Enums.RefereeQualificationEnum import RefereeQualificationEnum
from datetime import datetime

user_db = MongoUserDB()
team_db = MongoTeamDB()
league_db = MongoLeagueDB()
policy_db = MongoPolicyDB()
season_db = MongoSeasonDB()
match_db = MongoGameDB()
game_event_db = MongoGameEventDB()

match_con = MatchController(match_db, user_db, game_event_db, team_db)
team_cont = TeamManagementController(team_db, user_db)
user_cont = SignedUserController(user_db)

match_con.add_game('team1', 'team2', datetime.now(), "1", 5)