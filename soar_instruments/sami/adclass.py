from astrodata import astro_data_tag, TagSet, astro_data_descriptor, returns_list
from ..soar import AstroDataSOAR

class AstroDataSAMI(AstroDataSOAR):

    @staticmethod
    def _matches_data(data_provider):
        return data_provider.phu.get('INSTRMT', '').upper() == 'SAMI'

    @astro_data_tag
    def _tag_instrument(self):
        return TagSet(['SAMI'])

    @astro_data_tag
    def _tag_flat(self):
        if self.phu.get('OBSTYPE') == 'SFLAT':
            return TagSet(['FLAT', 'CAL'])