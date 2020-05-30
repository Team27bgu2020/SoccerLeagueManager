from Domain.PersonalPage import PersonalPage
from Log.Logger import *

""" Idan """


class PageController:

    def __init__(self, page_db):
        self.__page_DB = page_db
        self.__id_counter = self.__page_DB.get_id_counter()
        Logger.start_logger()

    """this method is used in order to search for a personal page in the pages_db"""

    def search_personal_page(self, query: str, user_id=""):
        # TODO: search by query
        try:
            page = self.__page_DB.show_personal_page(query)
            if page is None:
                raise ValueError
            Logger.info_log("{0}: ".format(user_id) + "Present Page ")
            return page
        except Exception as err:
            Logger.error_log("{0}:".format(user_id) + err.__str__())
            raise err

    """ this method is used for an update of a personal page"""

    def update_personal_page(self, user_id=""):
        pass

    """ this method adds a page to the pages DB"""

    def add_page(self, title, user_id=""):
        try:
            self.__page_DB.add(PersonalPage(self.__id_counter, title))
            self.update_counter()
            Logger.info_log("{0}: ".format(user_id) + "Page {0} add".format(title))
        except Exception as err:
            Logger.error_log("{0}:".format(user_id) + err.__str__())
            raise err

    def get_page(self, page_id):
        return self.__page_DB.get(page_id)

    def remove_page(self, page_id):
        self.__page_DB.delete(page_id)

    def update_counter(self):
        self.__id_counter += 1
        self.__page_DB.update_id_counter(self.__id_counter)
