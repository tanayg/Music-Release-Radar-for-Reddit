import config
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

def getArtistData(artistName):
    client_credentials_manager = SpotifyClientCredentials(config.spotify["clientId"], config.spotify["clientSecret"])
    spotify = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
    results = spotify.search(q='artist:' + artistName, type='artist')
    return results
