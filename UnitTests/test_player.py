from unittest import TestCase
from Domain.Player import Player


class TestPlayer(TestCase):
    player = Player("winger")

    def test_set_role_name(self):
        self.player.to_string()
        self.assertEqual(self.player.get_position_name(), "winger")
        self.player.set_position_name("mid")
        self.assertEqual(self.player.get_position_name(), "mid")


