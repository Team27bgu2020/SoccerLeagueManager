from unittest import TestCase
from Domain.GameSchedulePolicy import GameSchedulePolicy
from Domain.PointsCalculationPolicy import PointsCalculationPolicy
from Enums.GameAssigningPoliciesEnum import GameAssigningPoliciesEnum


class TestPolicies(TestCase):

    def test_points_calculation_policy(self):

        points_policy = PointsCalculationPolicy(3, 0, -3)
        self.assertEqual(points_policy.win_points, 3)
        self.assertEqual(points_policy.tie_points, 0)
        self.assertEqual(points_policy.lose_points, -3)

    def test_game_schedule_policy(self):

        days = ['S', 'M']
        schedule_policy = GameSchedulePolicy(5, 3, days, GameAssigningPoliciesEnum.RANDOM)

        self.assertEqual(schedule_policy.team_games_num, 5)
        self.assertEqual(schedule_policy.games_per_week, 3)
        self.assertEqual(schedule_policy.chosen_days, days)
        self.assertEqual(schedule_policy.team_stadium_assignment_policy, GameAssigningPoliciesEnum.RANDOM)