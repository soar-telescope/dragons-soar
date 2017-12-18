# -*- coding: utf-8 -*-

from __future__ import print_function, absolute_import

import unittest
import pkg_resources

import soar_instruments
import astrodata


class TestSAMI(unittest.TestCase):

    def test_bias(self):

        sample_bias = pkg_resources.resource_filename(
            'soar_instruments', 'sample_data/sami_bias.fits')

        ad = astrodata.open(sample_bias)

        assert True

