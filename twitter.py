import tweepy #twitter api (https://docs.tweepy.org/) pip install tweepy
import apikey #api keys are stored here
from datetime import datetime, timedelta

class Twitter:
    CONSUMER_KEY = apikey.T_CONSUMER_KEY
    CONSUMER_SECRET = apikey.T_CONSUMER_SECRET
    ACCESS_TOKEN = apikey.T_ACCESS_TOKEN
    ACCESS_SECRET = apikey.T_ACCESS_SECRET
    api = ""

    def __init__(self):
        auth = tweepy.OAuthHandler(self.CONSUMER_KEY, self.CONSUMER_SECRET)
        auth.set_access_token(self.ACCESS_TOKEN, self.ACCESS_SECRET)
        self.api = tweepy.API(auth, wait_on_rate_limit=True)

        try:
            self.api.verify_credentials()
        except Exception as e:
            logger.error("Error creating API", exc_info=True)
            raise e
            logger.info("API created")

#USER FUNCTIONS
    #gets user's current follow count
    def followCount(self, username):
        user = self.api.get_user(username)
        return user.followers_count

    #gets user's current tweet count
    def tweetCount(self, username):
        user = self.api.get_user(username)
        return user.statuses_count

    #gets user's recent followers
    def recentFollows(self, username):
        pass

    def recentFriends(self, username):
        pass

    #get user's favourite tweets
    def userFav(self, username):
        fav=[]
        for tweet in tweepy.Cursor(self.api.favorites, id=username, 
            lang="en", wait_on_rate_limit=True,
            tweet_mode="extended").items(10):
            images = []
            if 'media' in tweet.entities:
                for media in tweet.extended_entities['media']:
                    files_location = str(media['media_url'])
                    images.append(files_location)
            fav.append([tweet.user.screen_name, tweet.full_text, images])

        return fav

#TWEET FUNCTIONS
    #gets the favourite count of a tweet
    def tweetFavCount(self, tweetID):
        tweet = self.api.get_status(tweetID)
        return tweet.favourite_count

    #gets the RT count of a tweet
    def tweetRTCount(self, tweetID):
        tweet = self.api.get_status(tweetID)
        return tweet.retweet_count

    #get tweet location of a tweet
    def tweetLoc(self, tweetID):
        return self.api.geo_id(tweetID)

#SEARCH FUNCTIONS
    def searchKeyword(self, keyword):
        #recent tweets
        recentTweets = []
        for tweet in tweepy.Cursor(
            self.api.search,
            q=keyword + " -filter:retweets",
            lang="en", wait_on_rate_limit=True,
            tweet_mode="extended"
        ).items(10):
            images = []
            if 'media' in tweet.entities:
                for media in tweet.extended_entities['media']:
                    files_location = str(media['media_url'])
                    images.append(files_location)
            recentTweets.append([tweet.user.screen_name, tweet.full_text, images])
        
        #other information
        #tweet.user.screen_name
        #tweet.full_text
        #tweet.id
        #tweet.created_at
        #tweet.retweet_count
        #tweet.favorite_count

        return recentTweets



    def searchLocation(self, location):
        pass

    def searchLocKeyword(self, location, keyword):
        pass

    
    