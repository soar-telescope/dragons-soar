# -*- coding: utf-8 -*-
"""
    Test SOAR Data-Reduction

    Methods and Classes created to test SOAR generic data.
"""
import glob
import os
import signal
import subprocess

from astropy.io import fits
from unittest import TestCase, skip, main


class TestSoarDrScript(TestCase):

    def setUp(self):

        path_empty = './empty_folder'
        log_file = os.path.join(path_empty, 'reduce.log')

        if os.path.exists(log_file):
            os.remove(log_file)

        if os.path.exists(path_empty):
            os.rmdir(path_empty)

    def tearDown(self):
        pass

    def test_soar_dr_fails_on_empty_folder(self):

        # Bruno discovered recently that the SOAR software team is developing a
        #  tool to reduce SOAR data. Bruno is very skeptical and wants to try
        #  it. He goes to a random folder that contains no data and run the
        #  'reduce' command. Since there is no SOAR data inside, he expects an
        #  error message and that the program leaves.
        path = './empty_folder'
        abs_path = os.path.abspath(path)
        os.mkdir(abs_path)
        os.chdir(abs_path)

        process = subprocess.Popen(["reduce"])
        stdoutdata, stderrdata = process.communicate()

        self.assertEqual(signal.SIGIO.value, process.returncode)

        os.remove('./reduce.log')
        os.chdir('../')
        os.rmdir(path)

    def test_finds_fits_images(self):

        # Bruno is still not trusting much the code. He does not believe that
        #  `reduce` can recognise if an image was obtained with SOAR or not.
        #  To check that, Bruno creates again that empty folder, enters it, add
        #  an empty FITS file. He expects the software to find it, read and exit
        #  since this data was not obtained at SOAR.
        path = './empty_folder'
        os.mkdir(path)
        os.chdir(path)

        filename = './empty_file.fits'
        hdu = fits.ImageHDU()
        hdu.writeto(filename)

        fits_files = glob.glob(filename)
        process = subprocess.Popen(["reduce"] + fits_files)
        stdoutdata, stderrdata = process.communicate()

        self.assertEqual(signal.SIGHUP.value, process.returncode)

        os.remove(filename)
        os.remove('./reduce.log')
        os.chdir('../')
        os.rmdir(path)

    # @skip
    # def test_finds_soar_data(self):
    #
    #     # Now Bruno wants to know if the `reduce` command can find data obtained
    #     # at SOAR. Bruno as access to the data of every instrument at SOAR and
    #     # but he will only try with a single file. He runs `reduce` with no
    #     # arguments and finds out that the `soar_instruments` module was not
    #     # loaded.
    #     path = './data'
    #     self.assertRaises(SystemExit, Reduce)
    #
    #     # He then re-runs the command line, adds the `--adpkg soar_instrument`
    #     # argument and expects that the data-reduction process starts and ends
    #     # with no error. Since this is a single image, there is actually nothing
    #     # to be done, so the program will leave.
    #     args = Namespace(adpkg='soar_instruments')
    #     reduce = Reduce(args)


if __name__ == '__main__':
    main()






