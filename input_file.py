class Input_File:
    """Class tha contains information about and the contents of the input file"""
    def __init__(self, filename):
        self.filename = filename
        self.name = filename.split('.')[0]
        self.extension = filename.split('.')[1]
        if self.extension != 'csv' and self.extension != 'ris':
            print 'Error: file extension not supported. Supported extensions are csv and ris.'
            sys.exit()
        f = open(self.filename, 'r')
        self.content = f.read()
        f.close()
