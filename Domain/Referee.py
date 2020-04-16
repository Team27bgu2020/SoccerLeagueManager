from Domain.SignedUser import SignedUser


class Referee(SignedUser):

    def __init__(self):
        pass

    def add_event(self, event):
        pass


def type_check(obj):

    if type(obj) is not Referee:
        raise TypeError
