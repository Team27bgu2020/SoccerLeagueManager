import hashlib
from typing import Any

from Domain.Fan import Fan
from Domain.Referee import Referee
from Domain.SystemAdmin import SystemAdmin
from Domain.TeamUser import TeamUser
from Domain.Player import Player
from Domain.Coach import Coach
from Domain.TeamManager import TeamManager
from Domain.TeamOwner import TeamOwner
from Domain.UnionRepresentor import UnionRepresentor
from DataBases.UserDB import UserDB

""" Created By Roman"""


class SignedUserController:

    def __init__(self, user_db):
        self.__user_data_base = user_db
        self.__ID = self.__user_data_base.get_id_counter()

    """ delete user by user name """

    def delete_signed_user(self, user_id):
        if self.__user_data_base.is_sign_user(user_id):
            if type(self.__user_data_base.get_signed_user(user_id)) is SystemAdmin:
                """Check if there is more admins in  system if no return false"""
                if self.__user_data_base.get_number_of_admins() < 2:
                    raise AssertionError("System has to have at least one system admin")
            self.__user_data_base.delete_user(user_id)
            return True
        else:
            return False

    def show_all_users(self):

        return self.__user_data_base.get_all_signed_users

    def confirm_user(self, user_name, password):
        """
        @param user_name: for confirm
        @param password: for confirm
        @return: if the user exist - the function will return the type of the user
        """
        try:
            user = self.__user_data_base.get_signed_user_by_user_name(user_name)
        except Exception as err:
            return False

        if user.password == str(hashlib.sha256(password.encode()).hexdigest()):
            if type(user) is not TeamUser:
                return str(type(user).__name__)
            return str(type(user.role).__name__)

    def get_user_by_id(self, user_id):
        return self.__user_data_base.get_signed_user(user_id)

    def get_user_by_name(self, user_name):
        return self.__user_data_base.get_signed_user_by_user_name(user_name)

    def get_all_signed_users(self):
        return self.__user_data_base.get_all_signed_users()

    """ Edit all of the personal data of signed user """
    def edit_personal_data(self, user_id, user_name, password, name, birth_date):

        user = self.__user_data_base.get_signed_user(user_id)
        user.edit_personal_data(user_name, password, name, birth_date)
        self.__user_data_base.update_signed_user(user)

    """Editing personal info"""

    def edit_personal_name(self, user_id, new_name):
        if self.__user_data_base.is_sign_user(user_id):
            signed_user = self.__user_data_base.get_signed_user(user_id)
            signed_user.name = new_name
            self.__user_data_base.update_signed_user(signed_user)
            return True
        else:
            return False

    def edit_personal_birth_date(self, user_id, new_birth_date):
        if self.__user_data_base.is_sign_user(user_id):
            signed_user = self.__user_data_base.get_signed_user(user_id)
            signed_user.birth_date = new_birth_date
            self.__user_data_base.update_signed_user(signed_user)
            return True
        else:
            return False

    def edit_personal_password(self, user_id, old_password, new_password):
        if self.confirm_user(user_id, old_password):
            signed_user = self.__user_data_base.get_signed_user(user_id)
            signed_user.password = str(hashlib.sha256(new_password.encode()).hexdigest())
            self.__user_data_base.update_signed_user(signed_user)
            return True
        else:
            return False

    """ Adding users by type =>"""

    def add_fan(self, user_name, password, name, birth_date):
        """
        add`s fan to DB - the fan is signed user
        @param user_name: string
        @param password: given string before security algorithm
        @param name: name - no numbers
        @param birth_date: date Type only!
        @return: no return
        """
        fan = Fan(user_name, password, name, birth_date, self.__ID)
        self.__user_data_base.add_signed_user(fan, 'fan')
        self.update_counter()

    def add_system_admin(self, user_name, password, name, birth_date):
        admin = SystemAdmin(user_name, password, name, birth_date, self.__ID)
        self.__user_data_base.add_signed_user(admin, 'system_admin')
        self.update_counter()

    def add_referee(self, qualification, user_name, password, name, birth_date):
        referee_user = Referee(qualification, user_name, password, name, birth_date, self.__ID)
        self.__user_data_base.add_signed_user(referee_user, 'referee')
        self.update_counter()

    def add_union_representor(self, user_name, password, name, birth_date, salary):
        union_rep = UnionRepresentor(user_name, password, name, birth_date, self.__ID, salary)
        self.__user_data_base.add_signed_user(union_rep, 'union_representor')
        self.update_counter()

    def add_player(self, user_name, password, name, birth_date, assigned_by=None, position=None, number=0):
        player_role = Player(assigned_by, position, number)
        player = TeamUser(user_name, password, name, birth_date, self.__ID, role=player_role)
        self.__user_data_base.add_signed_user(player, 'player')
        self.update_counter()

    def add_coach(self, user_name, password, name, birth_date, assigned_by=None, qualifications=None):
        coach_role = Coach(assigned_by, qualifications)
        coach = TeamUser(user_name, password, name, birth_date, self.__ID, role=coach_role)
        self.__user_data_base.add_signed_user(coach, 'coach')
        self.update_counter()

    def add_team_manager(self, user_name, password, name, birth_date, assigned_by=None,
                         bool_open_close=False, bool_accounting=False, bool_add_remove=False, bool_set_permission=False):
        team_manager_role = TeamManager(assigned_by, bool_open_close, bool_accounting,
                                        bool_add_remove, bool_set_permission)
        team_manager = TeamUser(user_name, password, name, birth_date, self.__ID, role=team_manager_role)
        self.__user_data_base.add_signed_user(team_manager, 'team_manager')
        self.update_counter()

    def add_team_owner(self, user_name, password, name, birth_date, assigned_by=None, additional_roles=[]):
        team_owner_role = TeamOwner(assigned_by, additional_roles)
        team_owner = TeamUser(user_name, password, name, birth_date, self.__ID, role=team_owner_role)
        self.__user_data_base.add_signed_user(team_owner, 'team_owner')
        self.update_counter()

    def update_counter(self):
        self.__ID += 1
        self.__user_data_base.update_id_counter(self.__ID)
