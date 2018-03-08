# -*- coding: utf-8 -*-

import unittest
import pkg_resources
import os

from astropy.io import fits as pyfits

import soar_instruments
import soardr
import astrodata


class SAMI_IO(unittest.TestCase):

    def test_bias(self):
        """
        Just check if the a BIAS obtained with SAMI is read correctly and if
        the tags are set properly.
        """
        sample_bias = 'tests/data/sami/sami_bias.fits'

        # Check if file exists
        assert os.path.exists(sample_bias)

        # Temporary fix for the issue regarding the EXTNAME
        hdu = pyfits.open(sample_bias)
        for i in range(1, len(hdu)):
            del hdu[i].header['EXTNAME']

        new_sample_bias = sample_bias.replace('.fits', '_c.fits')
        hdu.writeto(new_sample_bias, overwrite=True)

        # Try to open in astrodata
        ad = astrodata.open(new_sample_bias)

        # Check if the tags are set correctly
        self.assertIn('SOAR', ad.tags)
        self.assertIn('SAM', ad.tags)
        self.assertIn('SAMI', ad.tags)
        self.assertIn('CAL', ad.tags)
        self.assertIn('BIAS', ad.tags)

        os.remove(new_sample_bias)

    def test_flat(self):
        """
        Just check if the a FLAT obtained with SAMI is read correctly and if
        the tags are set properly.
        """
        sample_flat = 'tests/data/sami/sami_skyflat.fits'

        # Check if file exists
        self.assertTrue(os.path.exists(sample_flat))

        # Temporary fix for the issue regarding the EXTNAME
        hdu = pyfits.open(sample_flat)
        for i in range(1, len(hdu)):
            del hdu[i].header['EXTNAME']

        new_sample_flat = sample_flat.replace('.fits', '_c.fits')
        hdu.writeto(new_sample_flat, overwrite=True)

        # Try to open in astrodata
        ad = astrodata.open(new_sample_flat)

        # Check if the tags are set correctly
        self.assertIn('SOAR', ad.tags)
        self.assertIn('SAM', ad.tags)
        self.assertIn('SAMI', ad.tags)
        self.assertIn('CAL', ad.tags)
        self.assertIn('FLAT', ad.tags)

        os.remove(new_sample_flat)

    def test_object(self):
        """
        Just check if the a FLAT obtained with SAMI is read correctly and if
        the tags are set properly.
        """
        sample_object = 'tests/data/sami/sami_object.fits'

        # Check if file exists
        self.assertTrue(os.path.exists(sample_object))

        # Temporary fix for the issue regarding the EXTNAME
        hdu = pyfits.open(sample_object)
        for i in range(1, len(hdu)):
            del hdu[i].header['EXTNAME']

        new_sample_object = sample_object.replace('.fits', '_c.fits')
        hdu.writeto(new_sample_object, overwrite=True)

        # Try to open in astrodata
        ad = astrodata.open(new_sample_object)

        # Check if the tags are set correctly
        self.assertIn('SOAR', ad.tags)
        self.assertIn('SAM', ad.tags)
        self.assertIn('SAMI', ad.tags)
        self.assertIn('IMAGE', ad.tags)

        os.remove(new_sample_object)

class SAMI_DR(unittest.TestCase):

    def test_hello_world(self):

        self.fail("Implement me!")