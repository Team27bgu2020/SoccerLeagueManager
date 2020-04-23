from Domain.SignedUser import SignedUser
import Domain.Team as Team

""" Changed By: Roman """

class SystemAdmin(SignedUser):
    """ Constructor for SystemAdmin class getting arguments, checks them and updates the relevant fields"""

    def __init__(self, user_name, password, name, birth_date):
        super(SystemAdmin, self).__init__(user_name, password, name, birth_date)

    """ This method closes a Team in the DB """

    def close_team(self, team):
        Team.type_check(team)

        if team.is_open is False:
            raise ValueError

        team.close_team()

    """ This method removes a user from the DB """

    def remove_user(self, user):
        SignedUser.type_check(user)
        pass

    """ This method shows complaints """

    def show_complaints(self):
        pass

    """ This method allows to comment on a complaint """

    def reply_to_complaint(self, complaint):
        pass

    """ This method shows system log files """

    def show_log_files(self):
        pass

    """ This method builds a recommendation system """

    def build_recommendation_system(self):
        pass

    @property
    def user_name(self):
        return super(SystemAdmin, self).user_name

    @property
    def name(self):
        return super(SystemAdmin, self).name

    @property
    def password(self):
        return super(SystemAdmin, self).password

    @property
    def birth_date(self):
        return super(SystemAdmin, self).birth_date
