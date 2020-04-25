from Domain.SignedUser import SignedUser
from Domain.Team import Team


""" Changed By: Roman """


class SystemAdmin(SignedUser):
    """ Constructor for SystemAdmin class getting arguments, checks them and updates the relevant fields"""

    def __init__(self, user_name, password, name, birth_date, ip_address, user_id):
        super(SystemAdmin, self).__init__(user_name, password, name, birth_date, ip_address, user_id)

    """ This method closes a Team in the DB """

    def close_team(self, team: Team):
        if type(team) is Team:
            if team.is_open is False:
                raise ValueError
            team.close_team()
        else:
            raise TypeError

    """ This method removes a user from the DB """



