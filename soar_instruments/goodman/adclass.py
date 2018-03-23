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
    def _tag_spect(self):
        if self.phu.get('CAM_TARG') != 0 and self.phu.get('WAVMODE') != 'Imaging':
            return TagSet(['SPECT'])

    @astro_data_descriptor
    def instrument(self, generic=False):
        return 'goodman'
