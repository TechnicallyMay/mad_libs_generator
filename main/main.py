import string
import re
import get_lyrics
import find_words


song = ["Fall Away", "Twenty One Pilots"]
lyrics = get_lyrics.get_song(song[0], song[1])
regex = re.compile('[%s]' % string.punctuation)
no_punct = regex.sub("", lyrics)

unique_words = []
for word in no_punct.lower().split(" "):
    if word not in unique_words:
        unique_words.append(word)

tagged = find_words.tag_pos(" ".join(unique_words))
print(unique_words)
