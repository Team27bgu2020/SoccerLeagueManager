from Domain.PersonalPage import PersonalPage

""" Idan """


class PageController:

    def __init__(self, page_db):
        self.__page_DB = page_db

    """this method is used in order to search for a personal page in the pages_db"""

    def search_personal_page(self, query: str):
        page = self.__page_DB.show_personal_page(query)
        if page is None:
            raise ValueError
            return
        return self.__page_DB.show_personal_page(query)

    """ this method is used for an update of a personal page"""

    def update_personal_page(self):
        pass

    """ this method adds a page to the pages DB"""

    def add_page(self, title):
        self.__page_DB.add(PersonalPage(title))
