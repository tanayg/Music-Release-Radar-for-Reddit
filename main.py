import config
import spotify

def main():
    albums = spotify.getArtistSongsAndAlbums(config.artists["RL Grime"])
    for album in albums:
        print "Name: " + album[0] + " | Release Date: " + album[1] + " | Link: " + album[2]


if __name__ == "__main__":
    main()
