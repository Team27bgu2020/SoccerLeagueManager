import Domain.SignedUser as SignedUser


class Referee(SignedUser):

    def __init__(self):
        super().__init__()
        raise NotImplementedError

    def add_event(self, event):

        raise NotImplementedError


def type_check(obj):

    if type(obj) is not Referee:
        raise TypeError
