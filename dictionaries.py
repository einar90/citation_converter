"""
Currently missing "translations":
    * ID/J2 -> Some sort of Document ID
    * DATE/DA -> Exact publication date. Translate to year+month
    * SP, EP = Start Page, End Page -> Convert to 'pages=x-y'

Issues: 
    * 'C1':'organization'
        This is a custom field, "translation" may not always be correct.
"""

ris_dictionary = {'SN':'isbn',
                  'AU':'author',
                  'A2':'author',
                  'A3':'author',
                  'A4':'author',
                  'ET':'edition',
                  'PY':'year',
                  'UR':'url',
                  'DO':'doi',
                  'VL':'volume',
                  'J2':'ja',
                  'PB':'publisher',
                  'TI':'title',
                  'AB':'abstract',
                  'C1':'organization',
                  'N1':'note'}

ris_type_dictionary = {'CONF':'inproceedings',
                       'CPAPER':'inproceedings',
                       'BOOK':'book',
                       'CHAPTER':'inbook'
                       }

csv_dictionary = {'Authors':'author',
                  'DOI':'doi',
                  'Publisher':'publisher',
                  'Society Code':'organization',
                  'Title':'title'
                  }

def convert_ris_date(ris_date):
    return ris_date.split('/')[0]


def convert_csv_date(csv_date):
    return {csv_date.split(' ')[-1]}


