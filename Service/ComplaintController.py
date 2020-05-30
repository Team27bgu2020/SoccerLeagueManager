from Domain.Complaint import Complaint

from Domain.Fan import Fan

""" Idan """


class ComplaintController:

    def __init__(self, complaint_db, user_db):
        self.__complaints_DB = complaint_db
        self.__user_DB = user_db
        self.__complaint_ID = self.__complaints_DB.get_id_counter()

    @property
    def complaint_id(self):
        return self.__complaint_ID

    """ Show all complaints in DB"""

    def show_complaints(self):
        return self.__complaints_DB.get_all()

    """Get a specific complaint by her description"""

    def get_complaint(self, ID):

        complaint = self.__complaints_DB.get(ID)
        if complaint is None:
            raise Exception("no such complaint")
        return complaint

    """Respond to a complaint"""

    def respond_to_complaint(self, answer, ID):

        if not isinstance(answer, str):
            raise TypeError("Should be string")
        comp = self.get_complaint(ID)
        comp.set_answer(answer)
        self.__complaints_DB.update(comp)

    """Open a new complaint, and add it to the complaint DB-dictionary"""

    def new_complaint(self, description, complainer_id):
        if not isinstance(description, str):
            raise TypeError("Should be string")
        complaint = Complaint(description, complainer_id, self.__complaint_ID)
        self.__complaints_DB.add(complaint)
        self.update_counter()
        complainer = self.__user_DB.get_signed_user(complainer_id)
        complainer.complain(complaint.complaint_id)
        self.__user_DB.update_signed_user(complainer)
        return complaint

    def update_counter(self):
        self.__complaint_ID += 1
        self.__complaints_DB.update_id_counter(self.__complaint_ID)