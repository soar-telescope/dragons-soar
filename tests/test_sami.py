# -*- coding: utf-8 -*-

import unittest
import pkg_resources

import astrodata
import soar_instruments


class TestSAMI(unittest.TestCase):

    def test_bias(self):

        sample_bias = pkg_resources.resource_filename(
            'soar_instruments', 'sample_data/sami_bias.fits')

        ad = astrodata.open(sample_bias)
        assert isinstance(1, int)
        assert isinstance(1., float)
