from astrodata import AstroDataFits, astro_data_tag, astro_data_descriptor, TagSet

from ..utilities import section_to_tuple

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

    # Utilities
    def _parse_section(self, keyword, pretty):
        try:
            value_filter = (str if pretty else section_to_tuple)
            process_fn = lambda x: (None if x is None else value_filter(x))
            # Dummy keyword FULLFRAME returns shape of full data array
            if keyword == 'FULLFRAME':
                try:
                    sections = '[1:{1},1:{0}]'.format(*self.data.shape)
                except AttributeError:
                    sections = ['[1:{1},1:{0}]'.format(*ext.shape)
                                for ext in self.data]
            else:
                sections = self.hdr.get(keyword)
            if self.is_single:
                return process_fn(sections)
            else:
                return [process_fn(raw) for raw in sections]
        except (KeyError, TypeError):
            return None
