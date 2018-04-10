import astrodata

from ..utilities import section_to_tuple

soar_keyword_names = dict(
    exposure_time='EXPTIME'
)


class AstroDataSOAR(astrodata.AstroDataFits):
    __keyword_dict = soar_keyword_names

    @staticmethod
    def _matches_data(source):

        if 'OBSERVAT' in source[0].header:
            return source[0].header['OBSERVAT'].strip().upper() == 'SOAR'

        elif 'TELESCOP' in source[0].header:
            return source[0].header['TELESCOP'] == 'SOAR 4.1m'

        else:
            return False

    @astrodata.astro_data_tag
    def _type_observatory(self):
        return astrodata.TagSet(['SOAR'])

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


class AstroDataDummy(AstroDataSOAR):

    __keyword_dict = dict(data_section='TRIMSEC')

    @staticmethod
    def _matches_data(source):
        if 'INSTRUME' in source[0].header:
            instrument = source[0].header.get('INSTRUME')
            instrument = instrument.strip()
            instrument = instrument.upper()
            return instrument in {'DUMMY'}
        else:
            False

    @astrodata.astro_data_tag
    def _tag_instrument(self):
        return astrodata.TagSet(['DUMMY'])

    @astrodata.astro_data_descriptor
    def data_section(self, pretty=False):
        return self._parse_section(self._keyword_for('data_section'), pretty)