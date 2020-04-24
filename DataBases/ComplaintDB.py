
class ComplaintDB:

    def __init__(self):

        self.__complaints = {}

    """ This method adds a new complaint to the data base """

    def add(self, complaint):
        complainer = complaint.complainer()
        if complainer not in self.__complaints.keys():
            self.__complaints[complainer] = []

        self.__complaints[complainer].append(complaint)

    """ This method returns all the complaints in the database """

    def show_complaints(self):

        return self.__complaints

    """ This method returns a specific complaint """

    def get_complaints(self, complainer):

        if complainer not in self.__complaints.keys():
            return []

        return self.__complaints[complainer]

    @property
    def complaints(self):
        return self.__complaints