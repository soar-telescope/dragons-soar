import re

from astrodata import astro_data_tag, TagSet, astro_data_descriptor, returns_list
from ..soar import AstroDataSOAR


class AstroDataGOODMAN(AstroDataSOAR):

    __keyword_dict = dict(data_section='TRIMSEC')

    @staticmethod
    def _matches_data(source):
        return source[0].header.get('INSTRUME', '') == 'Goodman Spectro'

    @astro_data_tag
    def _tag_instrument(self):
        return TagSet(['GOODMAN'])
    
    @astro_data_tag
    def _tag_arc(self):
        if self.phu.get('OBSTYPE') == 'COMP':
            return TagSet(['ARC', 'CAL'])

    @astro_data_tag
    def _tag_bias(self):
        if self.phu.get('OBSTYPE') == 'BIAS':
            return TagSet(['BIAS', 'CAL'])

    @astro_data_tag
    def _tag_flat(self):
        if self.phu.get('OBSTYPE') == 'FLAT':
            return TagSet(['FLAT', 'CAL'])

    @astro_data_tag
    def _tag_red(self):
        if self.phu.get('INSTCONF') == 'Red':
            return TagSet(['RED'])

    @astro_data_tag
    def _tag_blue(self):
        if self.phu.get('INSTCONF') == 'Blue':
            return TagSet(['BLUE'])

    @astro_data_tag
    def _tag_image(self):
        if self.phu.get('CAM_TARG') == 0 and self.phu.get('WAVMODE') == 'Imaging':
            return TagSet(['IMAGE'])

    @astro_data_tag
    def _tag_acq(self):
        if self.phu.get('CAM_TARG') == 0 and self.phu.get('WAVMODE') != 'Imaging':
            return TagSet(['ACQ'])
        
    @astro_data_tag
    def _tag_spect(self):
        if self.phu.get('CAM_TARG') != 0 and self.phu.get('WAVMODE') != 'Imaging':
            return TagSet(['SPECT'])

    @astro_data_descriptor
    def instrument(self, generic=False):
        # The code existing here was removed because the file is checked during the load process. There is no need to
        # check it again here.
        return 'goodman'

    @astro_data_descriptor
    def data_section(self, pretty=False):
        """
        Returns the rectangular section that includes the pixels that would be
        exposed to light.  If pretty is False, a tuple of 0-based coordinates
        is returned with format (x1, x2, y1, y2).  If pretty is True, a keyword
        value is returned without parsing as a string.  In this format, the
        coordinates are generally 1-based.

        One tuple or string is return per extension/array, in a list. If the
        method is called on a single slice, the section is returned as a tuple
        or a string.

        Parameters
        ----------
        pretty : bool
         If True, return the formatted string found in the header.

        Returns
        -------
        tuple of integers or list of tuples
            Location of the pixels exposed to light using Python slice values.

        string or list of strings
            Location of the pixels exposed to light using an IRAF section
            format (1-based).
        """
        return self._parse_section(self._keyword_for('data_section'), pretty)
