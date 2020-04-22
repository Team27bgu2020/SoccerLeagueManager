from Domain.League import League


class LeagueController:

    def __init__(self, league_db):

        self.__league_DB = league_db

    """ This method creates a new league and adds it to the league data base """

    def create_new_league(self, name: str, season, points_calculation_policy, games_schedule_policy):

        league = League(name, season, points_calculation_policy, games_schedule_policy)
        self.__league_DB.add(league)

    """ This method updates the points calculation policy """

    def update_points_calculation_policy(self, league, points_calculation_policy):

        league.points_calculation_policy = points_calculation_policy

    """ This method updates the game schedule policy """

    def update_game_schedule_policy(self, league, game_schedule_policy):

        league.game_schedule_policy = game_schedule_policy



