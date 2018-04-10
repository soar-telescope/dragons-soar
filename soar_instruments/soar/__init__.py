__all__ = ['AstroDataSOAR', 'AstroDataDummy']


from .adclass import AstroDataSOAR, AstroDataDummy
from astrodata import factory

factory.addClass(AstroDataSOAR)
factory.addClass(AstroDataDummy)
