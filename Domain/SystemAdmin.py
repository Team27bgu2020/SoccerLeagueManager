from Domain.SignedUser import SignedUser
from Domain.Team import Team


""" Changed By: Roman """


class SystemAdmin(SignedUser):
    """ Constructor for SystemAdmin class getting arguments, checks them and updates the relevant fields"""

    def __init__(self, user_name, password, name, birth_date, user_id):
        super().__init__(user_name, password, name, birth_date, user_id)
