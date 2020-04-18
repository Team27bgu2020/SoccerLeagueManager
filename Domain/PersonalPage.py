class PersonalPage:

    def __init__(self):
        pass


def type_check(obj):
    if type(obj) is not PersonalPage:
        raise TypeError
