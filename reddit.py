import praw

class Reddit:
    def __init__(self, userAgent, clientId, clientSecret, usernameArg, passwordArg, subredditName):
        self.bot = praw.Reddit(user_agent=userAgent, client_id=clientId, client_secret=clientSecret, username=usernameArg, password=passwordArg)
        self.subreddit = self.bot.subreddit(subredditName)