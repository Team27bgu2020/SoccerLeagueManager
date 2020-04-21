from Domain.User import User


class Guest(User):
    
    def __init__(self, ip_address, user_id):
        super().__init__(ip_address, user_id)

    @property
    def get_user_id(self):
        return super().get_user_id()

    @property
    def get_ip_address(self):
        return super().get_ip_address()
