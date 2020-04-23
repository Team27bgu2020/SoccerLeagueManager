""" idan """


class PageDB:

    def __init__(self):

        self.__pages = {}

    """ This method adds a new page to the data base """

    def add(self, page):

        if page.title not in self.__pages.keys():
            self.__pages[page.title] = []

        self.__pages[page.title].append(page)

    """ This method returns a page in the database """

    def show_personal_page(self, title):
        if title not in self.__pages.keys():
            TypeError("page Doesnt exist")
            return None
        return self.__pages[title]

