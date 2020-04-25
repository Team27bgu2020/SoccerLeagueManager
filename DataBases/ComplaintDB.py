class ComplaintDB:

    def __init__(self):

        self.__complaints = {}

    """ This method adds a new complaint to the data base """

    def add(self, complaint):
        complaint_id = complaint.complaint_ID
        if complaint_id not in self.__complaints.keys():
            self.__complaints[(complaint_id, complaint.complainer)] = []

        self.__complaints[(complaint_id, complaint.complainer)].append(complaint)

    """ This method returns all the complaints in the database """

    def show_complaints(self):

        return self.__complaints

    """ This method returns a specific complaint """

    def get_complaints(self, complainer, ID):

        if (ID, complainer) not in self.__complaints.keys():
            return None

        for (key_id, key_complainer), complaint in self.__complaints.items():
            if (ID, complainer) == (key_id, key_complainer):
                x = complaint[0]
                return x

    @property
    def complaints(self):
        return self.__complaints
