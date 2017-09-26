from io import open

class Author:

    def __init__(self, name, language):
        self.name = name
        self.language = language

def all_authors(authors_txt_path):
    raw_authors = []

    with open(authors_txt_path, 'r', encoding="utf-8") as f:
        raw_authors = list(map(lambda sentence: sentence.strip(), f.readlines()))

    def to_author(txt_line):
        splitted = [x.strip() for x in txt_line.split(',')]
        return Author(splitted[0], splitted[1])

    return list(map(to_author, raw_authors))
