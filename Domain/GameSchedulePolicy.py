class GameSchedulePolicy:

    def __init__(self):
        pass


def type_check(obj):
    if type(obj) is not GameSchedulePolicy:
        raise TypeError
