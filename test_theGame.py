from unittest import TestCase

from game import FixedSetupSource


class TestFixedSetupSource(TestCase):
    def test_read_number_of_players(self):
        assert FixedSetupSource(4).read_number_of_players() == 4
