import unittest

from freezegun import freeze_time
from hashids import Hashids

from lib import generate_hashid


class TestGenerateHashid(unittest.TestCase):
    def test_generates_hashids_that_are_8_characters_or_greater(self):
        for _ in range(1000):
            self.assertGreaterEqual(len(generate_hashid()), 8)

    @freeze_time('2016-01-01')
    def test_returns_equal_hash_for_equal_time(self):
        expected = Hashids(min_length=8).encode(1451606400000)
        self.assertEqual(generate_hashid(), expected)
