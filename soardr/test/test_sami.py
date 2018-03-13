
from unittest import skip, TestCase

import soar_instruments
import soardr
import astrodata

from recipe_system.reduction.coreReduce import Reduce

import sys


class TestReduce(TestCase):

    def test_reduce(self):
        reduce = Reduce()