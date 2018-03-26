
import os
import unittest

import soar_instruments
import astrodata


class TestBlueIo(unittest.TestCase):

    path = "soar_instruments/test/data/"

    def tag_checker(self, filename, tags):

        sample = os.path.join(self.path, filename)

        # Check if file exists
        self.assertTrue(os.path.exists(sample))

        # Try to open in astrodata
        ad = astrodata.open(sample)

        self.assertEqual(ad.instrument(), 'goodman')

        # Check if the tags are set correctly
        for t in tags:
            self.assertIn(t, ad.tags)

        for t in ad.tags:
            self.assertIn(t, tags)

        for t in ad.tags:
            self.assertIn(t, tags)

    def test_acq(self):

        filename = "goodman_blue_acq.fits"
        expected_tags = ['SOAR', 'GOODMAN', 'BLUE', 'ACQ']
        self.tag_checker(filename, expected_tags)

    def test_bias(self):

        filename = "goodman_blue_bias.fits"
        expected_tags = ['SOAR', 'GOODMAN', 'BLUE', 'CAL', 'BIAS', 'SPECT']
        self.tag_checker(filename, expected_tags)

    def test_comp(self):

        filename = "goodman_blue_comp.fits"
        expected_tags = ['SOAR', 'GOODMAN', 'BLUE', 'CAL', 'ARC', 'SPECT']
        self.tag_checker(filename, expected_tags)

    def test_flat(self):

        filename = "goodman_blue_flat.fits"
        expected_tags = ['SOAR', 'GOODMAN', 'BLUE', 'CAL', 'FLAT', 'SPECT']
        self.tag_checker(filename, expected_tags)

    def test_imag(self):

        filename = "goodman_blue_imag.fits"
        expected_tags = ['SOAR', 'GOODMAN', 'BLUE', 'IMAGE']
        self.tag_checker(filename, expected_tags)

    def test_spec(self):
        filename = "goodman_blue_spec.fits"
        expected_tags = ['SOAR', 'GOODMAN', 'BLUE', 'SPECT']
        self.tag_checker(filename, expected_tags)


class TestRedIo(unittest.TestCase):

    path = "soar_instruments/test/data/"

    def tag_checker(self, filename, tags):

        sample = os.path.join(self.path, filename)

        # Check if file exists
        self.assertTrue(os.path.exists(sample))

        # Try to open in astrodata
        ad = astrodata.open(sample)

        # Check if the tags are set correctly
        for t in tags:
            self.assertIn(t, ad.tags)

    def test_acq(self):

        filename = "goodman_red_acq.fits"
        expected_tags = ['SOAR', 'GOODMAN', 'RED', 'ACQ']
        self.tag_checker(filename, expected_tags)

    def test_bias(self):

        filename = "goodman_red_bias.fits"
        expected_tags = ['SOAR', 'GOODMAN', 'RED', 'CAL', 'BIAS', 'SPECT']
        self.tag_checker(filename, expected_tags)

    def test_comp(self):

        filename = "goodman_red_comp.fits"
        expected_tags = ['SOAR', 'GOODMAN', 'RED', 'CAL', 'ARC', 'SPECT']
        self.tag_checker(filename, expected_tags)

    def test_flat(self):

        filename = "goodman_red_flat.fits"
        expected_tags = ['SOAR', 'GOODMAN', 'RED', 'CAL', 'FLAT', 'SPECT']
        self.tag_checker(filename, expected_tags)

    def test_imag(self):

        filename = "goodman_red_imag.fits"
        expected_tags = ['SOAR', 'GOODMAN', 'RED', 'IMAGE']
        self.tag_checker(filename, expected_tags)

    def test_spec(self):

        filename = "goodman_red_spec.fits"
        expected_tags = ['SOAR', 'GOODMAN', 'RED', 'SPECT']
        self.tag_checker(filename, expected_tags)
