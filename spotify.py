import config
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

client_credentials_manager = SpotifyClientCredentials(config.spotify["clientId"], config.spotify["clientSecret"])
spotifyApi = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

def getArtistSongsAndAlbums(artistId):
    result = spotifyApi.artist_albums(artistId)
    retVal = [] # List of tuples that contain (Album Name, Release Date, Spotify Link)
    for album in result["items"]:
        if album["album_type"] == "single":
            retVal.append((album["name"], album["release_date"], getTrackLinkFromAlbum(album["external_urls"]["spotify"])))
        else:
            retVal.append((album["name"], album["release_date"], album["external_urls"]["spotify"]))
    return retVal

def getTrackLinkFromAlbum(albumId):
    result = spotifyApi.album_tracks(albumId)
    return result["items"][0]["external_urls"]["spotify"]