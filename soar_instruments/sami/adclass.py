import re
import astrodata

from astrodata import (astro_data_tag, TagSet, astro_data_descriptor,
                       returns_list)
from astrodata.fits import FitsLoader, FitsProvider
from ..soar import AstroDataSOAR


class AstroDataSAMI(AstroDataSOAR):

    __keyword_dict = dict(data_section='DATASEC', gain='GAIN')

    @staticmethod
    def _matches_data(source):
        return source[0].header.get('INSTRUME', '').upper() in {'SAMI', 'SAM'}

    @astrodata.astro_data_tag
    def _tag_instrument(self):
        # QUESTIONS:
        # 1) is SAMI always used with the SAM AO?
        # 2) is SAMI used only at one telescopes or multiple ones?
        # ANSWER:
        # 1) SAMI is always used withing SAM but not always with AO.
        # 2) SAMI and SAM are only used at SOAR Telescope.
        return astrodata.TagSet(['SAMI', 'SAM'])

    @astrodata.astro_data_tag
    def _tag_flat(self):
        # Ideally, we would want 'IMAGE' to be set by the 'IMAGE' tag.
        # But since OBSTYPE is being used for both, not clear how that
        # can be done right now.
        obstype = self.phu.get('OBSTYPE', '')
        if 'FLAT' in obstype:
            return astrodata.TagSet(['FLAT', 'CAL', 'IMAGE'])

    @astrodata.astro_data_tag
    def _tag_twilight(self):
        if self.phu.get('OBSTYPE') == 'SFLAT':
            return astrodata.TagSet(['TWILIGHT'])

    @astrodata.astro_data_tag
    def _tag_domeflat(self):
        if self.phu.get('OBSTYPE') == 'DFLAT':
            return astrodata.TagSet(['DOME'])

    @astrodata.astro_data_tag
    def _tag_acquisition(self):
        # Ideally, we would want 'IMAGE' to be set by the 'IMAGE' tag.
        # But since OBSTYPE is being used for both, not clear how that
        # can be done right now.
        filename = self.phu.get('FILENAME', '')
        notes = self.phu.get('NOTES', '')

        if re.search('acq.[0-9]+', filename) or re.search('/acq/i',  notes):
            return astrodata.TagSet(['ACQUISITION', 'IMAGE'])

    @astrodata.astro_data_tag
    def _tag_image(self):
        # this one will need something like "if not FABRY keyword", I think.
        if self.phu.get('OBSTYPE') == 'OBJECT':
            return astrodata.TagSet(['IMAGE'])

    @astrodata.astro_data_tag
    def _tag_bias(self):
        if self.phu.get('OBSTYPE') == 'ZERO':
            return astrodata.TagSet(['BIAS', 'CAL'], blocks=['IMAGE', 'FABRY'])

    @astrodata.astro_data_descriptor
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

    @astrodata.astro_data_descriptor
    def filter_name(self):
        """
        Returns the name of the filter used according to the summary FILTERS
        keyword.

        Returns
        -------
        str
            The name of the filter.

        """
        return self.phu.get('FILTERS')

    @astrodata.astro_data_descriptor
    def gain(self):
        """
        Gain of the amplifier

        Returns
        -------
        float
            The gain for each amplifier
        """
        # Bruno:  GAIN is set to "unavail" in the headers. Do you have
        #         the gain for each amp in some lookup table?
        gain = []
        for ad in self[1:]:
            val = ad.hdr['gain']
            if val != 'unavail':
                gain.append(val)
            else:
                gain.append(None)
        return gain

    @classmethod
    def load(cls, source):

        def sami_parser(hdu):
            m = re.match('im(\d)', hdu.header.get('EXTNAME', ''))
            if m:
                hdu.header['EXTNAME'] = ('SCI', 'Added by AstroData')
                hdu.header['EXTVER'] = (int(m.group(1)), 'Added by AstroData')

        return cls(FitsLoader(FitsProvider).load(source,
                                                 extname_parser=sami_parser))