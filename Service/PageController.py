from Domain.PersonalPage import PersonalPage
from Log.Logger import *

""" Idan """


class PageController:

    def __init__(self, page_db):
        self.__page_DB = page_db
        Logger.start_logger()

    """this method is used in order to search for a personal page in the pages_db"""

    def search_personal_page(self, query: str, user_id=""):
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
            self.__page_DB.add(PersonalPage(title))
            Logger.info_log("{0}: ".format(user_id) + "Page {0} add".format(title))
        except Exception as err:
            Logger.error_log("{0}:".format(user_id) + err.__str__())
            raise err
