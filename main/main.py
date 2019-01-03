import get_lyrics
from mad_libs import MadLibs

song = "Nico and the Niners"
artist = "Twenty One Pilots"
lyrics = get_lyrics.get_song(song, artist)

libs = MadLibs(lyrics)

libs.print()
