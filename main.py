import config
import spotify

def main():
    results = spotify.getArtistData(config.artists["RL Grime"])
    for item in results["items"]:
        print "Name: " + item["name"] + ", Release Date: " + item["release_date"]


if __name__ == "__main__":
    main()
