import config
from spotify import *

def main():
    spotifyObj = Spotify(config.spotifyConfig["clientId"], config.spotifyConfig["clientSecret"])
    """albums = spotifyObj.getArtistTracksAndAlbums(config.artists["RL Grime"])
    for album in albums:
        print "Name: " + album[0] + " | Release Date: " + album[1] + " | Link: " + album[2]"""

    results = spotifyObj.getNewestTrackOrAlbum(config.artists["Sufjan Stevens"])
    print results


if __name__ == "__main__":
    main()
