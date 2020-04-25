from unittest import TestCase
from Domain.UnionRepresentor import UnionRepresentor
from Domain.UnionOrganization import UnionOrganization
from datetime import datetime
from Domain.Team import Team


class TestUnionOrganization(TestCase):

    def setUp(self):

        self.organization = UnionOrganization()
        self.user1 = UnionRepresentor('user_name', '1234', 'Dor', datetime.today(), '1.1.1.1', 1, 5000)
        self.user2 = UnionRepresentor('user_name', '1234', 'Shahar', datetime.today(), '1.1.1.1', 1, 5000)
        self.team1 = Team('team1')
        self.team2 = Team('Team2')
        self.team3 = Team('Team3')

    def test_add_team_to_union(self):

        self.assertEqual(len(self.organization.teams_in_union), 0)
        self.organization.add_team_to_union(self.team1)
        self.assertEqual(len(self.organization.teams_in_union), 1)
        self.assertEqual(self.organization.teams_in_union[0].name, self.team1.name)
        self.organization.add_team_to_union(self.team2)
        self.assertEqual(len(self.organization.teams_in_union), 2)
        self.assertEqual(self.organization.teams_in_union[1].name, self.team2.name)

    def test_remove_team_from_union(self):

        # Preparation

        self.organization.add_team_to_union(self.team1)
        self.organization.add_team_to_union(self.team2)

        # Tests

        self.assertEqual(len(self.organization.teams_in_union), 2)
        self.organization.remove_team_from_union(self.team1)
        self.assertEqual(len(self.organization.teams_in_union), 1)
        self.assertEqual(self.organization.teams_in_union[0].name, self.team2.name)
        self.organization.remove_team_from_union(self.team2)
        self.assertEqual(len(self.organization.teams_in_union), 0)

    def test_add_employee_to_union(self):

        self.assertEqual(len(self.organization.employees), 0)
        self.organization.add_employee_to_union(self.user1)
        self.assertEqual(len(self.organization.employees), 1)
        self.assertEqual(self.organization.employees[0].name, self.user1.name)
        self.organization.add_employee_to_union(self.user2)
        self.assertEqual(len(self.organization.employees), 2)
        self.assertEqual(self.organization.employees[1].name, self.user2.name)

    def test_remove_employee_from_union(self):

        # Preparation

        self.organization.add_employee_to_union(self.user1)
        self.organization.add_employee_to_union(self.user2)

        # Tests

        self.assertEqual(len(self.organization.employees), 2)
        self.organization.remove_employee_from_union(self.user1)
        self.assertEqual(len(self.organization.employees), 1)
        self.assertEqual(self.organization.employees[0].name, self.user2.name)
        self.organization.remove_employee_from_union(self.user2)
        self.assertEqual(len(self.organization.teams_in_union), 0)

    def test_add_income(self):

        self.assertEqual(self.organization.balance, 0)
        self.assertTrue(self.organization.add_income(1000, 'Test'))
        self.assertEqual(len(self.organization.incomes), 1)
        self.assertEqual(self.organization.incomes[0][1], 1000)
        self.assertEqual(self.organization.incomes[0][0], 'Test')
        self.assertEqual(self.organization.balance, 1000)

        # Test negative income

        self.assertRaises(ValueError, self.organization.add_income, -100, 'Test')

        # Test 0 income

        self.assertRaises(ValueError, self.organization.add_income, 0, 'Test2')

    def test_add_expense(self):

        # Preparation

        self.organization.add_income(1000, 'Prep')

        # Tests

        self.organization.add_expense(400, 'Test2')
        self.assertEqual(len(self.organization.expenses), 1)
        self.assertEqual(self.organization.expenses[0][1], 400)
        self.assertEqual(self.organization.expenses[0][0], 'Test2')
        self.assertEqual(self.organization.balance, 600)

        # Test negative expanse

        self.assertRaises(ValueError, self.organization.add_expense, -100, 'Test')

        # Test 0 income

        self.assertRaises(ValueError, self.organization.add_expense, 0, 'Test 2')

        # Test expanse bigger than balance

        self.assertRaises(ValueError, self.organization.add_expense, 1000, 'Test')

    def test_is_team_in_union(self):

        # Preparation
        self.organization.add_team_to_union(self.team1)
        self.organization.add_team_to_union(self.team2)

        # Tests

        self.assertTrue(self.organization.is_team_in_union(self.team1))
        self.assertTrue(self.organization.is_team_in_union(self.team2))
        self.assertFalse(self.organization.is_team_in_union(self.team3))
