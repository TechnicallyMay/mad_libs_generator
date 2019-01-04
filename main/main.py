import get_lyrics
from mad_libs import MadLibs


number_replacements = 20

# song = "lips of an angel"
# artist = "hinder"
# lyrics = get_lyrics.get_song(song, artist)

libs = MadLibs("test")

# for i in range(number_replacements):
#     part_of_speech, to_replace = libs.pick_word()
#     word = input(part_of_speech + ": ").lower()
#     libs.replace_word(to_replace, word)
#
# libs.print()

print(libs.text)
