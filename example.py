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

game = game_db.get(1)
game.main_referee = 15
game_db.update(game)
user = Referee(RefereeQualificationEnum.REGULAR, 'ssss', 'ssss', 'ssss', datetime.now(), 15)
user._Referee__referee_in_games.append(1)
user_db.add_signed_user(user, 'referee')
# game_event = match_cont.add_event(1, 112, EventTypeEnum.GOAL, 'Goal!!!', datetime.now(), 22)

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
# game_db.update(game)

match_cont.start_game(1)

