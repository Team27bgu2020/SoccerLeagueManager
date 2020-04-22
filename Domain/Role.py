# noinspection PyAttributeOutsideInit
class Role:

    """ Default constructor for Role class """

    def __init__(self, assigned_by):
        self.assigned_by(assigned_by)

    @property
    def assigned_by(self):
        return self.assigned_by

    @assigned_by.setter
    def assigned_by(self, assigned_by):
        if type(assigned_by) is not Role:
            raise TypeError
        self.__assigned_by = assigned_by
