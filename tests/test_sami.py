# -*- coding: utf-8 -*-

import unittest
import pkg_resources
import os

from astropy.io import fits as pyfits

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

        # ToDo - Temporary fix for the issue regarding the EXTNAME
        hdu = pyfits.open(sample_bias)
        for i in range(1, len(hdu)):
            del hdu[i].header['EXTNAME']

        sample_bias = sample_bias.replace('.fits', '_c.fits')
        hdu.writeto(sample_bias, overwrite=True)

        # Try to open in astrodata
        ad = astrodata.open(sample_bias)

        print ad.info()