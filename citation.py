import dictionaries as Dictionary

class Citation:
    """Class that holds the parsed citation"""
    def __init__(self, input_file):
        self.input_file = input_file
        self.fields = {}
        if self.input_file.extension == 'csv':
            self.parse_csv()
        elif self.input_file.extension == 'ris':
            self.parse_ris()
    def add_field(self, key, value):
        self.fields[key] = value
    def add_author(self, author):
        if self.fields.get('author'):
            self.fields['author'].append(author)
        else:
            self.fields['author'] = [author]
    def set_type(self, citation_type):
        if Dictionary.ris_type_dictionary.get(citation_type):
            self.citation_type = Dictionary.ris_type_dictionary.get(citation_type)
        else:
            print 'Citation type \'', citation_type, '\' not recognized.'
    def parse_csv(self):
        print 'Parsing csv.'
    def parse_ris(self):
        lines = self.input_file.content.split('\r\n') # Splitting lines
        lines = [line.split('  - ') for line in lines] # Splitting entries into key,value
        unknown_keys = []
        for line in lines:
            if line[0] == 'AU' or line[0] == 'A2' or line[0] == 'A3':
                self.add_author(line[1])
            elif Dictionary.ris_dictionary.get(line[0]):
                self.add_field(Dictionary.ris_dictionary.get(line[0]), line[1])
            elif line[0] == 'DA':
                self.add_field('year', Dictionary.convert_ris_date(line[1]))
            elif line[0] == 'TY':
                self.set_type(line[1])
            elif line[0] == 'ER':
                continue
            else: # Key not recognized
                print line[0]
                unknown_keys.append(line[0])
        if len(unknown_keys) > 0 and unknown_keys != ['']:
            print 'Unknown keys: ', unknown_keys
