class GameSchedulePolicy:

    def __init__(self):
        raise NotImplementedError


def type_check(obj):
    if type(obj) is not GameSchedulePolicy:
        raise TypeError