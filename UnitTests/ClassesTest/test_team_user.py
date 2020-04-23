from unittest import TestCase
from Domain.TeamUser import *


class TestTeamUser(TestCase):

    def __init__(self):
        self.team_user = TeamUser()

    def test_set_team(self):

        valid_team = Team()
        valid_team.__name = 'valid_input'
        invalid_team = 'team'

        # Test valid input
        self.team_user.set_team(valid_team)
        self.assertEqual(valid_team, self.team_user.__team)

        # Test invalid input
        self.assertRaises(TypeError, self.team_user.set_team, invalid_team)

        def test_set_role(self):
            valid_role = Role()
            invalid_role = 'role'

            # Test valid input
            self.team_user.set_role(valid_role)
            self.assertEqual(valid_role, self.team_user.__role)

            # Test invalid input
            self.assertRaises(TypeError, self.team_user.set_role, invalid_role)
