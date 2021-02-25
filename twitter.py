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

#TREND FUNCTIONS
#get trending topics
#get trending topics by location

#ENGAGEMENT FUNCTIONS
#get user most fav tweet
#get user most engaged tweet
#get user most engaged friend
#get user most engaged follower
#get user most engaged topics

    
class TUser(Twitter):

    def __init__(self, username):
        super().__init__()
        self.username = username
        self.user = self.api.get_user(self.username)

    #gets user's current follow count
    def followCount(self):
        return self.user.followers_count

    #gets user's current tweet count
    def tweetCount(self):
        return self.user.statuses_count

    def userLoc(self):
        return self.user.location

    #gets user's recent followers
    def recentFollows(self):
        pass

    def recentFriends(self):
        pass

    #get user's favourite tweets
    def userFav(self):
        fav=[]
        for tweet in tweepy.Cursor(self.api.favorites, id=self.username, 
            lang="en", wait_on_rate_limit=True,
            tweet_mode="extended").items(10):
            images = []
            if 'media' in tweet.entities:
                for media in tweet.extended_entities['media']:
                    files_location = str(media['media_url'])
                    images.append(files_location)
            fav.append([tweet.user.screen_name, tweet.full_text, images])

        return fav

class TTweet(Twitter):

    def __init__(self, tweetID):
        super().__init__()
        self.tweetID = tweetID
        self.tweet = self.api.get_status(self.tweetID)

    #gets the favourite count of a tweet
    def favCount(self):
        return self.tweet.favorite_count

    #gets the RT count of a tweet
    def RTCount(self):
        return self.tweet.retweet_count

    #get tweet location of a tweet
    def loc(self):
        return self.tweet.place