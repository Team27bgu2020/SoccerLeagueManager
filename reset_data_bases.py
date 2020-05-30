from DataBases.MongoDB.MongoGameEventDB import MongoGameEventDB
from DataBases.MongoDB.MongoTeamDB import MongoTeamDB
from DataBases.MongoDB.MongoGameDB import MongoGameDB
from DataBases.MongoDB.MongoUsersDB import MongoUserDB
from DataBases.MongoDB.MongoUnionOrganizationDB import MongoUnionOrganizationDB
from DataBases.MongoDB.MongoSeasonDB import MongoSeasonDB
from DataBases.MongoDB.MongoPageDB import MongoPageDB
from DataBases.MongoDB.MongoLeagueDB import MongoLeagueDB
from DataBases.MongoDB.MongoComplaintDB import MongoComplaintDB

game_event_db = MongoGameEventDB()
team_db = MongoTeamDB()
game_db = MongoGameDB()
user_db = MongoUserDB()
union_org = MongoUnionOrganizationDB()
season_db = MongoSeasonDB()
page_db = MongoPageDB()
league_db = MongoLeagueDB()
complaint_db = MongoComplaintDB()

game_event_db.reset_db()
team_db.reset_db()
game_db.reset_db()
user_db.reset_db()
union_org.init_union()
season_db.reset_db()
page_db.reset_db()
league_db.reset_db()
complaint_db.reset_db()
