from unittest import TestCase

from game import DiscardPile, Direction


class TestDiscardPile(TestCase):
    def test_discard_pile(self):
        original: DiscardPile = DiscardPile.from_direction(Direction.INCREASING)
        with5: DiscardPile = original.play(5)
        assert with5.last == 5
        assert original.last == 1
