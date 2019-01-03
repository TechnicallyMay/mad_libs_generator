import find_words
from collections import defaultdict


class MadLibs():

    def __init__(self, text):
        self.text = text
        tagged_text = find_words.tag_pos(text)
        self.pos = self.find_important_pos(tagged_text)


    def find_important_pos(self, tagged):
        important = defaultdict(list)
        for tag, words in tagged.items():
            if tag == "NN":
                key = "Singular Noun"
            elif tag == "NNS":
                key = "Plural Noun"
            elif tag == "NNP" or tag == "NNPS":
                key = "Proper Noun"
            elif tag[0] == "V":
                key = "Verb"
            elif tag[0] == "J":
                key = "Adjective"
            elif tag[0] == "P":
                key = "Pronoun"
            elif tag[0] == "R":
                key = "Adverb"
            else:
                key = "Unimportant"
            for word in words:
                important[key].append(word)
        return(important)
