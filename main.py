import config
import time
import datetime
import requests
from spotify import *
from reddit import *

def main():
    #Setup
    artist = "RL Grime"

    spotifyObj = Spotify(config.spotifyConfig["clientId"], config.spotifyConfig["clientSecret"])

    redditObj = Reddit(config.redditConfig["userAgent"], config.redditConfig["clientId"], config.redditConfig["clientSecret"], 
    config.redditConfig["username"], config.redditConfig["password"], config.subreddits[1])


    startTime = time.time()

    i = 0
    results = spotifyObj.getNewestTrackOrAlbum(config.artists[artist])
    print "Last Release: (" + results[2] + ") Today: (" + datetime.datetime.today().strftime('%Y-%m-%d') + ")"
    while results[2] < datetime.datetime.today().strftime('%Y-%m-%d'):
        try:
            results = spotifyObj.getNewestTrackOrAlbum(config.artists[artist])
            print "Call " + str(i) + ", Time: " + datetime.datetime.now().time().strftime('%H:%M:%S')
            i = i + 1
            time.sleep(1)
        except requests.exceptions.ConnectionError:
            print "Connection refused. Trying again"
            time.sleep(4)
            pass
    postResult = redditObj.createPost(results[0], results[1], results[3])

    endTime = time.time()

    print "Time: " + str(endTime - startTime)
    print "Fetched from Spotify! Song Info: " + results[0] + ", " + results[1] + ", " + results[2] + ", " + results[3]
    print "Posted to Reddit! Post Link: " + postResult


if __name__ == "__main__":
    main()
