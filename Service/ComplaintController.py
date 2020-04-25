from Domain.Complaint import Complaint
# from DataBases.ComplaintDB import ComplaintDB
from Domain.Fan import Fan

""" Idan """


class ComplaintController:

    def __init__(self, complaint_db):
        self.__complaints_DB = complaint_db
        self.__complaint_ID = 1

    @property
    def complaint_id(self):
        return self.__complaint_ID

    """ Show all complaints in DB"""

    def show_complaints(self):
        return self.__complaints_DB

    """Get a specific complaint by her description"""

    def get_complaint(self, complainer, ID):
        if type(complainer) is not Fan:
            raise ValueError
        complaint = self.__complaints_DB.get_complaints(complainer, ID)
        if complaint is None:
            raise Exception("no such complaint")
        return complaint

    """Respond to a complaint"""

    def respond_to_complaint(self, answer, complainer, ID):
        if type(complainer) is not Fan:
            raise ValueError
        if not isinstance(answer, str):
            raise TypeError("Should be string")
        comp = self.get_complaint(complainer, ID)
        comp.set_answer(answer)

    """Open a new complaint, and add it to the complaint DB-dictionary"""

    def new_complaint(self, description, complainer):
        if type(complainer) is not Fan:
            raise ValueError
        if not isinstance(description, str):
            raise TypeError("Should be string")
        complaint = Complaint(description, complainer, self.__complaint_ID)
        self.__complaints_DB.add(complaint)
        self.__complaint_ID += 1
        complainer.complain(complaint)
