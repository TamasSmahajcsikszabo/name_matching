from typing import List
from langdetect import detect
from googletrans import Translator, constants


'''
    The main concept for name matching is also to check for the language
    and if necessary translate the term to the entry to match its language.
'''

translator = Translator()

def translate(string1: str, string2: str)->List[str]:
    lang1 = detect(string1)
    lang2 = detect(string2)
    if lang1 != lang2:
        try:
            translation = translator.translate(string2, dest=lang1)
            if not isinstance(translation, list):
                string2 = str(translation.text)
        except BaseException as ex:
            print(ex)
    return [string1, string2]



if __name__ == '__main__':
    print('test case 1')
    print(translate("it's new", "das ist neu"))
