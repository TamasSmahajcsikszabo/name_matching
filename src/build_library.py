import os
from utils import tokenize
from lemmatize import lemmatize
from synonyms import get_synonyms
import pandas as pd
import pathlib
import pickle
import string
from rapidfuzz import fuzz
from utils import tokenize
from translate import translate

'''
    The concept of this name matching module is to pre-build a library
    of terms. Each term is stored in its alphabetically matching section
    of this library, e.g. apple is stored in library[a].

    Each record of each section corresponds to one test data record and has
    the lemmatized version of the original text and its synonyms stored.
'''


keys = list(string.ascii_lowercase)
library = {}
for k in keys:
    library[k] = []


def load_library(path):
    '''
        Loads the library on the given path.
    '''
    try:
        with open(path, 'rb') as file:
            library = pickle.load(file)
            return library
    except BaseException as ex:
        print(ex)
        return []


def lookupLibrarySection(library, term):
    '''
        A helper function to look up the matching library section for the
        search term.
    '''
    first_letter = str.lower(term.split()[0][0])
    try:
        return library[first_letter]
    except BaseException as ex:
        return []


def process(text, term):
    '''
        Wrapper for rapidfizz.fuzz for string matching ratio.
    '''
    return fuzz.ratio(text, term) / 100


def lookupTermInSection(section, term):
    '''
        Looks up the term in a the given section of the library.
    '''
    term = ' '.join(tokenize(term))
    texts = [' '.join(tokenize(entry['text'])) for entry in section]
    ratios = [process(text, term) for text in texts]
    found = [(texts[i], ratios[i])
             for i in range(len(texts)) if ratios[i] > 0.5]
    return found


if __name__ == '__main__':
    parent = pathlib.Path(__file__).parent.absolute()
    datadir = os.path.join(parent, '..', 'data', 'name_matching_test_data.csv')
    data = pd.read_csv(datadir)
    terms = data['term'].tolist()
    entries = data['entry'].tolist()
    res = data['match'].tolist()

    for e in entries:
        lemmas = lemmatize(e)
        synonyms = get_synonyms(lemmas)
        entry = {
            'text': e,
            'syonyms': synonyms
        }
        first_letter = str.lower(e.split()[0][0])
        try:
            library[first_letter].append(entry)
        except BaseException as ex:
            print(ex)

        # library[e] = entry

    targetdir = os.path.join(parent, '..', 'data', 'libary.pickle')
    with open(targetdir, 'wb') as file:
        pickle.dump(library, file, protocol=pickle.HIGHEST_PROTOCOL)
