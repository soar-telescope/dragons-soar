# -*- coding: utf-8 -*-


def test_installation():

    from astropy.io import fits as pyfits

    import soar_instruments
    import soardr
    import astrodata

    from recipe_system.mappers import recipeMapper
    from recipe_system.mappers import primitiveMapper
    from recipe_system.reduction.coreReduce import Reduce