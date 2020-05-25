import datetime as date
from unittest import TestCase

from DataBases.TeamDB import TeamDB
from Domain.Team import Team
from Domain.TeamOwner import TeamOwner
from Domain.TeamUser import TeamUser
from Service.TeamManagementController import TeamManagementController


owner = TeamUser('user_nam2', 'password', 'NameB', date.datetime(1993, 1, 12), "0.0.0.2", 3,
                          team=None,
                          role=TeamOwner())

team_db = TeamDB()
control = TeamManagementController(team_db)
control.open_new_team("barce",None)
control.open_new_team("barce",owner)

# control.open_new_team("barca",owner)
# control.open_new_team("barca",owner)