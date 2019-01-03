import nltk
import re
import string
from collections import defaultdict


nltk.download("punkt")
nltk.download('averaged_perceptron_tagger')


def tag_pos(text):
    tokens = nltk.word_tokenize(text)
    tagged = nltk.pos_tag(tokens)
    clean = remove_punctuation(tagged)
    sorted = sort_by_pos(clean)
    return sorted


def remove_punctuation(tagged_text):
    no_punct = []
    regex = re.compile('[%s]' % string.punctuation)
    for word, pos in tagged_text:
        clean = regex.sub("", word).lower()
        no_punct.append((clean, pos))
    return no_punct


def sort_by_pos(tokens):
    parts_of_speech = defaultdict(list)
    punct = string.punctuation
    for word, tag in tokens:
        if len(word) > 2:
            parts_of_speech[tag].append(word)
    return parts_of_speech
