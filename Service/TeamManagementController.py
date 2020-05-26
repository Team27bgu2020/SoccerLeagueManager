"""Oscar"""
from DataBases.TeamDB import TeamDB
from Domain import TeamUser
from Domain.Role import Role
from Domain.Team import Team
from Domain.TeamOwner import TeamOwner
from Log.ErrorLogger import *
from Log.Logger import *
import datetime as date
import os


class TeamManagementController:

    def __init__(self, team_db):
        self.__dictionary_team = team_db
        # Logger.start_logger()
        Logger.start_logger()

    @property
    def dictionary_team(self):
        return self.__dictionary_team

    """Get the team, and check if not None"""

    # test: test_get_team

    def get_team(self, team_name: str, user_id=""):
        try:
            team = self.__dictionary_team.get(team_name)
            return team
        except Exception as err:
            Logger.error_log("{0}:".format(user_id) + err.__str__())

    """Open a new team, and add it to the team DB-dictionary"""

    # test:test_open_new_team

    def open_new_team(self, team_name: str, owner: TeamUser, user_id=""):
        try:
            new_team = Team(team_name)
            new_team.owner = owner
            self.__dictionary_team.add(new_team)
            owner.team = new_team
            Logger.info_log("{0}: Team {1} was created".format(user_id, team_name))
        except Exception as err:
            Logger.error_log("{0}:".format(user_id) + err.__str__())
            raise err

    """Add a team existing object, and add it to the team DB-dictionary"""

    # test: test_get_team

    def add_existing_team(self, team, user_id=""):
        try:
            self.__dictionary_team.add(team)
        except Exception as err:
            Logger.error_log("{0}:".format(user_id) + err.__str__())
            raise err

    """ ReOpening closed team"""

    # test: test_reopen_team

    def reopen_team(self, team_name: str, user_id=""):
        try:
            team = self.get_team(team_name, "")
            team.open_team()
            Logger.info_log("{0}:Team {1} reopened".format(user_id,team_name))
        except Exception as err:
            Logger.error_log("{0}:".format(user_id) + err.__str__())
            raise err

    """Closing team, need to check what to do here"""

    # test: test_reopen_team

    def close_team(self, team_name: str, user_id=""):
        try:
            team = self.get_team(team_name, "")
            team.close_team()
            Logger.info_log("{0}: Team {1} closed".format(user_id,team_name))
        except Exception as err:
            Logger.error_log("{0}:".format(user_id) + err.__str__())
            raise err

    """Add team member to a team"""

    # test:test_add_team_member_to_team

    def add_team_member_to_team(self, team_name: str, team_member: TeamUser, user_id=""):
        try:
            team = self.get_team(team_name, "")
            team.add_team_member(team_member)
            Logger.info_log("{0}: User {1} was added to {2}".format(user_id,team_member.name, team_name,user_id))
        except Exception as err:
            Logger.error_log("{0}:".format(user_id) + err.__str__())
            raise err

    """Add team a list members to a team"""

    # test:test_add_team_member_to_team

    def add_team_members_to_team(self, team_name: str, team_members: list, user_id=""):
        try:
            team = self.get_team(team_name, "")
            team.add_team_members(team_members)
            Logger.info_log("{0}: List of users was added".format(user_id))
        except Exception as err:
            Logger.error_log("{0}:".format(user_id) + err.__str__())
            raise err

    """Delete team member from a team"""

    # test:test_add_team_member_to_team

    def remove_team_member_from_team(self, team_name: str, team_member: TeamUser,  user_id=""):
        try:
            team = self.get_team(team_name, "")
            team.remove_team_member(team_member)
            Logger.info_log("{0}: User {1} was deleted from {2}".format(user_id,team_member.name, team_name))
        except Exception as err:
            Logger.error_log("{0}:".format(user_id) + err.__str__())
            raise err

    """Delete team a list members from a team"""

    def remove_team_members_from_team(self, team_name: str, team_members: list, user_id=""):
        try:
            team = self.get_team(team_name, "")
            team.remove_team_members(team_members)
            Logger.info_log("{0}: List of users was deleted".format(user_id))
        except Exception as err:
            Logger.error_log("{0}:".format(user_id) + err.__str__())
            raise err

    """ Get team managers """

    def get_team_managers(self, team_name: str, user_id=""):
        try:
            team = self.get_team(team_name, "")
            return team.managers
        except Exception as err:
            Logger.error_log("{0}:".format(user_id) + err.__str__())
            raise err

    """ Add Manager To team """

    def add_manager_to_team(self, team_name: str, manager: TeamUser, user_id=""):
        try:
            team = self.get_team(team_name, "")
            if manager in team.managers:
                raise ValueError("Already exist in team")
            team.add_team_manager(manager)
            Logger.info_log("{0}: Manager {1} was added to {2}".format(user_id,manager.name, team_name))
        except Exception as err:
            Logger.error_log("{0}:".format(user_id) + err.__str__())
            raise err

    """ Remove Manager from team """

    def remove_manager_from_team(self, team_name: str, manager: TeamUser, user_id=""):
        try:
            team = self.get_team(team_name, "")
            if manager not in team.managers:
                raise ValueError("doesnt have manager")
            team.remove_team_manager(manager)
            Logger.info_log("{0}: User {1} was deleted from {2}".format(user_id,manager.name, team_name))
        except Exception as err:
            Logger.error_log("{0}:".format(user_id) + err.__str__())
            raise err

    """ Get team owners """

    # test:test_get_set_remove_team_owner

    def get_team_owners(self, team_name: str, user_id=""):
        try:
            team = self.get_team(team_name, "")
            return team.owners
        except Exception as err:
            Logger.error_log("{0}:".format(user_id) + err.__str__())
            raise err

    """ Add role player to Owner  """

    def add_role_player_to_owner(self, owner: TeamUser, role: Role, user_id=""):
        try:
            if owner.role.role_player is not None:
                raise ValueError("already has role player")
            owner.role.role_player = role
            Logger.info_log("{0}: Role {2} was added to Owner {1}".format(user_id,owner.SignedUser.name, role.__class__))
        except Exception as err:
            Logger.error_log("{0}:".format(user_id) + err.__str__())
            raise err

    """ remove role from owner  """

    def remove_role_player_from_owner(self, owner: TeamUser, user_id=""):
        try:
            if owner.role.role_player is None:
                raise ValueError("Owner dont Have player role")
            owner.role.role_player = None
        except Exception as err:
            Logger.error_log("{0}:".format(user_id) + err.__str__())
            raise err

    """ Add role coach to Owner  """

    def add_role_coach_to_owner(self, owner: TeamUser, role: Role, user_id=""):
        try:
            if owner.role.role_coach is not None:
                raise ValueError("already has role player")
            owner.role.role_coach = role
            Logger.info_log("{0}: Role {2} was added to Owner {1}".format(user_id, owner.SignedUser.name, role.__class__))
        except Exception as err:
            Logger.error_log("{0}:".format(user_id) + err.__str__())
            raise err

    """ remove coach from owner  """

    def remove_role_coach_from_owner(self, owner: TeamUser, user_id=""):
        try:
            if owner.role.role_coach is None:
                raise ValueError("Owner dont Have player role")
            owner.role.role_coach = None
        except Exception as err:
            Logger.error_log("{0}:".format(user_id) + err.__str__())
            raise err

    """ Add manager role player to Owner  """

    def add_role_manager_to_owner(self, owner: TeamUser, role: Role, user_id=""):
        try:
            if owner.role.role_manager is not None:
                raise ValueError("already has role player")
            owner.role.role_manager = role
            Logger.info_log("{0}: Role {2} was added to Owner {1}".format(user_id, owner.SignedUser.name, role.__class__))
        except Exception as err:
            Logger.error_log("{0}:".format(user_id) + err.__str__())
            raise err

    """ remove manager role from owner  """

    def remove_role_from_owner(self, owner: TeamUser, user_id=""):
        try:
            if owner.role.role_manager is None:
                raise ValueError("Owner dont Have player role")
            owner.role.role_manager = None
        except Exception as err:
            Logger.error_log("{0}:".format(user_id) + err.__str__())
            raise err

    """ Remove Owner from team, By UC 6.3! """
    """ This function removing assigned team owner by the owner and removing his roles"""
    """Talk with OSCAR"""

    """ Add Owner To team """

    def add_owner_to_team(self, team_name: str, owner: TeamUser, user_id=""):
        try:
            team = self.get_team(team_name, "")
            if owner in team.owners:
                raise ValueError("Already exist in team")
            team.add_team_owner(owner)
            Logger.info_log("{0}: Owner {1} was added to {2}".format(user_id, owner.name, team_name))
        except Exception as err:
            Logger.error_log("{0}:".format(user_id) + err.__str__())
            raise err

    def remove_owner_from_team(self, team_name: str, rem_owner: TeamUser, user_id=""):
        try:
            team = self.get_team(team_name, "")
            if rem_owner not in team.owners:
                raise ValueError("doesnt have manager")
            team.remove_team_owner(rem_owner)
            Logger.info_log("{0}: Owner {1} was removed from {2}".format(user_id, rem_owner.name, team_name))
        except Exception as err:
            Logger.error_log("{0}:".format(user_id) + err.__str__())
            raise err

    """ Set stadium To team """

    def set_stadium_to_team(self, team_name: str, stadium, user_id=""):
        try:
            team = self.get_team(team_name, "")
            team.stadium = stadium
            Logger.info_log("{0}: Stadium {1} was set to {2}".format(user_id,stadium, team_name))
        except Exception as err:
            Logger.error_log("{0}:".format(user_id) + err.__str__())
            raise err

    """ Get team stadium """

    def get_team_stadium(self, team_name: str, user_id=""):
        try:
            team = self.get_team(team_name, "")
            return team.stadium
        except Exception as err:
            Logger.error_log("{0}:".format(user_id) + err.__str__())
            raise err

    """ Get team income"""

    # test:test_team__budget

    def get_team_incomes(self, team_name: str, user_id=""):
        try:
            team = self.get_team(team_name, "")
            return team.incomes
        except Exception as err:
            Logger.error_log("{0}:".format(user_id) + err.__str__())
            raise err

    """ Get team expanses"""

    # test:test_team__budget

    def get_team_expanses(self, team_name: str, user_id=""):
        try:
            team = self.get_team(team_name, "")
            return team.expanses
        except Exception as err:
            Logger.error_log("{0}:".format(user_id) + err.__str__())
            raise err

    """ Get team transactions"""

    # test:test_team__budget

    def get_team_transactions(self, team_name: str, user_id=""):
        try:
            team = self.get_team(team_name, "")
            return team.transactions
        except Exception as err:
            Logger.error_log("{0}:".format(user_id) + err.__str__())
            raise err

    """ Get team current budget"""

    # test:test_team__budget

    def get_team_budget(self, team_name: str, user_id=""):
        try:
            team = self.get_team(team_name, "")
            return team.budget
        except Exception as err:
            Logger.error_log("{0}:".format(user_id) + err.__str__())
            raise err

    """ Add income to a team"""""

    # test:test_team__budget

    def add_income_to_team(self, team_name, amount: int, description: str, user_id=""):
        try:
            team = self.get_team(team_name, "")
            team.add_income(amount, description)
            Logger.info_log("{0}: Add income to team {1} : {2}, {3}".format(user_id,team_name, amount ,description))
        except Exception as err:
            Logger.error_log("{0}:".format(user_id) + err.__str__())
            raise err

    """ Add expanse to a team"""""

    # test:test_team__budget

    def add_expanse_to_team(self, team_name, amount: int, description: str, user_id=""):
        try:
            team = self.get_team(team_name, "")
            team.add_expanse(amount, description)
            Logger.info_log("{0}: Add expanse to team {1} : {2}, {3}".format(user_id,team_name, amount ,description))
        except Exception as err:
            Logger.error_log("{0}:".format(user_id) + err.__str__())
            raise err

    """ Set Number To Player """

    def set_number_to_player(self, team_user: TeamUser, number: str, user_id=""):
        try:
            team_user.role.number = number
        except Exception as err:
            Logger.error_log("{0}:".format(user_id) + err.__str__())
            raise err

    """ Set Position To Player """

    def set_position_to_player(self, team_user: TeamUser, position: str, user_id=""):
        try:
            team_user.role.position = position
        except Exception as err:
            Logger.error_log("{0}:".format(user_id) + err.__str__())
            raise err

    """ Set qualification To Player """

    def set_qualification_to_player(self, team_user: TeamUser, qualification: str, user_id=""):
        try:
            team_user.role.qualification = qualification
        except Exception as err:
            Logger.error_log("{0}:".format(user_id) + err.__str__())
            raise err

    def check_if_free_team_user(self, team_user: TeamUser):
        if team_user.team is None:
            return True
        else:
            return False
