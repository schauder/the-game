from unittest import TestCase

import numbers


class Test(TestCase):
    def test_safe_convert_to_int(self):
        assert numbers.safe_convert_to_int("5") == 5
        assert numbers.safe_convert_to_int("0") == 0
        assert numbers.safe_convert_to_int("bla") is None
        assert numbers.safe_convert_to_int("  23  ") == 23
