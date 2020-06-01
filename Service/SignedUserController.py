import hashlib

from Domain.Coach import Coach
from Domain.Fan import Fan
from Domain.Player import Player
from Domain.Referee import Referee
from Domain.SystemAdmin import SystemAdmin
from Domain.TeamManager import TeamManager
from Domain.TeamOwner import TeamOwner
from Domain.TeamUser import TeamUser
from Domain.UnionRepresentor import UnionRepresentor
from Log.Logger import *

""" Created By Roman"""


class SignedUserController:

    def __init__(self, user_db):
        self.__user_data_base = user_db
        self.__ID = self.__user_data_base.get_id_counter()
        Logger.start_logger()

    """ delete user by user name """

    def delete_signed_user(self, user_id, using_user_id=""):
        try:
            if self.__user_data_base.is_sign_user(user_id):
                if type(self.__user_data_base.get_signed_user(user_id)) is SystemAdmin:
                    """Check if there is more admins in  system if no return false"""
                    if self.__user_data_base.get_number_of_admins() < 2:
                        raise AssertionError("System has to have at least one system admin")
                self.__user_data_base.delete_user(user_id)
                Logger.info_log("{0}:".format(using_user_id) + "deleted user {0}".format(user_id))
                return True
            else:
                return False
        except Exception as err:
            Logger.error_log("{0}:".format(using_user_id) + err.__str__())
            raise err

    def show_all_users(self, using_user_id=""):
        try:
            Logger.info_log("{0}:".format(using_user_id) + "got all users")
            return self.__user_data_base.get_all_signed_users
        except Exception as err:
            Logger.error_log("{0}:".format(using_user_id) + err.__str__())
            raise err

    def confirm_user(self, user_name, password, using_user_id=""):
        """
        @param user_name: for confirm
        @param password: for confirm
        @return: if the user exist - the function will return the type of the user
        """
        try:
            user = self.__user_data_base.get_signed_user_by_user_name(user_name)
        except Exception as err:
            Logger.error_log("{0}:".format(using_user_id) + err.__str__())
            return False
        try:
            if user.password == str(hashlib.sha256(password.encode()).hexdigest()):
                Logger.info_log("{0}:".format(using_user_id) + " user {0} was confirmed".format(user.user_name))
                if type(user) is not TeamUser:
                    return str(type(user).__name__)
                return str(type(user.role).__name__)
        except Exception as err:
            Logger.error_log("{0}:".format(using_user_id) + err.__str__())
            raise err

    def get_user_by_id(self, user_id, using_user_id=""):
        try:
            Logger.info_log("{0}:".format(using_user_id) + "got user {0} by id".format(user_id))
            return self.__user_data_base.get_signed_user(user_id)
        except Exception as err:
            Logger.error_log("{0}:".format(using_user_id) + err.__str__())
            raise err

    def get_user_by_name(self, user_name, using_user_id=""):
        try:
            Logger.info_log("{0}:".format(using_user_id) + "got user {0} by name".format(user_name))
            return self.__user_data_base.get_signed_user_by_user_name(user_name)
        except Exception as err:
            Logger.error_log("{0}:".format(using_user_id) + err.__str__())
            raise err

    def get_all_signed_users(self, using_user_id=""):
        try:
            Logger.info_log("{0}:".format(using_user_id) + "got all signed users")
            return self.__user_data_base.get_all_signed_users()
        except Exception as err:
            Logger.error_log("{0}:".format(using_user_id) + err.__str__())
            raise err

    """ Edit all of the personal data of signed user """

    def edit_personal_data(self, user_id, user_name, password, name, birth_date, using_user_id=""):
        try:
            user = self.__user_data_base.get_signed_user(user_id)
            user.edit_personal_data(user_name, password, name, birth_date)
            self.__user_data_base.update_signed_user(user)
            Logger.info_log("{0}:".format(using_user_id) + " user {0} data edited".format(user_id))
        except Exception as err:
            Logger.error_log("{0}:".format(using_user_id) + err.__str__())
            raise err

    """Editing personal info"""

    def edit_personal_name(self, user_id, new_name, using_user_id=""):
        try:
            if self.__user_data_base.is_sign_user(user_id):
                signed_user = self.__user_data_base.get_signed_user(user_id)
                signed_user.name = new_name
                self.__user_data_base.update_signed_user(signed_user)
                Logger.info_log("{0}:".format(using_user_id) + " user {0} name edited".format(user_id))
                return True
            else:
                return False
        except Exception as err:
            Logger.error_log("{0}:".format(using_user_id) + err.__str__())
            raise err

    def edit_personal_birth_date(self, user_id, new_birth_date, using_user_id=""):
        try:
            if self.__user_data_base.is_sign_user(user_id):
                signed_user = self.__user_data_base.get_signed_user(user_id)
                signed_user.birth_date = new_birth_date
                self.__user_data_base.update_signed_user(signed_user)
                Logger.info_log("{0}:".format(using_user_id) + " user {0} birth date edited".format(user_id))
                return True
            else:
                return False
        except Exception as err:
            Logger.error_log("{0}:".format(using_user_id) + err.__str__())
            raise err

    def edit_personal_password(self, user_id, old_password, new_password, using_user_id=""):
        try:
            if self.confirm_user(user_id, old_password):
                signed_user = self.__user_data_base.get_signed_user(user_id)
                signed_user.password = str(hashlib.sha256(new_password.encode()).hexdigest())
                self.__user_data_base.update_signed_user(signed_user)
                Logger.info_log("{0}:".format(using_user_id) + " user {0} password changed".format(user_id))
                return True
            else:
                return False
        except Exception as err:
            Logger.error_log("{0}:".format(using_user_id) + err.__str__())
            raise err

    """ Adding users by type =>"""

    def add_fan(self, user_name, password, name, birth_date, using_user_id=""):
        """
        add`s fan to DB - the fan is signed user
        @param using_user_id:
        @param user_name: string
        @param password: given string before security algorithm
        @param name: name - no numbers
        @param birth_date: date Type only!
        @return: no return
        """
        try:
            fan = Fan(user_name, password, name, birth_date, self.__ID)
            self.__user_data_base.add_signed_user(fan, 'fan')
            self.update_counter()
            Logger.info_log("{0}".format(using_user_id) + "add fan : {0}".format(user_name))
        except Exception as err:
            Logger.error_log("{0}:".format(using_user_id) + err.__str__())
            raise err

    def add_system_admin(self, user_name, password, name, birth_date, using_user_id=""):

        try:
            admin = SystemAdmin(user_name, password, name, birth_date, self.__ID)
            self.__user_data_base.add_signed_user(admin, 'system_admin')
            self.update_counter()
            Logger.info_log("{0}:".format(using_user_id) + "add system admin : {0}".format(user_name))
        except Exception as err:
            Logger.error_log("{0}:".format(using_user_id) + err.__str__())
            raise err

    def add_referee(self, qualification, user_name, password, name, birth_date, using_user_id=""):
        try:
            referee_user = Referee(qualification, user_name, password, name, birth_date, self.__ID)
            self.__user_data_base.add_signed_user(referee_user, 'referee')
            self.update_counter()
            Logger.info_log("{0}:".format(using_user_id) + "add referee : {0}".format(user_name))
        except Exception as err:
            Logger.error_log("{0}:".format(using_user_id) + err.__str__())
            raise err

    def add_union_representor(self, user_name, password, name, birth_date, salary=0, using_user_id=""):
        try:
            union_rep = UnionRepresentor(user_name, password, name, birth_date, self.__ID, salary)
            self.__user_data_base.add_signed_user(union_rep, 'union_representor')
            self.update_counter()
            Logger.info_log("{0}:".format(using_user_id) + "add Union Representor : {0}".format(user_name))
        except Exception as err:
            Logger.error_log("{0}:".format(using_user_id) + err.__str__())
            raise err

    def add_player(self, user_name, password, name, birth_date, assigned_by=None, position=None, number=0,
                   using_user_id=""):
        try:
            player_role = Player(assigned_by, position, number)
            player = TeamUser(user_name, password, name, birth_date, self.__ID, role=player_role)
            self.__user_data_base.add_signed_user(player, 'player')
            self.update_counter()
            Logger.info_log("{0}:".format(using_user_id) + "add player: {0}".format(user_name))
        except Exception as err:
            Logger.error_log("{0}:".format(using_user_id) + err.__str__())
            raise err

    def add_coach(self, user_name, password, name, birth_date, assigned_by=None, qualifications=None, using_user_id=""):
        try:
            coach_role = Coach(assigned_by, qualifications)
            coach = TeamUser(user_name, password, name, birth_date, self.__ID, role=coach_role)
            self.__user_data_base.add_signed_user(coach, 'coach')
            self.update_counter()
            Logger.info_log("{0}:".format(using_user_id) + "add coach: {0}".format(user_name))
        except Exception as err:
            Logger.error_log("{0}:".format(using_user_id) + err.__str__())
            raise err

    def add_team_manager(self, user_name, password, name, birth_date, assigned_by=None,
                         bool_open_close=False, bool_accounting=False, bool_add_remove=False,
                         bool_set_permission=False, using_user_id=""):
        try:
            team_manager_role = TeamManager(assigned_by, bool_open_close, bool_accounting,
                                            bool_add_remove, bool_set_permission)
            team_manager = TeamUser(user_name, password, name, birth_date, self.__ID, role=team_manager_role)
            self.__user_data_base.add_signed_user(team_manager, 'team_manager')
            self.update_counter()
            Logger.info_log("{0}:".format(using_user_id) + "add manager: {0}".format(user_name))
        except Exception as err:
            Logger.error_log("{0}:".format(using_user_id) + err.__str__())
            raise err

    def add_team_owner(self, user_name, password, name, birth_date, assigned_by=None, additional_roles=[], using_user_id=""):
        try:
            team_owner_role = TeamOwner(assigned_by, additional_roles)
            team_owner = TeamUser(user_name, password, name, birth_date, self.__ID, role=team_owner_role)
            self.__user_data_base.add_signed_user(team_owner, 'team_owner')
            self.update_counter()
            Logger.info_log("{0}:".format(using_user_id) + "add owner: {0}".format(user_name))
        except Exception as err:
            Logger.error_log("{0}:".format(using_user_id) + err.__str__())
            raise err

    def update_counter(self):
        self.__ID += 1
        self.__user_data_base.update_id_counter(self.__ID)
