"""Oscar"""
from DataBases.MongoDB.MongoTeamDB import MongoTeamDB
from DataBases.MongoDB.MongoUsersDB import MongoUserDB
from Domain import TeamUser
from Domain.Role import Role
from Domain.Team import Team
from Domain.TeamOwner import TeamOwner
from Log.ErrorLogger import *
from Log.Logger import *
import datetime as date
import os


class TeamManagementController:

    def __init__(self, team_db, users_db):
        self.__dictionary_team = team_db
        self.__users_db = users_db
        Logger.start_logger()

    @property
    def dictionary_team(self):
        return self.__dictionary_team

    """Get the team, and check if not None"""

    def get_team(self, team_name: str, user_id=""):
        try:
            team = self.__dictionary_team.get(team_name)
            return team
        except Exception as err:
            Logger.error_log("{0}:".format(user_id) + err.__str__())

    def get_all_teams(self):
        return self.__dictionary_team.get_all()

    """Open a new team, and add it to the team DB-dictionary"""

    # test:test_open_new_team

    def open_new_team(self, team_name: str, owner_id, user_id=""):
        try:
            owner = self.__users_db.get_signed_user(owner_id)
            new_team = Team(team_name)
            new_team.add_team_owner(owner_id)
            owner.team = team_name
            self.__dictionary_team.add(new_team)
            self.__users_db.update_signed_user(owner)
            Logger.info_log("{0}: Team {1} was created".format(user_id, team_name))
        except Exception as err:
            Logger.error_log("{0}:".format(user_id) + err.__str__())
            raise err

    def delete_team(self, team_name, user_id=""):
        try:
            team = self.__dictionary_team.get(team_name)
            for member_id in team.team_members:
                self.remove_team_member_from_team(team_name, member_id)
            for manager_id in team.managers:
                self.remove_manager_from_team(team_name, manager_id)
            try:
                for owner_id in team.owners:
                    self.remove_owner_from_team(team_name, owner_id)
            except:
                owner = self.__users_db.get_signed_user(team.owners[0])
                owner.team = None
                self.__users_db.update_signed_user(owner)

            self.__dictionary_team.delete(team_name)
            Logger.info_log("{0}: Team {1} was deleted".format(user_id, team_name))
        except Exception as err:
            Logger.error_log("{0}:".format(user_id) + err.__str__())
            raise err

    """Add a team existing object, and add it to the team DB-dictionary"""

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
            self.__dictionary_team.update(team)
            self.notify_team_members(team, "Team {} is now reopened".format(team_name))
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
            self.__dictionary_team.update(team)
            self.notify_team_members(team, "Team {} is now closed".format(team_name))
            Logger.info_log("{0}: Team {1} closed".format(user_id,team_name))
        except Exception as err:
            Logger.error_log("{0}:".format(user_id) + err.__str__())
            raise err

    """ Notify team members with a certain notification """
    def notify_team_members(self, team, notification):
        for team_member_id in team.team_members:
            team_member = self.__users_db.get_signed_user(team_member_id)
            team_member.notify(notification)
            self.__users_db.update_signed_user(team_member)
        for team_manager_id in team.managers:
            team_manager = self.__users_db.get_signed_user(team_manager_id)
            team_manager.notify(notification)
            self.__users_db.update_signed_user(team_manager)
        for team_owner_id in team.owners:
            team_owner = self.__users_db.get_signed_user(team_owner_id)
            team_owner.notify(notification)
            self.__users_db.update_signed_user(team_owner)

    """Add team member to a team"""

    # test:test_add_team_member_to_team

    def add_team_member_to_team(self, team_name: str, team_member_id, user_id=""):
        try:
            team_member = self.__users_db.get_signed_user(team_member_id)
            if team_member.team is not None:
                raise ValueError('User {} already have a team'.format(team_member.user_name))
            team = self.get_team(team_name, "")
            team.add_team_member(team_member_id)
            team_member.team = team_name
            self.__users_db.update_signed_user(team_member)
            self.__dictionary_team.update(team)
            Logger.info_log("{0}: User {1} was added to {2}".format(user_id, team_member.name, team_name))
        except Exception as err:
            Logger.error_log("{0}:".format(user_id) + err.__str__())
            raise err

    """Add team a list members to a team"""

    # test:test_add_team_member_to_team

    def add_team_members_to_team(self, team_name: str, team_members: list, user_id=""):
        try:
            for team_member_id in team_members:
                self.add_team_member_to_team(team_name, team_member_id, user_id)
            Logger.info_log("{0}: List of users was added".format(user_id))
        except Exception as err:
            Logger.error_log("{0}:".format(user_id) + err.__str__())
            raise err

    """Delete team member from a team"""

    # test:test_add_team_member_to_team

    def remove_team_member_from_team(self, team_name: str, team_member_id,  user_id=""):
        try:
            team = self.get_team(team_name, "")
            team_member = self.__users_db.get_signed_user(team_member_id)
            team.remove_team_member(team_member_id)
            team_member.team = None
            self.__users_db.update_signed_user(team_member)
            self.__dictionary_team.update(team)
            Logger.info_log("{0}: User {1} was deleted from {2}".format(user_id, team_member.name, team_name))
        except Exception as err:
            Logger.error_log("{0}:".format(user_id) + err.__str__())
            raise err

    """Delete team a list members from a team"""

    def remove_team_members_from_team(self, team_name: str, team_members: list, user_id=""):
        try:
            for team_member_id in team_members:
                self.remove_team_member_from_team(team_name, team_member_id, user_id)
            Logger.info_log("{0}: List of users was deleted".format(user_id))
        except Exception as err:
            Logger.error_log("{0}:".format(user_id) + err.__str__())
            raise err

    """ Get team managers """

    def get_team_managers(self, team_name: str, user_id=""):
        try:
            team = self.get_team(team_name, "")
            res = []
            for manager_id in team.managers:
                res.append(self.__users_db.get_signed_user(manager_id))
            return res
        except Exception as err:
            Logger.error_log("{0}:".format(user_id) + err.__str__())
            raise err

    """ Add Manager To team """

    def add_manager_to_team(self, team_name: str, manager_id, user_id=""):
        try:
            team = self.get_team(team_name, "")
            manager = self.__users_db.get_signed_user(manager_id)
            if manager_id in team.managers:
                raise ValueError("Already exist in team")
            if manager.team is not None:
                raise ValueError('User {} is already in another team'.format(manager.user_name))
            team.add_team_manager(manager_id)
            manager.team = team_name
            self.__users_db.update_signed_user(manager)
            self.__dictionary_team.update(team)
            Logger.info_log("{0}: Manager {1} was added to {2}".format(user_id, manager.name, team_name))
        except Exception as err:
            Logger.error_log("{0}:".format(user_id) + err.__str__())
            raise err

    """ Remove Manager from team """

    def remove_manager_from_team(self, team_name: str, manager_id, user_id=""):
        try:
            team = self.get_team(team_name, "")
            manager = self.__users_db.get_signed_user(manager_id)
            if manager_id not in team.managers:
                raise ValueError("doesnt have manager")
            team.remove_team_manager(manager_id)
            manager.team = None
            self.__users_db.update_signed_user(manager)
            self.__dictionary_team.update(team)
            Logger.info_log("{0}: User {1} was deleted from {2}".format(user_id,manager.name, team_name))
        except Exception as err:
            Logger.error_log("{0}:".format(user_id) + err.__str__())
            raise err

    """ Get team owners """

    # test:test_get_set_remove_team_owner

    def get_team_owners(self, team_name: str, user_id=""):
        try:
            team = self.get_team(team_name, "")
            res = []
            for owner_id in team.owners:
                res.append(self.__users_db.get_signed_user(owner_id))
            return res
        except Exception as err:
            Logger.error_log("{0}:".format(user_id) + err.__str__())
            raise err

    """ Add role player to Owner  """

    def add_role_player_to_owner(self, owner_id, role: Role, user_id=""):
        try:
            owner = self.__users_db.get_signed_user(owner_id)
            if owner.role.role_player is not None:
                raise ValueError("already has role player")
            owner.role.role_player = role
            self.__users_db.update_signed_user(owner)
            Logger.info_log("{0}: Role {2} was added to Owner {1}".format(user_id,owner.SignedUser.name, role.__class__))
        except Exception as err:
            Logger.error_log("{0}:".format(user_id) + err.__str__())
            raise err

    """ remove role from owner  """

    def remove_role_player_from_owner(self, owner_id, user_id=""):
        try:
            owner = self.__users_db.get_signed_user(owner_id)
            if owner.role.role_player is None:
                raise ValueError("Owner dont Have player role")
            owner.role.role_player = None
            self.__users_db.update_signed_user(owner)
        except Exception as err:
            Logger.error_log("{0}:".format(user_id) + err.__str__())
            raise err

    """ Add role coach to Owner  """

    def add_role_coach_to_owner(self, owner_id, role: Role, user_id=""):
        try:
            owner = self.__users_db.get_signed_user(owner_id)
            if owner.role.role_coach is not None:
                raise ValueError("already has role player")
            owner.role.role_coach = role
            self.__users_db.update_signed_user(owner)
            Logger.info_log("{0}: Role {2} was added to Owner {1}".format(user_id, owner.SignedUser.name, role.__class__))
        except Exception as err:
            Logger.error_log("{0}:".format(user_id) + err.__str__())
            raise err

    """ remove coach from owner  """

    def remove_role_coach_from_owner(self, owner_id, user_id=""):
        try:
            owner = self.__users_db.get_signed_user(owner_id)
            if owner.role.role_coach is None:
                raise ValueError("Owner dont Have player role")
            owner.role.role_coach = None
            self.__users_db.update_signed_user(owner)
        except Exception as err:
            Logger.error_log("{0}:".format(user_id) + err.__str__())
            raise err

    """ Add manager role player to Owner  """

    def add_role_manager_to_owner(self, owner_id, role: Role, user_id=""):
        try:
            owner = self.__users_db.get_signed_user(owner_id)
            if owner.role.role_manager is not None:
                raise ValueError("already has role player")
            owner.role.role_manager = role
            self.__users_db.update_signed_user(owner)
            Logger.info_log("{0}: Role {2} was added to Owner {1}".format(user_id, owner.SignedUser.name, role.__class__))
        except Exception as err:
            Logger.error_log("{0}:".format(user_id) + err.__str__())
            raise err

    """ remove manager role from owner  """

    def remove_role_from_owner(self, owner_id, user_id=""):
        try:
            owner = self.__users_db.get_signed_user(owner_id)
            if owner.role.role_manager is None:
                raise ValueError("Owner dont Have player role")
            owner.role.role_manager = None
            self.__users_db.update_signed_user(owner)
        except Exception as err:
            Logger.error_log("{0}:".format(user_id) + err.__str__())
            raise err

    """ Remove Owner from team, By UC 6.3! """
    """ This function removing assigned team owner by the owner and removing his roles"""
    """Talk with OSCAR"""

    """ Add Owner To team """

    def add_owner_to_team(self, team_name: str, owner_id, user_id=""):
        try:
            team = self.get_team(team_name, "")
            owner = self.__users_db.get_signed_user(owner_id)
            if owner_id in team.owners:
                raise ValueError("Already exist in team")
            if owner.team is not None:
                raise ValueError('User {} already in a team'.format(owner.user_name))
            team.add_team_owner(owner_id)
            owner.team = team_name
            self.__users_db.update_signed_user(owner)
            self.__dictionary_team.update(team)
            Logger.info_log("{0}: Owner {1} was added to {2}".format(user_id, owner.name, team_name))
        except Exception as err:
            Logger.error_log("{0}:".format(user_id) + err.__str__())
            raise err

    def remove_owner_from_team(self, team_name: str, rem_owner_id, user_id=""):
        try:
            team = self.get_team(team_name, "")
            rem_owner = self.__users_db.get_signed_user(rem_owner_id)
            if rem_owner_id not in team.owners:
                raise ValueError("The user is not a owner in this team")

            team.remove_team_owner(rem_owner_id)
            try:
                self.cascade_remove(team, rem_owner.user_id)
            except Exception as err:
                raise Exception("Could not recursively delete all user appointments\n" + str(err))
            finally:
                rem_owner.team = None
                self.__users_db.update_signed_user(rem_owner)
                self.__dictionary_team.update(team)
            Logger.info_log("{0}: Owner {1} was removed from {2}".format(user_id, rem_owner.name, team_name))
        except Exception as err:
            Logger.error_log("{0}:".format(user_id) + err.__str__())
            raise err

    """ Remove all team members assigned by given team member"""
    def cascade_remove(self, team, team_member_user_id):
        exception = ''

        for player_id in team.team_members:
            player = self.__users_db.get_signed_user(player_id)
            if player.role.assigned_by == team_member_user_id:
                try:
                    self.remove_team_member(player)
                except ValueError as err:
                    exception = exception + str(err) + '\n'
        for manager_id in team.managers:
            manager = self.__users_db.get_signed_user(manager_id)
            if manager.role.assigned_by == team_member_user_id:
                try:
                    self.remove_team_manager(manager)
                except ValueError as err:
                    exception = exception + str(err) + '\n'
        for owner_id in team.owners:
            owner = self.__users_db.get_signed_user(owner_id)
            if owner.role.assigned_by == team_member_user_id:
                try:
                    team.remove_team_owner(owner)
                except ValueError as err:
                    exception = exception + str(err) + '\n'

        if exception is not '':
            raise Exception(exception)

    """ Set stadium To team """

    def set_stadium_to_team(self, team_name: str, stadium, user_id=""):
        try:
            team = self.get_team(team_name, "")
            team.stadium = stadium
            self.__dictionary_team.update(team)
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
            self.__dictionary_team.update(team)
            Logger.info_log("{0}: Add income to team {1} : {2}, {3}".format(user_id,team_name, amount ,description))
        except Exception as err:
            Logger.error_log("{0}:".format(user_id) + err.__str__())
            raise err

    """ Add expanse to a team"""""

    # test:test_team__budget

    def add_expanse_to_team(self, team_name, amount: int, description: str, user_id=""):
        try:
            team = self.get_team(team_name, "")
            if not team.add_expense(amount, description):
                raise ValueError("Team balance cant be negative")
            self.__dictionary_team.update(team)
            Logger.info_log("{0}: Add expanse to team {1} : {2}, {3}".format(user_id,team_name, amount ,description))
        except Exception as err:
            Logger.error_log("{0}:".format(user_id) + err.__str__())
            raise err

    """ Set Number To Player """

    def set_number_to_player(self, team_user_id, number: str, user_id=""):
        try:
            team_user = self.__users_db.get_signed_user(team_user_id)
            team_user.role.number = number
            self.__users_db.update_signed_user(team_user)
        except Exception as err:
            Logger.error_log("{0}:".format(user_id) + err.__str__())
            raise err

    """ Set Position To Player """

    def set_position_to_player(self, team_user_id, position: str, user_id=""):
        try:
            team_user = self.__users_db.get_signed_user(team_user_id)
            team_user.role.position = position
            self.__users_db.update_signed_user(team_user)
        except Exception as err:
            Logger.error_log("{0}:".format(user_id) + err.__str__())
            raise err

    def check_if_free_team_user(self, team_user_id):
        team_user = self.__users_db.get_signed_user(team_user_id)
        if team_user.team is None:
            return True
        else:
            return False
