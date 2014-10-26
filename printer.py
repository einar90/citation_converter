from citation import Citation

def build_string(citation):
    string = ''
    string += '@' + citation.citation_type + '{'
    string += citation.fields.get('author')[0].split(',')[0].lower() # First author surname
    string += citation.fields.get('year') + '\n'
    for key in citation.fields:
        if key == 'author':
            string += '\tauthor = {'
            for author in citation.fields.get('author'):
                string += author
                if author != citation.fields.get('author')[-1]:
                    string += ' and '
            string += '}\n'
        else:
            string += '\t' + key + ' = {' + citation.fields.get(key) + '}\n'
    string += '}\n'
    return string

class Printer:
    """Object in charge of printing the converted reference"""
    def __init__(self, citation, destination):
        self.citation = citation
        self.destination = destination
        self.print_citation()
    def print_citation(self):
        string = build_string(self.citation)
        if self.destination == 'console':
            print string
        else:
            f = open(self.destination, 'a')
            f.write(string)

