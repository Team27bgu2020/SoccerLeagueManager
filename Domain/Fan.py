from Domain.SignedUser import SignedUser
import Domain.PersonalPage as PersonalPage
import Domain.Game as Game


class Fan(SignedUser):
    """ Default constructor for Fan class"""

    def __init__(self):
        super().__init__()
        self.__followed_pages = []
        self.__followed_games = []

    """ Constructor for Fan class getting arguments, checks them and updates the relevant fields"""

    def __init__(self, user_name, password, name, birth_date):
        super().__init__(user_name, password, name, birth_date)

        self.__followed_pages = []
        self.__followed_games = []

    @property
    def followed_pages(self):

        return self.__followed_pages

    @property
    def followed_games(self):

        return self.__followed_games

    """ This method adds a new page to the followed pages list """

    def follow_page(self, page):
        PersonalPage.type_check(page)

        if page in self.__followed_pages:
            raise ValueError

        self.__followed_pages.append(page)

    """ This method ramoves a page from the followed pages list """

    def unfollow_page(self, page):
        PersonalPage.type_check(page)

        if page not in self.__followed_pages:
            raise ValueError

        self.__followed_pages.remove(page)

    """ This method adds a new game to the followed games list """

    def follow_game(self, game):
        Game.type_check(game)

        if game in self.__followed_games:
            raise ValueError

        self.__followed_games.append(game)

    """ This method ramoves a page from the followed pages list """

    def unfollow_game(self, game):
        Game.type_check(game)

        if game not in self.__followed_games:
            raise ValueError

        self.__followed_games.remove(game)


def type_check(obj):
    if type(obj) is not Fan:
        raise TypeError
