from Domain.Complaint import Complaint

from Domain.Fan import Fan
from Log.Logger import *

""" Idan """


class ComplaintController:

    def __init__(self, complaint_db, user_db):
        self.__complaints_DB = complaint_db
        self.__user_DB = user_db
        self.__complaint_ID = self.__complaints_DB.get_id_counter()
        Logger.start_logger()

    @property
    def complaint_id(self):
        return self.__complaint_ID

    """ Show all complaints in DB"""

    def show_complaints(self):
        return self.__complaints_DB.get_all()

    """Get a specific complaint by her description"""

    def get_complaint(self, ID, user_id=""):
        try:
            complaint = self.__complaints_DB.get(ID)
            if complaint is None:
                raise Exception("no such complaint")
            Logger.info_log("{0}: ".format(user_id) + "Got complaint {0}".format(complaint.complaint_id))
            return complaint

        except Exception as err:
            Logger.error_log("{0}:".format(user_id) + err.__str__())
            raise err

    """Respond to a complaint"""

    def respond_to_complaint(self, answer, ID, user_id=""):
        try:
            if not isinstance(answer, str):
                raise TypeError("Should be string")
            comp = self.get_complaint(ID)
            comp.set_answer(answer)
            self.__complaints_DB.update(comp)
            Logger.info_log("{0}: ".format(user_id) + "respond to complaint {0}".format(ID))
        except Exception as err:
            Logger.error_log("{0}:".format(user_id) + err.__str__())
            raise err

    """Open a new complaint, and add it to the complaint DB-dictionary"""

    def new_complaint(self, description, complainer_id, user_id=""):
        try:
            if not isinstance(description, str):
                raise TypeError("Should be string")
            complaint = Complaint(description, complainer_id, self.__complaint_ID)
            self.__complaints_DB.add(complaint)
            self.update_counter()
            complainer = self.__user_DB.get_signed_user(complainer_id)
            complainer.complain(complaint.complaint_id)
            self.__user_DB.update_signed_user(complainer)
            Logger.info_log("{0}: ".format(user_id) + "Added new complain {0}".format(complaint.complaint_id))
            return complaint
        except Exception as err:
            Logger.error_log("{0}:".format(user_id) + err.__str__())
            raise err

    def delete_complaint(self, complaint_id):
        self.__complaints_DB.delete(complaint_id)

    def update_counter(self):
        self.__complaint_ID += 1
        self.__complaints_DB.update_id_counter(self.__complaint_ID)