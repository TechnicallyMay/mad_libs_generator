import find_pos
from random import choice
from collections import defaultdict


class MadLibs():

    def __init__(self, text):
        self.text = text
        tagged_text = find_pos.tag_pos(text)
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
            elif tag == "VBD" or tag == "VBN":
                key = "Past Verb"
            elif tag[0] == "V":
                key = "Present Verb"
            elif tag[0] == "J":
                key = "Adjective"
            else:
                continue
            for word in words:
                important[key].append(word)
        return(important)


    def pick_word(self):
        random_key = choice(list(self.pos.keys()))
        random_word = choice(self.pos[random_key])
        self.pos[random_key] = [word for word in self.pos[random_key]
                                              if word != random_word]
        if self.pos[random_key] == []:
            del(self.pos[random_key])
        return (random_key, random_word)


    def replace_word(self, to_replace, input):
        words = self.text.split()
        for i, word in enumerate(words):
            new_word = input
            if word[0].isupper():
                new_word = new_word.capitalize()
            if word[-1] == ',':
                word = word.replace(",", "")
                new_word += ","
            if word.lower() == to_replace:
                words[i] = new_word
        self.text = " ".join(words)


    def print(self):
        for word in self.text.split():
            if word[0].isupper() and word != "I" and word != "I'm":
                print('\n' + word, end = " ")
            else:
                print(word, end = " ")
