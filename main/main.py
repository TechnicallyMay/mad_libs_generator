import get_lyrics
from mad_libs import MadLibs

song = ["Nico and the Niners", "Twenty One Pilots"]
lyrics = get_lyrics.get_song(song[0], song[1])

libs = MadLibs(lyrics)

for pos, words in libs.pos.items():
    print(pos, ": ", words)
    print("\n\n\n")
