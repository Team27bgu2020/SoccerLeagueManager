from Domain.League import League
from Domain.Season import Season
from Domain.PointsCalculationPolicy import PointsCalculationPolicy
from Domain.GameSchedulePolicy import GameSchedulePolicy
from Domain.TeamBudgetPolicy import TeamBudgetPolicy


class LeagueController:

    def __init__(self, league_db, season_db, policy_db):

        self.__league_DB = league_db
        self.__season_DB = season_db
        self.__policies_DB = policy_db

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

    def update_team_budget_policy(self, league, team_budget_policy):

        league.team_budget_policy = team_budget_policy

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

    """ This method returns the all the leagues in the given year (season) """

    def get_league(self, year: int):

        return self.__league_DB.get_leagues_by_season(year)

    """ This method create a new points calculation policy """

    def create_points_calculation_policy(self, win_points: int, tie_points: int, lose_points: int):

        policy = PointsCalculationPolicy(win_points, tie_points, lose_points)
        self.__policies_DB.add(policy)
        return policy

    """ This method create a new game schedule policy """

    def create_game_schedule_policy(self, team_games_num: int, games_per_week: int, chosen_days,
                                    games_stadium_assigning):

        policy = GameSchedulePolicy(team_games_num, games_per_week, chosen_days, games_stadium_assigning)
        self.__policies_DB.add(policy)
        return policy

    """ This method create a new team budget policy """

    def create_team_budget_policy(self, min_amount: int):

        policy = TeamBudgetPolicy(min_amount)
        self.__policies_DB.add(policy)
        return policy

    """ This method create a new points calculation policy """

    @property
    def points_calculation_policies(self):

        return self.__policies_DB.points_calculation_policies

    """ This method create a new game schedule policy """

    @property
    def game_schedule_policy(self):

        return self.__policies_DB.game_schedule_policies

    """ This method create a new team budget policy """

    @property
    def team_budget_policy(self):

        return self.__policies_DB.team_budget_policies