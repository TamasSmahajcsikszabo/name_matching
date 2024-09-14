import string
from typing import List


def standardize(text: str) -> str:
    '''
        Text standardization
        Converts to lower case and removes punctiation.
    '''
    text = text.lower()
    return "".join(char for char in text
                   if char not in string.punctuation)


def tokenize(text: str) -> List[str]:
    '''
        Tokenizes text after standardization
    '''
    text = standardize(text)
    return text.split()
