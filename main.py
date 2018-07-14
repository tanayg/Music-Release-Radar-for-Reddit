import spotify

def main():
    results = spotify.getArtistData("RL Grime")
    print results


if __name__ == "__main__":
    main()
