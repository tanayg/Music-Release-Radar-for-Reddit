import praw

class Reddit:
    def __init__(self, userAgent, clientId, clientSecret, usernameArg, passwordArg, subredditName):
        self.bot = praw.Reddit(user_agent=userAgent, client_id=clientId, client_secret=clientSecret, username=usernameArg, password=passwordArg)
        self.subreddit = self.bot.subreddit(subredditName)

    def getSubredditDetails(self):
        return (self.subreddit.display_name, self.subreddit.title)


    def createPost(self, artistName, trackOrAlbumName, link):
        titleText = artistName + " - " + trackOrAlbumName
        response = self.subreddit.submit(title=titleText, url=link)
        return response.shortlink
        