#!/usr/bin/python

"""
This tool har primarily been tested on citations exported from OnePetro.
"""

import sys

"""
Currently missing "translations":
    * ID/J2 -> Some sort of Document ID
    * DATE/DA -> Exact publication date. Translate to year+month

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
                  'VL':'volume',
                  'PB':'publisher',
                  'TI':'title',
                  'AB':'abstract',
                  'C1':'organization' # This is a custom field, translation may not alway 
                  'TY':'type'}

csv_dictionary = {'Authors':'author',
                  'DOI':'doi',
                  'Publisher':'publisher',
                  'Society Code':'organization',
                  'Title':'title'
                  }



class File:
    """Class tha contains information about and the contents of the input file"""
    def __init__(self, filename):
        self.filename = filename
        self.name = filename.split('.')[0]
        self.extension = filename.split('.')[1]
        f = open(self.filename, 'r')
        self.content = f.read()
        f.close()


# Terminating if first parameter is missing
if len(sys.argv) < 2:
    print 'Error: Missing argument - Need name of input file as first argument.'
    sys.exit()

# Initiating file object and reading file contents
file = File(str(sys.argv[1]))





# Debug printing
print 'Number of arguments:', len(sys.argv), 'arguments.'
print 'Argument List:', str(sys.argv)
print 'Filename: ', file.filename
print 'Name: ', file.name
print 'Extension: ', file.extension
print 'File content: ', file.content