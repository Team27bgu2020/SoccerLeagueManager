from Domain.Coach import Coach
from Domain.Player import Player
from Domain.Team import Team
from Domain.TeamOwner import TeamOwner
from Domain.TeamUser import TeamUser


class AcceptanceTestsOwner:
    # Preparation
    team = Team()
    u_owner = TeamOwner("Oscar")
    p1 = Player("striker")
    c1 = Coach("1")
    u_player = TeamUser(team, Player("striker"))
    u_coach = TeamUser(team, Coach("1"))
