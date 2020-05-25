class TeamDB:

    def __init__(self):

        self.__teams = {}

    """ This method adds a new team to the data base """

    def add(self, team):

        if team.name in self.__teams.keys():
            raise ValueError("Could not add team, {0} already exist".format(team.name))

        self.__teams[team.name] = team

    """ This method deletes a team from the data base """

    def delete(self, team_name: str):

        if team_name not in self.__teams.keys():
            raise ValueError("Team Doesnt exist")

        if team_name in self.__teams:
            del self.__teams[team_name]

    """ This method returns the wanted team """

    def get(self, team_name: str):

        if team_name not in self.__teams.keys():
            raise ValueError("Could not get team {0}, team does not exist".format(team_name))

        return self.__teams[team_name]

    @property
    def teams(self):
        return self.__teams