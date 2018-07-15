import config
import spotify

def main():
    results = spotify.getArtistData(config.artists["RL Grime"])
    print results["items"][0]["release_date"]


if __name__ == "__main__":
    main()
