from bs4 import BeautifulSoup
import requests
import pprint
import config
import spotipy
from spotipy.oauth2 import SpotifyOAuth


# Scraping Billboard 100
date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")
# date = "1984-06-27"

response = requests.get(f"https://www.billboard.com/charts/hot-100/{date}")
billboard_webpage = response.text
soup = BeautifulSoup(billboard_webpage, "html.parser")
song_names = [song.getText() for song in soup.find_all(name="span", class_="chart-element__information__song")]
# song_names = ['Incomplete', 'Bent', "It's Gonna Be Me"]
# print(song_names)

#Spotify Authentication
SPOTIPY_CLIENT_ID = config.client_id
SPOTIPY_CLIENT_SECRET = config.client_secret
SPOTIPY_REDIRECT_URI = 'http://example.com'
sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri=SPOTIPY_REDIRECT_URI,
        client_id=SPOTIPY_CLIENT_ID,
        client_secret=SPOTIPY_CLIENT_SECRET,
        show_dialog=True,
        cache_path="token.txt"
    )
)

user_id = sp.current_user()["id"]
# print(user_id)

#Searching Spotify for songs by title
pp = pprint.PrettyPrinter()
song_uris = []
year = date.split("-")[0]
for song in song_names:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    # pp.pprint(result)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        # print(uri)
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")


#Creating a new private playlist in Spotify
playlist = sp.user_playlist_create(user=user_id, name=f"{date} Billboard 100", public=False)
# print(playlist)
#Adding songs found into the new playlist
result = sp.user_playlist_add_tracks(user=user_id, playlist_id=playlist["id"], tracks=song_uris, position=None)
print(result)