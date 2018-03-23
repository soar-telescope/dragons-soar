
import unittest
import os

import soar_instruments
import astrodata


class Test_IO(unittest.TestCase):

    path = "soar_instruments/test/data/"

    def test_other_file(self):

        empty_fits = os.path.join(self.path, "empty_file.fits")

        # Check if file exists
        self.assertTrue(os.path.exists(empty_fits))

        # Try to open in astrodata
        ad = astrodata.open(empty_fits)

        # Check if the tags are set correctly
        self.assertNotIn('SOAR', ad.tags)
        self.assertNotIn('SAMI', ad.tags)
        self.assertNotIn('SAM', ad.tags)
        self.assertNotIn('Goodman', ad.tags)

    @unittest.skip
    def test_dummy_class(self):

        empty_fits = os.path.join(self.path, "dummy_file.fits")

        # Check if file exists
        self.assertTrue(os.path.exists(empty_fits))

        # Try to open in astrodata
        ad = astrodata.open(empty_fits)

        self.assertIn('DUMMY', ad.tags)