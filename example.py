from Domain.Referee import Referee
from Service.LeagueController import LeagueController
from Service.MatchController import MatchController
from DataBases.MongoDB.MongoLeagueDB import MongoLeagueDB
from DataBases.MongoDB.MongoUsersDB import MongoUserDB
from DataBases.MongoDB.MongoTeamDB import MongoTeamDB
from DataBases.MongoDB.MongoPolicyDB import MongoPolicyDB
from DataBases.MongoDB.MongoSeasonDB import MongoSeasonDB
from DataBases.MongoDB.MongoGameDB import MongoGameDB
from DataBases.MongoDB.MongoGameEventDB import MongoGameEventDB
from Service.SignedUserController import SignedUserController
from Service.TeamManagementController import TeamManagementController
from Enums.GameAssigningPoliciesEnum import GameAssigningPoliciesEnum
from Enums.RefereeQualificationEnum import RefereeQualificationEnum
from datetime import  datetime
from Domain.PointsCalculationPolicy import PointsCalculationPolicy
from Domain.GameSchedulePolicy import GameSchedulePolicy
from Domain.TeamBudgetPolicy import TeamBudgetPolicy

user_db = MongoUserDB()
team_db = MongoTeamDB()
league_db = MongoLeagueDB()
policy_db = MongoPolicyDB()
season_db = MongoSeasonDB()
game_db = MongoGameDB()
game_event_db = MongoGameEventDB()

match_cont = MatchController(game_db, user_db, game_event_db, team_db)
team_cont = TeamManagementController(team_db, user_db)
user_con = SignedUserController(user_db)


policy = PointsCalculationPolicy(2, 12, 2, 13)
policy_db.add_point_policy(policy)

# game = game_db.get(1)
# game.remove_event(1)
# game.remove_event(2)
# game.remove_event(3)
# game.remove_event(6)
# game.remove_event(21)
# game.remove_event(22)
# game.remove_event(14)
# game.remove_event(16)
# game.remove_event(17)
# game.remove_event(18)

