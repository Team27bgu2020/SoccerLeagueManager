from Domain.SignedUser import SignedUser

""" Idan """


class Fan(SignedUser):
    """ Constructor for Fan class getting arguments, checks them and updates the relevant fields"""

    def __init__(self, user_name, password, name, birth_date, ip_address, user_id):
        super().__init__(user_name, password, name, birth_date, ip_address, user_id)

        self.__search_history = []
        self.__followed_pages = []
        self.__followed_games = []
        self.__complaints = []
        self.__recommendation_system = None

    @property
    def complaints(self):

        return self.__complaints

    @property
    def followed_pages(self):

        return self.__followed_pages

    @property
    def followed_games(self):

        return self.__followed_games

    @property
    def recommendation_system(self):

        return self.__recommendation_system

    """ This method adds a new page to the followed pages list """

    def follow_page(self, page):

        if page in self.__followed_pages:
            raise ValueError('Page already followed')

        self.__followed_pages.append(page)

    """ This method ramoves a page from the followed pages list """

    def unfollow_page(self, page):

        if page not in self.__followed_pages:
            raise ValueError('User is not following this page')

        self.__followed_pages.remove(page)

    """ This method adds a new game to the followed games list """

    def follow_game(self, game):

        if game in self.__followed_games:
            raise ValueError('User already following this game')

        self.__followed_games.append(game)

    """ This method ramoves a page from the followed pages list """

    def unfollow_game(self, game):

        if game not in self.__followed_games:
            raise ValueError("User is not following this game")

        self.__followed_games.remove(game)

    """ Setter for recommendation system """

    def set_recommendation_system(self, recommendation_system):

        self.__recommendation_system = recommendation_system

    """ This method lets the fan register a complaint"""

    def complain(self, complaint):

        self.__complaints.append(complaint)
