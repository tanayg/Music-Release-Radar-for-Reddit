import config
import time
import datetime
import requests
import sys
from spotify import *
from reddit import *

def main():
    if sys.argv[1] not in config.artists:
        sys.exit("Invalid artist name.")
    if "-o" in sys.argv:
        postNewMusic(sys.argv[1])
    while True:
        sleepUntil("59:30")
        postNewMusic(sys.argv[1])
    

def sleepUntil(checkTime):
    currTime = datetime.datetime.now().time().strftime('%M:%S')
    minDiff = int(checkTime[:2]) - int(currTime[:2])
    secDiff = int(checkTime[3:]) - int(currTime[3:])
    if (secDiff < 0):
        minDiff -= 1
        secDiff = 60 + secDiff
    if (minDiff < 0):
        minDiff = 60 + minDiff
    print "Sleeping for " + str(minDiff) + ":" + str(secDiff)
    time.sleep(minDiff * 60 + secDiff)
    print "Done sleeping!"


def postNewMusic(artist):
    spotifyObj = Spotify(config.spotifyConfig["clientId"], config.spotifyConfig["clientSecret"])
    print "Connected to Spotify API"

    redditObj = Reddit(config.redditConfig["userAgent"], config.redditConfig["clientId"], config.redditConfig["clientSecret"], 
    config.redditConfig["username"], config.redditConfig["password"], config.redditConfig["subreddit"])
    print "Connected to Reddit API. Logged in as " + config.redditConfig["username"] + ". Posting to r/" + config.redditConfig["subreddit"]


    startTime = time.time()

    i = 0
    results = spotifyObj.getNewestTrackOrAlbum(config.artists[artist])
    print "Last Release by " + artist + ": (" + results[2] + ") Today: (" + datetime.datetime.today().strftime('%Y-%m-%d') + ")"

    newTrackRelease = True

    while results[2] < datetime.datetime.today().strftime('%Y-%m-%d'):
        try:
            results = spotifyObj.getNewestTrackOrAlbum(config.artists[artist])
            currTime = datetime.datetime.now().time().strftime('%H:%M:%S')
            print "Call " + str(i) + ", Time: " + currTime
            i = i + 1
            if (time.time() - startTime) >= 60:
                newTrackRelease = False
                break
            time.sleep(1)
        except requests.exceptions.ConnectionError:
            print "Connection refused. Trying again"
            time.sleep(4)
            pass
    
    if "-o" not in sys.argv:
        sleepUntil("59:58")
    postResult = redditObj.createPost(results[0], results[1], results[3], "New")

    if newTrackRelease:
        print "Found new music on " + artist + "'s Spotify! Song Info: " + results[0] + ", " + results[1] + ", " + results[2] + ", " + results[3]
        print "Posted to Reddit! Post Link: " + postResult
        print "Exiting Program"
        exit()
    else:
        print "No new release from " + artist + " as of " + datetime.datetime.now().strftime('%m/%d/%Y %H:%M')


if __name__ == "__main__":
    main()
