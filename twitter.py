import tweepy #twitter api (https://docs.tweepy.org/) pip install tweepy
import apikey #api keys are stored here
from urllib.parse import urlparse
import json

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

    def trendingTopics(self):
        print(self.api.trends_available())

    def locTopics(self):
        topics = {} #create a dictionary to store name and tweet volume
        latSG = 1.3521
        lngSG = 103.8198
        loc =  self.api.trends_closest(latSG, lngSG)
        allTrends = self.api.trends_place(loc[0]['woeid'])
        trends = json.loads(json.dumps(allTrends, indent=1))
        for x in trends[0]["trends"]:
            topics[x["name"]] = x["tweet_volume"]

        return topics
        #need to parse...
        #return format of a single trend
        # {'trends': [{'name': '#UFC259', 'url': 'http://twitter.com/search?q=%23UFC259', 
        # 'promoted_content': None, 'query': '%23UFC259', 'tweet_volume': 408621}, {...} ]}
        # probably just want the name and tweet volume



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

#https://twitter.com/ + username
#able to parse url to grab the username behind for this class
#accepts both URL and tweetID
class TUser(Twitter):

    def __init__(self, username):
        super().__init__()
        self.username = username
        self.user = self.api.get_user(self.username)

    @classmethod
    def byID(cls, username):
        return cls(username)
    
    @classmethod
    def byURL(cls, URL):
        urlpath = urlparse(URL).path
        #path would be username/status/tweetid
        res = urlpath.split('/')
        username = res[1]
        return cls(username)

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

#https://twitter.com/twitter/statuses/ + tweetID
#able to parse url to grab the ID behind for this class
#accepts both URL and tweetID
class TTweet(Twitter):

    def __init__(self, tweetID):
        super().__init__()
        self.tweetID = tweetID
        self.tweet = self.api.get_status(self.tweetID)

    @classmethod
    def byID(cls, tweetID):
        return cls(tweetID)
    
    @classmethod
    def byURL(cls, URL):
        urlpath = urlparse(URL).path
        #path would be username/status/tweetid
        res = urlpath.split('/')
        tweetID = res[-1]
        return cls(tweetID)

    #gets the favourite count of a tweet
    def favCount(self):
        return self.tweet.favorite_count

    #gets the RT count of a tweet
    def RTCount(self):
        return self.tweet.retweet_count

    #get tweet location of a tweet
    def loc(self):
        return self.tweet.place

    #get tweet author
    #get what device is use to tweet this tweet