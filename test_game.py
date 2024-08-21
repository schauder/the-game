from unittest import TestCase

from game import DiscardPile, Direction, IllegalPlay


class TestDiscardPile(TestCase):
    def test_discard_pile_does_not_mutate(self):
        original: DiscardPile = DiscardPile.from_direction(Direction.INCREASING)
        with5: DiscardPile = original.play(5)
        self.assertEqual(5, with5.last)
        self.assertEqual(1, original.last)

    def test_discard_pile_rejects_illegal_moves(self):
        original: DiscardPile = DiscardPile(Direction.INCREASING, 45)
        self.assertRaises(IllegalPlay,  original.play, 5)

    def test_discard_pile_accept_backward_move_by_10(self):
        original: DiscardPile = DiscardPile(Direction.DECREASING, 45)
        original.play(55)


