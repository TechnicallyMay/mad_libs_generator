import nltk


nltk.download("punkt")
nltk.download('averaged_perceptron_tagger')


def tag_pos(text):
    tokens = nltk.word_tokenize(text)
    tagged = nltk.pos_tag(tokens)
    return tagged
