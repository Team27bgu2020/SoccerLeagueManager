
class ComplaintDB:

    def __init__(self):

        self.__complaints = {}

    """ This method adds a new complaint to the data base """

    def add(self, complaint):

        if complaint.description not in self.__complaints.keys():
            self.__leagues[complaint.description] = []

        self.__complaints[complaint.description].append(complaint)

    """ This method returns all the complaints in the database """

    def show_complaints(self):

        return self.__complaints

    """ This method returns a specific complaint """

    def get_complaints(self, description: str):

        if description not in self.__complaints.keys():
            return []

        return self.__complaints[description]