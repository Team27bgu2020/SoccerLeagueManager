import hashlib
from typing import Any

from Domain.Coach import Coach
from Domain.Fan import Fan
from Domain.Player import Player
from Domain.Referee import Referee
from Domain.SystemAdmin import SystemAdmin
from Domain.SignedUser import SignedUser
from Domain.Guest import Guest
from DataBases.UserDB import UserDB
from Domain.TeamManager import TeamManager
from Domain.TeamOwner import TeamOwner
from Domain.TeamUser import TeamUser
from Log.Logger import *
from Domain.UnionRepresentor import UnionRepresentor


""" Created By Roman"""


class SignedUserController:

    def __init__(self, user_db):
        self.__user_data_base = user_db
        self.__ID = 0
        Logger.start_logger()

    """ Add new signed user to DB """

    def add_signed_user(self, user_name, password, name, birth_date, ip_address, user_id=""):
        """
        @param user_id:
        @param user_name:
        @param password:
        @param name:
        @param birth_date:
        @param ip_address:
        @return: add signed user to DB
        """
        try:
            self.__ID = self.__ID + 1
            new_signed_user = SignedUser(user_name, password, name, birth_date, ip_address, self.__ID)
            self.add_user(new_signed_user)
            Logger.info_log("{0}:".format(user_id) + "added user {0}".format(user_name))
        except Exception as err:
            Logger.error_log("{0}:".format(user_id) + err.__str__())
            raise err

    def add_guest(self, ip, user_id=""):
        try:
            self.__ID = self.__ID + 1
            new_guest = Guest(ip, self.__ID)
            self.add_user(new_guest)
            Logger.info_log("{0}:".format(user_id) + "added guest with ip {0}".format(ip))
        except Exception as err:
            Logger.error_log("{0}:".format(user_id) + err.__str__())
            raise err

    def add_Team_User(self, user_name, password, name, birth_date, ip_address, user_id=""):
        try:
            self.__ID = self.__ID + 1
            new_signed_user = SignedUser(user_name, password, name, birth_date, ip_address, self.__ID)
            self.add_user(new_signed_user)
            Logger.info_log("{0}:".format(user_id) + "added team user {0}".format(user_name))
        except Exception as err:
            Logger.error_log("{0}:".format(user_id) + err.__str__())
            raise err

    """ delete user by user name """

    def delete_signed_user(self, user_name, user_id=""):
        try:
            if self.__user_data_base.is_sign_user(user_name):
                if type(self.__user_data_base.get_signed_user(user_name)) is SystemAdmin:
                    """Check if there is more admins in  system if no return false"""
                    if (self.number_of_admins() < 2):
                        raise AssertionError
                self.__user_data_base.delete_signed_user(user_name)
                Logger.info_log("{0}:".format(user_id) + "deleted user {0}".format(user_name))
                return True
            else:
                return False
        except Exception as err:
            Logger.error_log("{0}:".format(user_id) + err.__str__())
            raise err

    def delete_guest(self, ip, user_id=""):
        try:
            if self.__user_data_base.is_guest_in_data(ip):
                self.__user_data_base.delete_guest(ip)
                Logger.info_log("{0}:".format(user_id) + "deleted guest {0}".format(ip))
                return True
            else:
                return False
        except Exception as err:
            Logger.error_log("{0}:".format(user_id) + err.__str__())
            raise err

    def show_all_users(self, user_id=""):
        """
        @return: 2 values: 1. signed users  2. guests
        """
        try:
            return self.get_signed_users(), self.get_guests()
            Logger.info_log("{0}:".format(user_id) + "got all users")
        except Exception as err:
            Logger.error_log("{0}:".format(user_id) + err.__str__())
            raise err

    def add_user(self, user, user_id=""):
        """
        Adding users to dictionary by type
        @param user_id:
        @param user: can be guest or signed user
        """
        try:
            if isinstance(user, SignedUser):
                if self.__user_data_base.is_sign_user(user.user_name):
                    self.__ID = self.__ID - 1
                else:
                    self.__user_data_base.add_sign_user(user)
                    Logger.info_log("{0}:".format(user_id) + "added user {0}".format(user.user_name))

            elif type(user) is Guest:
                if self.__user_data_base.is_guest_in_data(user.user_ip):
                    self.__ID = self.__ID - 1
                else:
                    self.__user_data_base.add_guest(user)
                    Logger.info_log("{0}:".format(user_id) + "added guest with ip {0}".format(user.ip))
            else:
                """ Not a guest and not a signed user """
                raise TypeError("Trying to add not a guest and not a signed user")

        except Exception as err:
            Logger.error_log("{0}:".format(user_id) + err.__str__())
            raise err

    def confirm_user(self, user_name, password, user_id=""):
        """
        @param user_id:
        @param user_name: for confirm
        @param password: for confirm
        @return: if the user exist - the function will return the type of the user
        """
        try:
            user = self.__user_data_base.get_signed_user(user_name)
            if user is None:
                return False

            if user.password == str(hashlib.sha256(password.encode()).hexdigest()):
                Logger.info_log("{0}:".format(user_id) + " user {0} was confirmed".format(user.user_name))
                return str(type(user).__name__)

            else:
                return False

        except Exception as err:
            Logger.error_log("{0}:".format(user_id) + err.__str__())
            raise err

    """ Edit all of the personal data of signed user """

    def edit_personal_data(self, user, user_name, password, name, birth_date, user_id=""):
        try:
            user.edit_personal_data(user_name, password, name, birth_date)
            Logger.info_log("{0}:".format(user_id) + " user {0} data edited".format(user.name))
        except Exception as err:
            Logger.error_log("{0}:".format(user_id) + err.__str__())
            raise err

    """Editing personal info"""

    def edit_personal_name(self, user_name, new_name, user_id=""):
        try:
            if self.__user_data_base.is_sign_user(user_name):
                signed_user = self.__user_data_base.get_signed_user(user_name)
                signed_user.name = new_name
                Logger.info_log("{0}:".format(user_id) + " user {0} name edited".format(user_name))
                return True
            else:
                return False
        except Exception as err:
            Logger.error_log("{0}:".format(user_id) + err.__str__())
            raise err

    def edit_personal_birth_date(self, user_name: str, new_birth_date, user_id=""):
        try:
            if self.__user_data_base.is_sign_user(user_name):
                signed_user = self.__user_data_base.get_signed_user(user_name)
                signed_user.birth_date = new_birth_date
                Logger.info_log("{0}:".format(user_id) + " user {0} birth date edited".format(user_name))
                return True
            else:
                return False
        except Exception as err:
            Logger.error_log("{0}:".format(user_id) + err.__str__())
            raise err

    def edit_personal_password(self, user_name, old_password, new_password, user_id=""):
        try:
            if self.confirm_user(user_name, old_password):
                signed_user = self.__user_data_base.get_signed_user(user_name)
                signed_user.password = str(hashlib.sha256(new_password.encode()).hexdigest())
                Logger.info_log("{0}:".format(user_id) + " user {0} password changed".format(user_name))
                return True
            else:
                return False
        except Exception as err:
            Logger.error_log("{0}:".format(user_id) + err.__str__())
            raise err

    def add_search(self, user_name, massage, user_id=""):
        try:
            self.__user_data_base.add_search(user_name, massage)
            Logger.info_log("{0}:".format(user_id) + "Searched: {0}".format(massage))
        except Exception as err:
            Logger.error_log("{0}:".format(user_id) + err.__str__())
            raise err

    def get_user(self, user_name, user_id=""):
        try:
            if user_name in self.__user_data_base.signed_users:
                Logger.info_log("{0}:".format(user_id) + "got user: {0}".format(user_name))
                return self.__user_data_base.signed_users[user_name]
            else:
                return None
        except Exception as err:
            Logger.error_log("{0}:".format(user_id) + err.__str__())
            raise err

    def get_signed_users(self, user_id=""):
        try:
            Logger.info_log("{0}:".format(user_id) + "got all signed users")
            return self.__user_data_base.signed_users

        except Exception as err:
            Logger.error_log("{0}:".format(user_id) + err.__str__())
            raise err

    def get_guests(self, user_id=""):
        try:
            Logger.info_log("{0}:".format(user_id) + "got guests")
            return self.__user_data_base.guests

        except Exception as err:
            Logger.error_log("{0}:".format(user_id) + err.__str__())
            raise err

    @property
    def user_data_base(self, user_id=""):
        return self.__user_data_base

    """ Adding users by type =>"""

    def add_fan_to_data(self, user_name, password, name, birth_date, ip_address, user_id=""):
        """
        add`s fan to DB - the fan is signed user
        @param user_id:
        @param user_name: string
        @param password: given string before security algorithm
        @param name: name - no numbers
        @param birth_date: date Type only!
        @param ip_address: ip of the user
        @return: no return
        """
        try:
            self.__ID = self.__ID + 1
            f = Fan(user_name, password, name, birth_date, ip_address, self.__ID)
            self.add_user(f)
            Logger.info_log("{0}:".format(user_id) + "add fan : {0}".format(user_name))
        except Exception as err:
            Logger.error_log("{0}:".format(user_id) + err.__str__())
            raise err

    """ When we init the signed controller the first user is system admin """

    def add_system_admin(self, user_name, password, name, birth_date, ip_address, user_id=""):
        try:
            self.__ID = self.__ID + 1
            admin = SystemAdmin(user_name, password, name, birth_date, ip_address, self.__ID)
            self.add_user(admin)
            Logger.info_log("{0}:".format(user_id) + "add system admin : {0}".format(user_name))
        except Exception as err:
            Logger.error_log("{0}:".format(user_id) + err.__str__())
            raise err

    def add_union_representor(self, user_name, password, name, birth_date, ip_address, user_id=""):
        try:
            self.__ID = self.__ID + 1
            union_rep = UnionRepresentor(user_name, password, name, birth_date, ip_address, self.__ID)
            self.add_user(union_rep)
            Logger.info_log("{0}:".format(user_id) + "add Union Representor : {0}".format(user_name))
        except Exception as err:
            Logger.error_log("{0}:".format(user_id) + err.__str__())
            raise err

    def add_referee_to_data(self, qualification, user_name, password, name, birth_date, ip_address, user_id=""):
        try:
            self.__ID = self.__ID + 1
            referee_user = Referee(qualification, user_name, password, name, birth_date, ip_address, self.__ID)
            self.add_user(referee_user)
            Logger.info_log("{0}:".format(user_id) + "add referee : {0}".format(user_name))
        except Exception as err:
            Logger.error_log("{0}:".format(user_id) + err.__str__())
            raise err

    def add_team_owner_to_data(self, user_name, password, name, birth_date, ip_address, assigned_by=None, roles=None,
                               team=None, user_id=""):
        try:
            self.__ID = self.__ID + 1
            team_owner = TeamOwner(assigned_by, roles)
            team_user = TeamUser(user_name, password, name, birth_date, ip_address, self.__ID, team, team_owner)
            self.add_user(team_user)
            Logger.info_log("{0}:".format(user_id) + "add referee : {0}".format(user_name))
        except Exception as err:
            Logger.error_log("{0}:".format(user_id) + err.__str__())
            raise err

    def add_team_manager_to_data(self, user_name, password, name, birth_date, ip_address, assigned_by=None,
                                 bool_open_close=False, bool_accounting=False, bool_add_remove=False,
                                 bool_set_permission=False, team=None, user_id=""):
        try:
            self.__ID = self.__ID + 1
            team_manager = TeamManager(assigned_by, bool_open_close, bool_accounting, bool_add_remove,
                                       bool_set_permission)
            team_user = TeamUser(user_name, password, name, birth_date, ip_address, self.__ID, team, team_manager)
            self.add_user(team_user)
            Logger.info_log("{0}:".format(user_id) + "add manager: {0}".format(user_name))
        except Exception as err:
            Logger.error_log("{0}:".format(user_id) + err.__str__())
            raise err

    def add_coach_to_data(self, user_name, password, name, birth_date, ip_address, assigned_by=None,
                          qualification: str = None, team=None, user_id=""):
        try:
            self.__ID = self.__ID + 1
            coach = Coach(assigned_by, qualification)
            team_user = TeamUser(user_name, password, name, birth_date, ip_address, self.__ID, team, coach)
            self.add_user(team_user)
            Logger.info_log("{0}:".format(user_id) + "add coach: {0}".format(user_name))
        except Exception as err:
            Logger.error_log("{0}:".format(user_id) + err.__str__())
            raise err

    def add_player_to_data(self, user_name, password, name, birth_date, ip_address, assigned_by=None,
                           position: str = None, number=0, team=None, user_id=""):
        try:
            self.__ID = self.__ID + 1
            player = Player(assigned_by, position, number)
            team_user = TeamUser(user_name, password, name, birth_date, ip_address, self.__ID, team, player)
            self.add_user(team_user)
            Logger.info_log("{0}:".format(user_id) + "add player: {0}".format(user_name))
        except Exception as err:
            Logger.error_log("{0}:".format(user_id) + err.__str__())
            raise err

    def number_of_admins(self, user_id=""):
        """

        @return: number of admins that in the system
        """
        try:
            Logger.info_log("{0}:".format(user_id) + "Got number of admins")
            return self.__user_data_base.get_number_of_admins_in_system()

        except Exception as err:
            Logger.error_log("{0}:".format(user_id) + err.__str__())
            raise err
