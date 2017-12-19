# -*- coding: utf-8 -*-

import unittest
import pkg_resources
import os

import soar_instruments
import astrodata


class TestSAMI(unittest.TestCase):

    def test_bias(self):
        """
        Just check if the a BIAS obtained with SAMI is read correctly and if
        the tags are set properly.
        """
        sample_bias = 'tests/data/sami/bias.fits'

        # Check if file exists
        assert os.path.exists(sample_bias)

        # Try to open in astrodata
        ad = astrodata.open(sample_bias)

        print ad.info()