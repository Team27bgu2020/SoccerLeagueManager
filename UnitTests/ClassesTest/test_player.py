from unittest import TestCase
from Domain.Player import Player


class TestPlayer(TestCase):
    player = Player(position="winger", number='5')

    def test_set_role_name(self):
        self.assertEqual(self.player.position, "winger")
        self.player.position = '2'
        self.assertEqual(self.player.position, "2")
        self.assertEqual(self.player.number,'5')
        self.player.number = '3'
        self.assertEqual(self.player.number,'3')




