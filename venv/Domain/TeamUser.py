class TeamUser:

    def __init__(self):
        raise NotImplementedError


def type_check(obj):

    if type(obj) is not TeamUser:
        raise TypeError
