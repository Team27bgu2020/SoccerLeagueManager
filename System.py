from DataBases.ComplaintDB import ComplaintDB
from DataBases.GameDB import GameDB
from DataBases.LeagueDB import LeagueDB
from DataBases.PolicyDB import PolicyDB
from DataBases.SeasonDB import SeasonDB
from DataBases.TeamDB import TeamDB
from DataBases.UserDB import UserDB
from Domain.UnionOrganization import UnionOrganization
from Service.ComplaintController import ComplaintController
from Service.LeagueController import LeagueController
from Service.MatchController import MatchController
from Service.SignedUserController import SignedUserController
from Service.TeamManagementController import TeamManagementController
from Service.UnionController import UnionController
from datetime import datetime


class System:

    def __init__(self, admin_user_name, admin_password, admin_name, admin_birth_date, admin_ip):
        self.complaint_db = ComplaintDB()
        self.game_db = GameDB()
        self.league_db = LeagueDB()
        self.season_DB = SeasonDB()
        self.team_db = TeamDB()
        self.user_db = UserDB()
        self.policy_db = PolicyDB()

        self.union_organization = UnionOrganization()

        self.complaint_controller = ComplaintController(self.complaint_db)
        self.league_controller = LeagueController(self.league_db, self.season_DB, PolicyDB)
        self.match_controller = MatchController(self.game_db)
        self.user_controller = SignedUserController(self.user_db)
        self.team_controller = TeamManagementController(self.team_db)
        self.union_controller = UnionController(self.union_organization)

        self.user_controller.add_system_admin(admin_user_name, admin_password, admin_name, admin_birth_date, admin_ip)
