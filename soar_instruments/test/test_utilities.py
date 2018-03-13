import unittest

from collections import namedtuple
from numpy import random
from .. import utilities


class TestUtils(unittest.TestCase):

    def test_str_to_int(self):

        x1, x2 = random.random_integers(0, 100, 2)
        y1, y2 = random.random_integers(0, 100, 2)

        section_string = '[{:d}:{:d}, {:d}:{:d}]'.format(x1+1, x2, y1+1, y2)
        nx1, nx2, ny1, ny2 = utilities.section_str_to_int_list(section_string)

        self.assertEqual(x1, nx1)
        self.assertEqual(x2, nx2)
        self.assertEqual(y1, ny1)
        self.assertEqual(y2, ny2)

    def test_str_to_section(self):

        Section = namedtuple('Section', 'x1 x2 y1 y2')

        x1, x2 = random.random_integers(0, 100, 2)
        y1, y2 = random.random_integers(0, 100, 2)
        original_section = Section(*[x1, x2, y1, y2])

        section_string = '[{:d}:{:d}, {:d}:{:d}]'.format(x1 + 1, x2, y1 + 1, y2)
        produced_section = utilities.section_to_tuple(section_string)

        self.assertEqual(original_section, produced_section)
