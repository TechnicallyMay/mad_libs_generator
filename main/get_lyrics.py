import requests
from bs4 import BeautifulSoup


def format_url(str):
    remove = ["-", "'"]
    for char in remove:
        str = str.replace(char, "")
    str = str.replace(" ", "-")
    return(str.lower())


def get_song(song, artist):
    song = format_url(song)
    artist = format_url(artist)
    url = 'http://www.metrolyrics.com/' + song +  '-lyrics-' + artist + '.html'
    return get_lyrics(url)


def get_lyrics(link):
    website = requests.get(link)
    code = website.status_code
    if code != requests.codes.ok:
        return
    soup = BeautifulSoup(website.text, 'html.parser')
    txt = soup.find_all('p', {"class":"verse"})
    txt = [part.text.split() for part in txt]
    #Splits list of lists into one list
    txt = [word for part in txt for word in part]
    lyrics = " ".join(txt)
    lyrics = clean_lyrics(lyrics)
    return lyrics


def clean_lyrics(lyrics):
    lyrics = lyrics.split()
    lyrics = [lyric for lyric in lyrics if '[' not in lyric and ']' not in lyric]
    return " ".join(lyrics)
