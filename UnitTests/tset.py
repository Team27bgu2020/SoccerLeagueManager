from Service.LeagueController import LeagueController
from DataBases.MongoDB.MongoLeagueDB import MongoLeagueDB
from DataBases.MongoDB.MongoSeasonDB import MongoSeasonDB
from DataBases.MongoDB.MongoUsersDB import MongoUserDB
from DataBases.MongoDB.MongoTeamDB import MongoTeamDB
from DataBases.MongoDB.MongoGameDB import MongoGameDB
from DataBases.MongoDB.MongoComplaintDB import MongoComplaintDB
from DataBases.MongoDB.MongoGameEventDB import MongoGameEventDB
from DataBases.MongoDB.MongoPageDB import MongoPageDB
from DataBases.MongoDB.MongoUnionOrganizationDB import MongoUnionOrganizationDB
from Service.MatchController import MatchController
from Service.SignedUserController import SignedUserController
from Service.TeamManagementController import TeamManagementController
from Service.UnionController import UnionController
from Domain.UnionOrganization import UnionOrganization
from Enums.RefereeQualificationEnum import RefereeQualificationEnum
from Enums.EventTypeEnum import EventTypeEnum
from Domain.Team import Team
from datetime import datetime

game_db = MongoGameDB()
team_db = MongoTeamDB()
user_db = MongoUserDB()
complaint_db = MongoComplaintDB()
game_event_db = MongoGameEventDB()
league_db = MongoLeagueDB()
page_db = MongoPageDB()
season_db = MongoSeasonDB()
union_org = MongoUnionOrganizationDB()

game_db.reset_db()
team_db.reset_db()
user_db.reset_db()
complaint_db.reset_db()
game_event_db.reset_db()
league_db.reset_db()
page_db.reset_db()
season_db.reset_db()
union_org.init_union()








