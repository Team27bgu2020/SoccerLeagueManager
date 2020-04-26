"""Oscar"""
from Domain.TeamManager import TeamManager
from DataBases.TeamDB import TeamDB
from Domain import TeamUser
from Domain.Role import Role
from Domain.Team import Team


class TeamManagementController:

    def __init__(self):
        self.__dictionary_team = TeamDB()

    @property
    def dictionary_team(self):
        return self.__dictionary_team

    """Get the team, and check if not None"""

    # test: test_get_team

    def get_team(self, team_name: str):
        team = self.__dictionary_team.get(team_name)
        return team

    """Open a new team, and add it to the team DB-dictionary"""

    # test:test_open_new_team

    def open_new_team(self, team_name: str, owner: TeamUser):
        if owner is None:
            # To add Team User Check has role Owner!!!!
            raise ValueError("Team Can not be created without owner")
        new_team = Team(team_name)
        new_team.owner = owner
        self.__dictionary_team.add(new_team)

    """Add a team existing object, and add it to the team DB-dictionary"""

    # test: test_get_team

    def add_existing_team(self, team):
        self.__dictionary_team.add(team)

    """ ReOpening closed team"""

    # test: test_reopen_team

    def reopen_team(self, team_name: str):
        team = self.get_team(team_name)
        team.open_team()

    """Closing team, need to check what to do here"""

    # test: test_reopen_team

    def close_team(self, team_name: str):
        team = self.get_team(team_name)
        team.close_team()

    """Add team member to a team"""

    # test:test_add_team_member_to_team

    def add_team_member_to_team(self, team_name: str, team_member: TeamUser):
        team = self.get_team(team_name)
        team.add_team_member(team_member)

    """Add team a list members to a team"""

    # test:test_add_team_member_to_team

    def add_team_members_to_team(self, team_name: str, team_members: list):
        team = self.get_team(team_name)
        team.add_team_members(team_members)

    """Delete team member from a team"""

    # test:test_add_team_member_to_team

    def remove_team_member_from_team(self, team_name: str, team_member: TeamUser):
        team = self.get_team(team_name)
        team.remove_team_member(team_member)

    """Delete team a list members from a team"""

    # test:test_add_team_member_to_team

    def remove_team_members_from_team(self, team_name: str, team_members: list):
        team = self.get_team(team_name)
        team.remove_team_members(team_members)

    """ Get team manager """

    # test:test_get_set_remove_team|_manager

    def get_team_manager(self, team_name: str):
        team = self.get_team(team_name)
        return team.manager

    """ Set Manager To team """

    # test:test_get_set_remove_team_manager

    def set_manager_to_team(self, team_name: str, manager: TeamUser):

        team = self.get_team(team_name)
        if team.manager is not None:
            raise ValueError("already has manager")
        if manager.role is not None:
            raise ValueError("Couldn't be set as manager")
        manager.role = TeamManager()
        team.manager = manager

    """ Remove Manager from team """

    # test:test_get_set_remove_team_manager

    def remove_manager_from_team(self, team_name: str):
        team = self.get_team(team_name)
        if team.manager is None:
            raise ValueError("doesnt have manager")
        team.manager.team = None
        team.manager.role = None
        team.manager = None


    """ Get team owner """

    # test:test_get_set_remove_team_owner

    def get_team_owner(self, team_name: str):
        team = self.get_team(team_name)
        return team.owner

    """ Set Owner To team """

    # test:test_get_set_remove_team_owner

    def set_owner_to_team(self, team_name: str, owner: TeamUser):
        team = self.get_team(team_name)
        team.owner = owner

    """ Add role player to Owner  """

    def add_role_to_owner(self, owner: TeamUser, role: Role):
        owner.role.add_role(role)

    """ remove role from owner  """

    def remove_role_from_owner(self, owner: TeamUser, role: Role):
        owner.role.remove_role(role)

    """ Remove Owner from team, By UC 6.3! """
    """ This function removing assigned team owner by the owner and removing his roles"""
    """Talk with OSCAR"""

    # test:test_get_set_remove_team_owner

    def remove_owner_from_team(self, team_name: str, rem_owner: TeamUser):
        rem_owner.role.remove_roles()
        team = self.get_team(team_name)
        team.owner = None

    def set__additional_owner_from_team(self, team_name: str, additional_owner: TeamUser):
        team = self.get_team(team_name)
        if team.additional_owner is not None:
            raise ValueError("already has manager")
        if additional_owner.role is not None:
            raise ValueError("Couldn't be set as additional owner")
        team.additional_owner = additional_owner

    def remove_additional_owner_from_team(self, team_name: str, rem_owner: TeamUser):
        rem_owner.remove_roles()
        team = self.get_team(team_name)
        if team.additional_owner is None:
            raise ValueError("doesnt have manager")
        team.additional_owner.team = None
        team.additional_owner.role = None
        team.additional_owner = None

    """ Set stadium To team """

    def set_stadium_to_team(self, team_name: str, stadium):
        team = self.get_team(team_name)
        team.stadium = stadium

    """ Get team stadium """

    def get_team_stadium(self, team_name: str):
        team = self.get_team(team_name)
        return team.stadium

    """ Get team income"""

    # test:test_team__budget

    def get_team_incomes(self, team_name: str):
        team = self.get_team(team_name)
        return team.incomes

    """ Get team expanses"""

    # test:test_team__budget

    def get_team_expanses(self, team_name: str):
        team = self.get_team(team_name)
        return team.expanses

    """ Get team transactions"""

    # test:test_team__budget

    def get_team_transactions(self, team_name: str):
        team = self.get_team(team_name)
        return team.transactions

    """ Get team current budget"""

    # test:test_team__budget

    def get_team_budget(self, team_name: str):
        team = self.get_team(team_name)
        return team.budget

    """ Add income to a team"""""

    # test:test_team__budget

    def add_income_to_team(self, team_name, amount: int, description: str):
        team = self.get_team(team_name)
        team.add_income(amount, description)

    """ Add expanse to a team"""""

    # test:test_team__budget

    def add_expanse_to_team(self, team_name, amount: int, description: str):
        team = self.get_team(team_name)
        team.add_expanse(amount, description)

    """ Set Number To Player """

    def set_number_to_player(self, team_user: TeamUser, number: str):
        team_user.role.number = number

    """ Set Position To Player """

    def set_position_to_player(self, team_user: TeamUser, position: str):
        team_user.role.position = position

    """ Set qualification To Player """

    def set_qualification_to_player(self, team_user: TeamUser, qualification: str):
        team_user.role.qualification = qualification

    def check_if_free_team_user(self, team_user: TeamUser):
        if team_user.team is None:
            return True
        else:
            return False
