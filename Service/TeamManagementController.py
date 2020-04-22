"""Oscar"""
from Domain import TeamUser, TeamOwner
from Domain.Team import Team


class TeamManagementController:

    def __init__(self):
        self.__dictionary_team = {}

    """Get the team, and check if not None"""

    def get_team(self, team_name: str):
        team = self.__dictionary_team[team_name]
        if team is None:
            raise Exception("Team Doesnt exist")
        return team

    """Open a new team, and add it to the team DB-dictionary"""

    def open_new_team(self, team_name: str, field: str):
        if not isinstance(team_name, str) or not isinstance(field, str):
            raise TypeError("Should be string")
        self.__dictionary_team[team_name] = Team(team_name, field)

    """ ReOpening closed team"""

    def reopen_team(self, team_name: str):
        if not isinstance(team_name, str):
            raise TypeError("Should be string")
        team = self.get_team(team_name)
        team.open_team()

    """Closing team, need to check what to do here"""

    def close_team(self, team_name: str):
        if not isinstance(team_name, str):
            raise TypeError("Should be string")
        team = self.get_team(team_name)
        team.close_team()

    """Add team member to a team"""

    def add_team_member_to_team(self, team_name: str, team_member: TeamUser):
        if not isinstance(team_name, str):
            raise TypeError("Should be string")
        team = self.get_team(team_name)
        team.add_team_member(team_member)

    """Add team a list members to a team"""

    def add_list_team_members_to_team(self, team_name: str, team_members: list):
        if not isinstance(team_name, str):
            raise TypeError("Should be string")
        team = self.get_team(team_name)
        team.add_team_members(team_members)

    """Delete team member from a team"""

    def delete_team_member_from_team(self, team_name: str, team_member: TeamUser):
        if not isinstance(team_name, str):
            raise TypeError("Should be string")
        team = self.get_team(team_name)
        team.remove_team_member(team_member)

    """Delete team a list members from a team"""

    def delete_list_team_members_to_team(self, team_name: str, team_members: list):
        if not isinstance(team_name, str):
            raise TypeError("Should be string")
        team = self.get_team(team_name)
        team.remove_team_members(team_members)

    """ Get team manager """

    def get_team_manager(self, team_name: str):
        if not isinstance(team_name, str):
            raise TypeError("Should be string")
        team = self.get_team(team_name)
        return team.manger

    """ Get team owner """

    def get_team_owner(self, team_name: str):
        if not isinstance(team_name, str):
            raise TypeError("Should be string")
        team = self.get_team(team_name)
        return team.owner

    """ Set Owner To team """

    def set_owner_to_team(self, team_name: str, owner: TeamUser):
        if not isinstance(team_name, str):
            raise TypeError("Should be string")
        TeamUser.type_check(owner)
        # ??? q1:check for TeamOwner
        team = self.get_team(team_name)
        team.set_owner(owner)

    """ Remove Owner from team """

    def remove_owner_to_team(self, team_name: str):
        if not isinstance(team_name, str):
            raise TypeError("Should be string")
        team = self.get_team(team_name)
        team.set_manager(None)

    """ Set Manager To team """

    def set_manager_to_team(self, team_name: str, manager: TeamUser):
        if not isinstance(team_name, str):
            raise TypeError("Should be string")
        TeamUser.type_check(manager)
        # ??? q2:Check for TeamManger
        team = self.get_team(team_name)
        team.set_manager(manager)

    """ Remove Manager from team """

    def remove_manager_to_team(self, team_name: str):
        if not isinstance(team_name, str):
            raise TypeError("Should be string")
        team = self.get_team(team_name)
        team.set_manager(None)

    """ Set Field To team """

    def set_field_to_team(self, team_name: str, field: str):
        if not isinstance(team_name, str):
            raise TypeError("Should be string")
        team = self.get_team(team_name)
        team.set_field(field)

    """ Get team income"""

    def get_team_incomes(self, team_name: str):
        if not isinstance(team_name, str):
            raise TypeError("Should be string")
        team = self.get_team(team_name)
        return team.incomes

    """ Get team expanses"""

    def get_team_expanses(self, team_name: str):
        if not isinstance(team_name, str):
            raise TypeError("Should be string")
        team = self.get_team(team_name)
        return team.expanses

    """ Get team transactions"""

    def get_team_transactions(self, team_name: str):
        if not isinstance(team_name, str):
            raise TypeError("Should be string")
        team = self.get_team(team_name)
        return team.transactions

    """ Get team current budget"""

    def get_team_current(self, team_name: str):
        if not isinstance(team_name, str):
            raise TypeError("Should be string")
        team = self.get_team(team_name)
        return team.current

    """ Add income to a team"""""

    def add_income_to_team(self, team_name, amount: int, description: str):
        if not isinstance(team_name, str):
            raise TypeError("Should be string")
        team = self.get_team(team_name)
        team.add_income(amount, description)

    """ Add expanse to a team"""""

    def add_expanse_to_team(self, team_name, amount: int, description: str):
        if not isinstance(team_name, str):
            raise TypeError("Should be string")
        team = self.get_team(team_name)
        team.add_expanse(amount, description)
