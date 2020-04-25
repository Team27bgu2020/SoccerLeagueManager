from unittest import TestCase
from Domain.Player import Player


class TestPlayer(TestCase):
    player = Player(position="winger")

    def test_set_role_name(self):
        self.assertEqual(self.player.position, "winger")
        self.player.position = '2'
        self.assertEqual(self.player.position, "2")


