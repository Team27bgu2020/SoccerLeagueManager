from Domain.SignedUser import SignedUser
import Domain.PersonalPage as PersonalPage
import Domain.Game as Game
import Domain.RecommendationSystem as RecommendationSystem
from Domain.Complaint import Complaint
import datetime

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
        if type(page) is not PersonalPage.PersonalPage:
            raise TypeError

        if page in self.__followed_pages:
            raise ValueError

        self.__followed_pages.append(page)

    """ This method ramoves a page from the followed pages list """

    def unfollow_page(self, page):
        if type(page) is not PersonalPage.PersonalPage:
            raise TypeError

        if page not in self.__followed_pages:
            raise ValueError

        self.__followed_pages.remove(page)

    """ This method adds a new game to the followed games list """

    def follow_game(self, game):
        if type(game) is not Game.Game:
            raise TypeError

        if game in self.__followed_games:
            raise ValueError

        self.__followed_games.append(game)

    """ This method ramoves a page from the followed pages list """

    def unfollow_game(self, game):
        if type(game) is not Game.Game:
            raise TypeError

        if game not in self.__followed_games:
            raise ValueError

        self.__followed_games.remove(game)

    """ Setter for recommendation system """

    def set_recommendation_system(self, recommendation_system):

        if type(recommendation_system) is not RecommendationSystem.RecommendationSystem:
            raise TypeError

        self.__recommendation_system = recommendation_system

    """ This method lets the fan register a complaint"""

    def complain(self, complaint):
        if type(complaint) is not Complaint:
            raise TypeError

        self.__complaints.append(complaint)
