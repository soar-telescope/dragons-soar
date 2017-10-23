from astrodata import AstroDataFits, astro_data_tag, astro_data_descriptor, TagSet

soar_keyword_names = dict(
    exposure_time = 'EXPTIME'
)

class AstroDataSOAR(AstroDataFits):
    __keyword_dict = soar_keyword_names

    @staticmethod
    def _matches_data(data_provider):
        return data_provider.phu.get('OBSERVAT', '').upper() == 'SOAR'

    @astro_data_tag
    def _type_observatory(self):
        return TagSet(['SOAR'])

