class Season:

    def __init__(self, year):

        self._year = year
        raise NotImplementedError

    """ This methods returns the seasons year """

    def get_year(self):

        return self._year


def type_check(obj):

    if type(obj) is not Season:
        raise TypeError