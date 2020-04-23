from Domain.User import User


class Guest(User):

    def __init__(self, ip_address, user_id):
        super().__init__(ip_address, user_id)


    def get_user_id(self):
        return super().user_id



