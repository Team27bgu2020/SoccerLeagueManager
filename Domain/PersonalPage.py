class PersonalPage:

    def __init__(self, page_id, title):
        self.__title = title
        self.__page_id = page_id

    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, value):
        self.__title = value

    @property
    def page_id(self):
        return self.__page_id

    @page_id.setter
    def page_id(self, value):
        self.__page_id = value

