import config
from spotify import *
from reddit import *

def main():
    spotifyObj = Spotify(config.spotifyConfig["clientId"], config.spotifyConfig["clientSecret"])
    """albums = spotifyObj.getArtistTracksAndAlbums(config.artists["RL Grime"])
    for album in albums:
        print "Name: " + album[0] + " | Release Date: " + album[1] + " | Link: " + album[2]"""

    results = spotifyObj.getNewestTrackOrAlbum(config.artists["Sufjan Stevens"])
    print results

    redditObj = Reddit(config.redditConfig["userAgent"], config.redditConfig["clientId"], config.redditConfig["clientSecret"], 
    config.redditConfig["username"], config.redditConfig["password"], config.subreddits[0])


if __name__ == "__main__":
    main()
