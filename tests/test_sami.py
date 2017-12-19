# -*- coding: utf-8 -*-

import unittest
import pkg_resources
import os

import soar_instruments
import astrodata


class TestSAMI(unittest.TestCase):

    def file_exists(self):

        sample_bias = pkg_resources.resource_filename(
            'soar_instruments', 'sample_data/sami_bias.fits')

        assert os.path.exists(sample_bias)

#    def test_bias(self):#
#
#        sample_bias = pkg_resources.resource_filename(
#            'soar_instruments', 'sample_data/sami_bias.fits')#
#
#        ad = astrodata.open(sample_bias)

