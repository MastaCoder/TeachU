import nltk
from textblob import Word
from textblob import TextBlob
import sys


def parse(string):
    txt = TextBlob(string)
    for sentence in txt.sentences:
        print(sentence)


with open('notes', encoding="utf8") as file:
    notes = file.read()

parse(notes)