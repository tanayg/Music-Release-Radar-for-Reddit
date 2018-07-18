import config
import time
from spotify import *
from reddit import *

def main():
    startTime = time.time()
    spotifyObj = Spotify(config.spotifyConfig["clientId"], config.spotifyConfig["clientSecret"])

    results = spotifyObj.getNewestTrackOrAlbum(config.artists["Illenium"])

    redditObj = Reddit(config.redditConfig["userAgent"], config.redditConfig["clientId"], config.redditConfig["clientSecret"], 
    config.redditConfig["username"], config.redditConfig["password"], config.subreddits[0])
    postResult = redditObj.createPost(results[0], results[1], results[3])
    endTime = time.time()

    print "Time: " + str(endTime - startTime)
    print "Fetched from Spotify! Song Info: " + results[0] + ", " + results[1] + ", " + results[2] + ", " + results[3]
    print "Posted to Reddit! Post Link: " + postResult


if __name__ == "__main__":
    main()
