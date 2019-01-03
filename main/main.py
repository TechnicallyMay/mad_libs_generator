import get_lyrics
from mad_libs import MadLibs


number_replacements = 10

song = "Migraine"
artist = "Twenty One Pilots"
lyrics = get_lyrics.get_song(song, artist)

libs = MadLibs(lyrics)

for i in range(number_replacements):
    part_of_speech, to_replace = libs.pick_word()
    word = input(part_of_speech + " : ").lower()
    libs.replace_word(to_replace, word)

libs.print()
