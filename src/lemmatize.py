import nltk
nltk.download('wordnet')
from nltk.stem import WordNetLemmatizer
from utils import tokenize

lemmatizer = WordNetLemmatizer()
stemmer = nltk.PorterStemmer()

def lemmatize(string1):
    list1 = tokenize(string1)
    list1_lemmas = [lemmatizer.lemmatize(l) for l in list1]
    return ' '.join(list1_lemmas)
