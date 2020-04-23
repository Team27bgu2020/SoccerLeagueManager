class PersonalPage:

    def __init__(self, title):
        self.title = title


def type_check(obj):
    if type(obj) is not PersonalPage:
        raise TypeError
