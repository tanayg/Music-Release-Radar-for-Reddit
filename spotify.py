import config
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

def getArtistData(artistId):
    client_credentials_manager = SpotifyClientCredentials(config.spotify["clientId"], config.spotify["clientSecret"])
    spotify = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
    #results = spotify.artist(artistId)
    results = spotify.artist_albums(artistId)
    return results
