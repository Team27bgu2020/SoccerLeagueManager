class SignedUser:

    def __init__(self):
        raise NotImplementedError

    def add_event(self, event):

        raise NotImplementedError


def type_check(obj):

    if type(obj) is not SignedUser:
        raise TypeError
