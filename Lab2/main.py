import nltk
from nltk.book import *
nltk.download()

def lexical_diversity(text):
    return len(text) / len(set(text))

print(len(text2), len(set(text2)))