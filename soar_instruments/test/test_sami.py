# -*- coding: utf-8 -*-

import glob
import os
import unittest

import soar_instruments
import soardr
import astrodata


class Test_IO(unittest.TestCase):

    path = "soar_instruments/test/data/"

    def test_acq(self):
        """
        Just check if the a DOMEFLAT obtained with SAMI is read correctly and if
        the tags are set properly.
        """
        sample_acq = os.path.join(self.path, "sami_acq.fits")

        # Check if file exists
        self.assertTrue(os.path.exists(sample_acq))

        # Try to open in astrodata
        ad = astrodata.open(sample_acq)

        # Check if the tags are set correctly
        self.assertIn('SOAR', ad.tags)
        self.assertIn('SAM', ad.tags)
        self.assertIn('SAMI', ad.tags)
        self.assertIn('IMAGE', ad.tags)

    def test_bias(self):
        """
        Just check if the a BIAS obtained with SAMI is read correctly and if
        the tags are set properly.
        """
        sample_bias = os.path.join(self.path, "sami_bias.fits")

        # Check if file exists
        assert os.path.exists(sample_bias)

        # Try to open in astrodata
        ad = astrodata.open(sample_bias)

        # Check if the tags are set correctly
        self.assertIn('SOAR', ad.tags)
        self.assertIn('SAM', ad.tags)
        self.assertIn('SAMI', ad.tags)
        self.assertIn('CAL', ad.tags)
        self.assertIn('BIAS', ad.tags)

    def test_domeflat(self):
        sample_flat = os.path.join(self.path, "sami_domeflat.fits")

        # Check if file exists
        self.assertTrue(os.path.exists(sample_flat))

        # Try to open in astrodata
        ad = astrodata.open(sample_flat)

        # Check if the tags are set correctly
        self.assertIn('SOAR', ad.tags)
        self.assertIn('SAM', ad.tags)
        self.assertIn('SAMI', ad.tags)
        self.assertIn('CAL', ad.tags)
        self.assertIn('FLAT', ad.tags)

    def test_object(self):
        """
        Just check if the an OBJECT obtained with SAMI is read correctly and if
        the tags are set properly.
        """
        sample_object = os.path.join(self.path, "sami_object.fits")

        # Check if file exists
        self.assertTrue(os.path.exists(sample_object))

        # Try to open in astrodata
        ad = astrodata.open(sample_object)

        # Check if the tags are set correctly
        self.assertIn('SOAR', ad.tags)
        self.assertIn('SAM', ad.tags)
        self.assertIn('SAMI', ad.tags)
        self.assertIn('IMAGE', ad.tags)

    def test_sky_flat(self):
        """
        Just check if the a SKYFLAT obtained with SAMI is read correctly and if
        the tags are set properly.
        """
        sample_flat = os.path.join(self.path, "sami_skyflat.fits")

        # Check if file exists
        self.assertTrue(os.path.exists(sample_flat))

        # Try to open in astrodata
        ad = astrodata.open(sample_flat)

        # Check if the tags are set correctly
        self.assertIn('SOAR', ad.tags)
        self.assertIn('SAM', ad.tags)
        self.assertIn('SAMI', ad.tags)
        self.assertIn('CAL', ad.tags)
        self.assertIn('FLAT', ad.tags)


class Test_Attributes(unittest.TestCase):

    path = "soar_instruments/test/data/"

    def test_datasec(self):

        files = glob.glob(os.path.join(self.path, "sami_*.fits"))

        for f in files:
            ad = astrodata.open(f)
            ad.data_section()

    def test_filters(self):

        files = glob.glob(os.path.join(self.path, "sami_*.fits"))

        for f in files:
            ad = astrodata.open(f)
            ad.filter_name()

    def test_gain(self):

        files = glob.glob(os.path.join(self.path, "sami_*.fits"))

        for f in files:
            ad = astrodata.open(f)
            ad.gain()
