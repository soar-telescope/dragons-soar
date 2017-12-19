import re

from astrodata import astro_data_tag, TagSet, astro_data_descriptor, returns_list
from ..soar import AstroDataSOAR


class AstroDataSAMI(AstroDataSOAR):
    __keyword_dict = dict(
        data_section = 'DATASEC',
        gain = 'GAIN',
    )

    @staticmethod
    def _matches_data(data_provider):
        return data_provider.phu.get('INSTRMT', '').upper() == 'SAMI'

    @astro_data_tag
    def _tag_instrument(self):
        # QUESTIONS: is SAMI always used with the SAM AO?
        #    is SAMI used only at one telescopes or multiple ones?
        # ANSWER: yes, SAMI is always used with SAM and only at SOAR Telescope.
        return TagSet(['SAMI', 'SAM'])

    @astro_data_tag
    def _tag_flat(self):
        # Ideally, we would want 'IMAGE' to be set by the 'IMAGE' tag.
        # But since OBSTYPE is being used for both, not clear how that
        # can be done right now.
        obstype = self.phu.get('OBSTYPE', '')
        if 'FLAT' in obstype:
            return TagSet(['FLAT', 'CAL', 'IMAGE'])

    @astro_data_tag
    def _tag_twilight(self):
        if self.phu.get('OBSTYPE') == 'SFLAT':
            return TagSet(['TWILIGHT'])

    @astro_data_tag
    def _tag_domeflat(self):
        if self.phu.get('OBSTYPE') == 'DFLAT':
            return TagSet(['DOME'])

    @astro_data_tag
    def _tag_acquisition(self):
        # Ideally, we would want 'IMAGE' to be set by the 'IMAGE' tag.
        # But since OBSTYPE is being used for both, not clear how that
        # can be done right now.
        filename = self.phu.get('FILENAME', '')
        #notes = self.phu.get('NOTES', '')
        if re.search('acq.[0-9]+', filename):
            return TagSet(['ACQUISITION', 'IMAGE'])

    @astro_data_tag
    def _tag_image(self):
        # this one will need something like "if not FABRY keyword", I think.
        if self.phu.get('OBSTYPE') == 'OBJECT':
            return TagSet(['IMAGE'])

    @astro_data_tag
    def _tag_bias(self):
        if self.phu.get('OBSTYPE') == 'ZERO':
            return TagSet(['BIAS', 'CAL'], blocks=['IMAGE', 'FABRY'])

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


    @astro_data_descriptor
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

    @astro_data_descriptor
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
        for hdr in self.header[1:]:
            val = hdr[self.__keyword_dict['gain']]
            if val != 'unavail':
                gain.append(val)
            else:
                gain.append(None)
        return gain