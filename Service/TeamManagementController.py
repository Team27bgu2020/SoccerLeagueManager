"""Oscar"""
from Domain.TeamManager import TeamManager
from DataBases.TeamDB import TeamDB
from Domain import TeamUser
from Domain.Role import Role
from Domain.Team import Team
from Domain.TeamOwner import TeamOwner


class TeamManagementController:

    def __init__(self, team_db):
        self.__dictionary_team = team_db

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

    def remove_team_members_from_team(self, team_name: str, team_members: list):
        team = self.get_team(team_name)
        team.remove_team_members(team_members)

    """ Get team managers """

    def get_team_managers(self, team_name: str):
        team = self.get_team(team_name)
        return team.managers

    """ Add Manager To team """

    def add_manager_to_team(self, team_name: str, manager: TeamUser):

        team = self.get_team(team_name)
        if manager in team.managers:
            raise ValueError("Already exist in team")
        team.add_team_manager(manager)

    """ Remove Manager from team """

    def remove_manager_from_team(self, team_name: str, manager: TeamUser):
        team = self.get_team(team_name)
        if manager not in team.managers:
            raise ValueError("doesnt have manager")
        team.remove_team_manager(manager)


    """ Get team owners """

    # test:test_get_set_remove_team_owner

    def get_team_owners(self, team_name: str):
        team = self.get_team(team_name)
        return team.owners

    """ Add role player to Owner  """

    def add_role_player_to_owner(self, owner: TeamUser, role: Role):
        if owner.role.role_player is not None:
            raise ValueError("already has role player")
        owner.role.role_player = role

    """ remove role from owner  """
    def remove_role_player_from_owner(self, owner: TeamUser):
        if owner.role.role_player is None:
            raise ValueError("Owner dont Have player role")
        owner.role.role_player = None

    """ Add role coach to Owner  """

    def add_role_coach_to_owner(self, owner: TeamUser, role: Role):
        if owner.role.role_coach is not None:
            raise ValueError("already has role coach")
        owner.role.role_coach = role

    """ remove coach from owner  """

    def remove_role_coach_from_owner(self, owner: TeamUser):
        if owner.role.role_coach is None:
            raise ValueError("Owner dont Have player role")
        owner.role.role_coach = None

    """ Add manager role player to Owner  """

    def add_role_manager_to_owner(self, owner: TeamUser, role: Role):
        if owner.role.role_manager is not None:
            raise ValueError("Owner already has manager role ")
        owner.role.role_manager = role

    """ remove manager role from owner  """

    def remove_role_from_owner(self, owner: TeamUser):
        if owner.role.role_manager is None:
            raise ValueError("Owner dont Have  manager role")
        owner.role.role_manager = None

    """ Remove Owner from team, By UC 6.3! """
    """ This function removing assigned team owner by the owner and removing his roles"""
    """Talk with OSCAR"""

    """ Add Owner To team """

    def add_owner_to_team(self, team_name: str, owner: TeamUser):
        team = self.get_team(team_name)
        if owner in team.owners:
            raise ValueError("Already exist in team")
        team.add_team_owner(owner)

    def remove_owner_from_team(self, team_name: str, rem_owner: TeamUser):
        team = self.get_team(team_name)
        if rem_owner not in team.owners:
            raise ValueError("doesnt have manager")
        team.remove_team_manager(rem_owner)


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
