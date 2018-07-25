import config
import time
import datetime
import requests
from spotify import *
from reddit import *

def main():
    #sleepUntil("59:25")
    job()

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
    print "I'm awake boiiii"


def job():
    artist = "Kasbo"
    print "Looking for new music by " + artist + "!"

    spotifyObj = Spotify(config.spotifyConfig["clientId"], config.spotifyConfig["clientSecret"])

    redditObj = Reddit(config.redditConfig["userAgent"], config.redditConfig["clientId"], config.redditConfig["clientSecret"], 
    config.redditConfig["username"], config.redditConfig["password"], config.subreddits[1])


    startTime = time.time()

    i = 0
    results = spotifyObj.getNewestTrackOrAlbum(config.artists[artist])
    print "Last Release: (" + results[2] + ") Today: (" + datetime.datetime.today().strftime('%Y-%m-%d') + ")"

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
    #postResult = redditObj.createPost(results[0], results[1], results[3])

    if newTrackRelease:
        print "Fetched from Spotify! Song Info: " + results[0] + ", " + results[1] + ", " + results[2] + ", " + results[3]
        #print "Posted to Reddit! Post Link: " + postResult
    else:
        print "No new release from " + artist + " :("


if __name__ == "__main__":
    main()
