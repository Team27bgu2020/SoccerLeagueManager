class GameDB:

    def __init__(self):

        self.__games_by_date = {}
        self.__games_by_team = {}

    """ This method adds a new game to the data base """

    def add(self, game):

        self.add_to_games_by_date(game)
        self.add_to_games_by_team(game, game.home_team)
        self.add_to_games_by_team(game, game.away_team)

    """ This method adds the game to the dictionary where the key is the game date
        *** Don't use that *** """

    def add_to_games_by_date(self, game):

        if game.match_time not in self.__games_by_date.keys():
            self.__games_by_date[game.match_time] = []

        if game not in self.__games_by_date[game.match_time]:
            self.__games_by_date[game.match_time].append(game)

    """ This method adds the game to the dictionary where the key is the team name 
        *** Don't use that *** """

    def add_to_games_by_team(self, game, team):

        if team.name not in self.__games_by_team.keys():
            self.__games_by_team[team.name] = []

        if game not in self.__games_by_team[team.name]:
            self.__games_by_team[team.name].append(game)

    """ This method deletes a game from the data base """

    def delete(self, game):

        self.delete_from_games_by_date(game)
        self.delete_from_games_by_team(game, game.home_team)
        self.delete_from_games_by_team(game, game.away_team)

    """ This method deletes the game from the dictionary where the key is the game date 
        *** Don't use that *** """

    def delete_from_games_by_date(self, game):

        if game.home_team in self.__games_by_date.keys() and game in self.__games_by_date[game.match_time]:
            self.__games_by_date[game.match_time].remove(game)

    """ This method deletes the game from the dictionary where the key is the team name 
        *** Don't use that *** """

    def delete_from_games_by_team(self, game, team):

        if team.name in self.__games_by_team.keys() and game in self.__games_by_team[team.name]:
            self.__games_by_team[team.name].remove(game)

    """ This method return the game if it saved in the data base """

    def get(self, team1_name: str, team2_name: str, game_date):

        for game in self.get_game_of_teams(team1_name, team2_name):
            if game.match_time == game_date:
                return game

    """ This method return the game if it saved in the data base """

    def get_game_of_teams(self, team1_name: str, team2_name: str):

        if team1_name or team2_name not in self.__games_by_team.keys():
            return []

        return list(set(self.__games_by_team[team1_name]) & set(self.__games_by_team[team2_name]))

    """ This method returns a list of all the games in a certain date """

    def get_games_by_date(self, date):

        return self.__games_by_date[date]

    """ This method returns a list of all the games in a certain date """

    def get_games_by_team(self, team_name):

        return self.__games_by_team[team_name]

