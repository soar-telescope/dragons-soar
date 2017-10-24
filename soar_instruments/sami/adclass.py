import re

from astrodata import astro_data_tag, TagSet, astro_data_descriptor, returns_list
from ..soar import AstroDataSOAR

class AstroDataSAMI(AstroDataSOAR):

    @staticmethod
    def _matches_data(data_provider):
        return data_provider.phu.get('INSTRMT', '').upper() == 'SAMI'

    @astro_data_tag
    def _tag_instrument(self):
        # QUESTIONS: is SAMI always used with the SAM AO?
        #    is SAMI used only at one telescopes or multiple ones?
        return TagSet(['SAMI'])

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

