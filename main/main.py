import get_lyrics
from mad_libs import MadLibs


number_replacements = 20

song = "right now"
artist = "korn"
lyrics = get_lyrics.get_song(song, artist)

libs = MadLibs(lyrics)

for i in range(number_replacements):
    part_of_speech, to_replace = libs.pick_word()
    word = input(part_of_speech + ": ").lower()
    libs.replace_word(to_replace, word)

libs.print()
