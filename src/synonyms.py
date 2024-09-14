from itertools import chain
from nltk.corpus import wordnet
from utils import tokenize


def get_synonyms(string, library=None):
    input = tokenize(string)
    result = {}
    for i in input:
        if library is None:
            synonyms = wordnet.synsets(i)
            lemmas = set(
                chain.from_iterable(
                    [word.lemma_names() for word in synonyms]))
            result[i] = lemmas
        else:
            result[i] = library.get(i)

    return result


if __name__ == '__main__':
    print(get_synonyms("Mr."))
