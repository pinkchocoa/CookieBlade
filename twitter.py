import tweepy #twitter api (https://docs.tweepy.org/) pip install tweepy
import apikey #api keys are stored here

class Twitter:
    auth = tweepy.OAuthHandler(apikey.T_CONSUMER_KEY, apikey.T_CONSUMER_SECRET)
    auth.set_access_token(apikey.T_ACCESS_TOKEN, apikey.T_ACCESS_SECRET)
    api = tweepy.API(auth)

    def __init__(self):
        pass

    def printHomePage(self):
        public_tweets = self.api.home_timeline()
        for tweet in public_tweets:
            print(tweet.text)

    def followCount(self, username):
        pass

    def likeCount(self, username):
        pass

    
    