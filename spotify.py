import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

class Spotify:
    def __init__(self, clientId, clientSecret):
        self.spotifyApi = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(clientId, clientSecret))

    def getTrackOrAlbumArtists(self, artists):
        artistList = ""

        for artist in artists:
            if artistList != "":
                artistList = artistList + ", "
            artistList = artistList + artist["name"]
        
        return artistList

    def getArtistTracksAndAlbums(self, artistId):
        result = self.spotifyApi.artist_albums(artistId)
        retVal = [] # List of tuples that contain (Artist Names, Album Name, Release Date, Spotify Link)

        for album in result["items"]:
            artists = self.getTrackOrAlbumArtists(album["artists"])
            albumName = album["name"]
            releaseDate = album["release_date"]
            trackLink = ""

            if album["album_type"] == "single":
                trackLink = self.getTrackLinkFromAlbum(album["external_urls"]["spotify"])
            else:
                trackLink = album["external_urls"]["spotify"]
            
            retVal.append((artists, albumName, releaseDate, trackLink))
        
        return retVal

    def getTrackLinkFromAlbum(self, albumId):
        result = self.spotifyApi.album_tracks(albumId)
        return result["items"][0]["external_urls"]["spotify"]

    def getNewestTrackOrAlbum(self, artistId):
        artistReleases = self.getArtistTracksAndAlbums(artistId)
        latestReleaseDate = "0000-00-00"
        latestReleaseIndex = 0

        for i, release in enumerate(artistReleases):
            if release[2] > latestReleaseDate:
                latestReleaseDate = release[2]
                latestReleaseIndex = i

        return artistReleases[latestReleaseIndex]
