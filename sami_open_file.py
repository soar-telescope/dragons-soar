#!python
# -*- coding: utf-8 -*-

import soar_instruments
import astrodata

filename = '/Users/Bruno/GitHub/dragons-soar/sample_data/sami_bias.fits'

ad = astrodata.open(filename)
print ad.info()