## @file twitter.py
#
# @brief this file uses the twitter API to retrieve wanted data
#
# @section libraries_main Libraries/Modules
# - tweepy (https://docs.tweepy.org/)
#   - access to twitter API
# - apikey (local)
#   - this file contains the twitter api token/key
# - urllib.parse
#   - access to urllib.parse to parse certain urls
# - json
#   - access to json loads and dump to convert from JSON string to python dictionary 

# Imports
import tweepy #twitter api (https://docs.tweepy.org/) pip install tweepy
import apikey #api keys are stored here
from urllib.parse import urlparse
import json

## Documentation for Twitter Class
# The twitter class instantiate connection with the twitter API
# this allows us to make use of the different functions available in twitter API
class Twitter:
    """! Twitter class
    Defines the base twitter object that does the authentication and instantiation to the twitter API
    """

    # static variables
    CONSUMER_KEY = apikey.T_CONSUMER_KEY
    CONSUMER_SECRET = apikey.T_CONSUMER_SECRET
    ACCESS_TOKEN = apikey.T_ACCESS_TOKEN
    ACCESS_SECRET = apikey.T_ACCESS_SECRET
    api = ""

    def __init__(self):
        """! Twitter class initializer
        @return an instance of Twitter class that connects to the twitter API
        """
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
    # by default it will search worldwide
    # mixed : include both popular and real time results in the response
    # recent : return only the most recent results in the response
    # popular : return only the most popular results in the response

    #return format: [ ['username', 'content', 'images if any'], [...] ]
    #e.g. 
    # ['RBW_MAMAMOO', '[#마마무]\n\n[Special] 2021 MAMAMOO\nFAN MEETING VCR Hidden Clip\n\n🔗 
    # https://t.co/FUfUnGE0K8\n\n#MAMAMOO #무무 #무무투어 https://t.co/psEmDli6nx', ['http://pbs.twimg.com/media/EveC0FwVoAQQSkf.jpg']]
    # https://twitter.com/RBW_MAMAMOO/status/1366704850671525890?s=20
    def searchKeyword(self, keyword, rType = "recent", amt = 3, getLoc = False, lat=1.3521, lng=103.8198):
        """! searches through twitter and returns a list of twitters following the filtered parameters
        @param self instance of the object that we are calling from
        @param keyword what to search for
        @param rType results type
                "mixed" will include both popular and recent results
                "recent" will include recent tweets 
                "popular" will include popular tweets
        @param getLoc False for worldwide results, True for specified location
        @param lat lattitude, default value set to singapore's. not in use for worldwide results
        @param lng longtitude, default value set to singapore's. not in use for worldwide results
        @return a list of tweets in the format of  [ ['username', 'content', 'images if any'], [...] ]
        """
        print("searching " + keyword)
        searchedTweets = []
        if getLoc:
            loc =  self.api.trends_closest(lat, lng)
            place = loc[0]['name']
            #200km radius of specified location
            loc = str(lat) + "," + str(lng) + ",700km"
            #print("test", loc)
        else:
            loc = ""
            place = "World Wide"

        for tweet in tweepy.Cursor(
            self.api.search,
            q=keyword + " -filter:retweets",
            geocode = loc, lang="en",
            result_type = rType,
            wait_on_rate_limit=True,
            tweet_mode="extended"
        ).items(amt):
            images = []
            if 'media' in tweet.entities:
                for media in tweet.extended_entities['media']:
                    files_location = str(media['media_url'])
                    images.append(files_location)
            searchedTweets.append([tweet.user.screen_name, tweet.full_text, tweet.id, images])
        
        print("returning trends for", place)

        #other information
        #tweet.user.screen_name
        #tweet.full_text
        #tweet.id
        #tweet.created_at
        #tweet.retweet_count
        #tweet.favorite_count

        return searchedTweets

    #true for worldwide, otherwise false and give own location (lat and lng)
    #leave location blank for singapore

    #return format
    #{'#DontCallMe4thWin': 32031, 'JUNGKOOK': 1039162, ... }
    #{'topic that is trending': tweet volume, ...}
    def trendingTopics(self, worldWide = True, lat=1.3521, lng=103.8198, limit=5):
        """! searches through twitter for trending topics
        @param self instance of the object that we are calling from
        @param worldWide True to search worldwide, False to search by location
        @param lat lattitude, default value set to singapore's. not in use for worldwide results
        @param lng longtitude, default value set to singapore's. not in use for worldwide results
        @return a dictionary of trending topics in the format of {'topic that is trending': tweet volume, ...}
        """
        topics = {} #create a dictionary to store name and tweet volume

        if not worldWide:
            loc =  self.api.trends_closest(lat, lng)
            place = loc[0]['name']
            loc = loc[0]['woeid']
        else:
            loc = 1
            place = "World Wide"

        allTrends = self.api.trends_place(loc)
        print("returning trends for", place)
        
        trends = json.loads(json.dumps(allTrends, indent=1))
        for idx, x in enumerate(trends[0]["trends"]):
            if x["tweet_volume"]:
                topics[x["name"]] = x["tweet_volume"]
            if idx == limit:
                break
        
        return topics

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
    """! TUser class
    This class inherits the base Twitter class for API access.
    This class contains methods specifically related to a twitter user
    """

    def __init__(self, username):
        """! TUser class initializer
        @param username username of the twitter account to fetch data of
        @return an instance of TUser class
        """
        super().__init__()
        self.username = username
        self.user = self.api.get_user(self.username)

    @classmethod
    def byID(cls, username):
        """! class method that creates a TUser instance with username
        @param username username of the twitter account to fetch data of
        @return an instance of TUser class
        """
        return cls(username)
    
    @classmethod
    def byURL(cls, URL):
        """! class method that creates a TUser instance with a profile url
        @param url profile url of the twitter account to fetch data of
        @return an instance of TUser class
        """
        urlpath = urlparse(URL).path
        #path would be username/status/tweetid
        res = urlpath.split('/')
        username = res[1]
        return cls(username)

    #gets user's current follow count
    def followCount(self):
        """! gets user's current follow count
        @param self instance of the object that we are calling from
        @return user's follow count (integer)
        """
        return self.user.followers_count

    #gets user's current tweet count
    def tweetCount(self):
        """! gets user's current tweet count
        @param self instance of the object that we are calling from
        @return user's tweet count (integer)
        """
        return self.user.statuses_count

    def favTweetCount(self):
        return self.user.favourites_count
        
    #returns city, state
    def userLoc(self):
        """! gets user's location (that is set on their profile)
        @param self instance of the object that we are calling from
        @return user's location, in the format of "city, state" (should be a string)
        """
        return self.user.location

    def userCreatedAt(self):
        return self.user.created_at

    #gets user's recent followers
    def recentFollows(self):
        pass

    def recentFriends(self):
        pass

    #get user's favourite tweets
    #return format: [ ['username', 'content', 'images if any'], [...] ]
    #e.g. 
    # ['RBW_MAMAMOO', '[#마마무]\n\n[Special] 2021 MAMAMOO\nFAN MEETING VCR Hidden Clip\n\n🔗 
    # https://t.co/FUfUnGE0K8\n\n#MAMAMOO #무무 #무무투어 https://t.co/psEmDli6nx', ['http://pbs.twimg.com/media/EveC0FwVoAQQSkf.jpg']]
    # https://twitter.com/RBW_MAMAMOO/status/1366704850671525890?s=20
    def userFav(self):
        """! get user's favourite tweets
        @param self instance of the object that we are calling from
        @return returns a list of tweets that the user have favourite/liked in the format of [ ['username', 'content', 'images if any'], [...] ]
        """
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

    def userTweets(self, num=100,startDate="2020-01-01", endDate="2021-01-01"):
        """! get user's tweets
        @param self instance of the object that we are calling from
        @return returns a list of tweets that the user have tweeted [ ['username', 'content', 'images if any'], [...] ]
        """
        tweets=[]
        for tweet in tweepy.Cursor(self.api.user_timeline, 
            q=" -filter:retweets",
            Since=startDate,
            Until=endDate,
            id=self.username, 
            lang="en", wait_on_rate_limit=True,
            tweet_mode="extended").items(num):
            images = []
            if 'media' in tweet.entities:
                for media in tweet.extended_entities['media']:
                    files_location = str(media['media_url'])
                    images.append(files_location)
            date = str(tweet.created_at)
            date = date.split(" ",1)[0]
            tweets.append([tweet.id, date, tweet.favorite_count, tweet.retweet_count])

        return tweets

#https://twitter.com/twitter/statuses/ + tweetID
#able to parse url to grab the ID behind for this class
#accepts both URL and tweetID
class TTweet(Twitter):
    """! TTweet Class
    This class inherits the base Twitter class for API access.
    This class contains methods specifically related to a tweet
    """

    def __init__(self, tweetID):
        """! TTweet class initializer
        @param tweetID tweet ID of the tweet to fetch data of
        @return an instance of TTweet class
        """
        super().__init__()
        self.tweetID = tweetID
        self.tweet = self.api.get_status(self.tweetID)

    @classmethod
    def byID(cls, tweetID):
        """! class method that creates a TTweet instance with username
        @param tweetID tweet ID of the tweet to fetch data of
        @return an instance of TTweet class
        """
        return cls(tweetID)
    
    @classmethod
    def byURL(cls, URL):
        """! class method that creates a TTweet instance with a tweet url
        @param url tweet url of the tweet to fetch data of
        @return an instance of TTweet class
        """
        urlpath = urlparse(URL).path
        #path would be username/status/tweetid
        res = urlpath.split('/')
        tweetID = res[-1]
        return cls(tweetID)

    #gets the favourite count of a tweet
    def favCount(self):
        """! gets the favourite count of a tweet
        @param self instance of the object that we are calling from
        @return favourite count of a tweet (integer)
        """
        return self.tweet.favorite_count

    #gets the RT count of a tweet
    def RTCount(self):
        """! gets the RT count of a tweet
        @param self instance of the object that we are calling from
        @return RT count of a tweet (integer)
        """
        return self.tweet.retweet_count

    #get tweet location of a tweet
    def loc(self):
        """! get tweet location of a tweet (if available)
        @param self instance of the object that we are calling from
        @return tweet location of a tweet, in the format of "city, state" (should be a string)
        """
        return self.tweet.place

    def getDate(self):
        return self.tweet.created_at

    #get tweet author
    #get what device is use to tweet this tweet
