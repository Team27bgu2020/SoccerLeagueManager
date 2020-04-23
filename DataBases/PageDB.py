""" idan """


class PageDB:

    def __init__(self):

        self.__pages = []

    """ This method adds a new page to the data base """

    def add(self, page):

        if page not in self.__pages.keys():
            self.__pages.append(page)

    """ This method returns a page in the database """

    def show_personal_page(self, page):

        return self.__pages[page]

