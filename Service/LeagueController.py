from Domain.League import League
from Domain.Season import Season


class LeagueController:

    def __init__(self, league_db, season_db):

        self.__league_DB = league_db
        self.__season_DB = season_db

    """ This method creates new season """

    def create_new_season(self, year: int):

        if self.__season_DB.get(year) is not None:
            raise ValueError("Season with the same year exists inn the System already")

        season = Season(year)
        self.__season_DB.add(season)
        return season

    """ This method creates a new league and adds it to the league data base """

    def create_new_league(self, name: str, season, points_calculation_policy, games_schedule_policy,
                          team_budget_policy):

        if self.__league_DB.get(name, season.year) is not None:
            raise ValueError("League with that name already exists in the given season")

        league = League(name, season, points_calculation_policy, games_schedule_policy, team_budget_policy)
        self.__league_DB.add(league)
        return league

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

    """ This method adds new teams to a season """

    def add_teams_to_league(self, league, teams):

        league.add_teams(teams)

    """ This method adds leagues to season """

    def add_leagues_to_season(self, season, leagues):

        season.add_leagues(leagues)

    """ This method returns the season of the given year """

    def get_season(self, year: int):

        return self.__season_DB.get(year)

    """ This method returns the league in the given year with the same given name """

    def get_league(self, name: str, year: int):

        return self.__league_DB.get(name, year)