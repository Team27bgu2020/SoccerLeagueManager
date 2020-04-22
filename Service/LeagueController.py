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

    """ This method updates the team budget policy """

    def update_game_schedule_policy(self, league, team_budget_policy):

        league.team_budget_policy = team_budget_policy

    """ This method creates a game schedule for the leagues """

    def make_game_schedule(self, league):

        pass

    def add_referee_to_league(self, league, referee):

        league.add_referee(referee)

