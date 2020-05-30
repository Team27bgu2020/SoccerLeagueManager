from Domain.User import User


class Guest(User):

    def __init__(self, user_id):
        super().__init__(user_id)

    def get_user_id(self):
        return super().user_id
