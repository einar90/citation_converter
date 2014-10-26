#!/usr/bin/python

"""
This tool har primarily been tested on citations exported from OnePetro.
"""

import sys
from input_file import Input_File
from citation import Citation
from printer import Printer

# Terminating if first parameter is missing
if len(sys.argv) < 2:
    print 'Error: Missing argument - Need name of input file as first argument.'
    sys.exit()
elif len(sys.argv) == 2:
    destination = 'console'
elif len(sys.argv) == 3:
    destination = sys.argv[2]
elif len(sys.argv) < 3:
    print 'Too many arguments.'
    print 'Example calls:'
    print 'python citation_converter.py inputfile.ris'
    print 'python citation_converter.py inputfile.ris outputfile.bib'

# Initiating file object and reading file contents
input_file = Input_File(str(sys.argv[1]))
citation = Citation(input_file)
printer = Printer(citation, destination)





# Debug printing
# print 'Number of arguments:', len(sys.argv), 'arguments.'
# print 'Argument List:', str(sys.argv)
# print 'Filename: ', input_file.filename
# print 'Name: ', input_file.name
# print 'Extension: ', input_file.extension
# print 'File content: ', input_file.content
# print 'Citation fields: ', citation.fields
