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
    # by default it will search worldwide
    # mixed : include both popular and real time results in the response
    # recent : return only the most recent results in the response
    # popular : return only the most popular results in the response

    #return format: [ ['username', 'content', 'images if any'], [...] ]
    #e.g. 
    # ['RBW_MAMAMOO', '[#마마무]\n\n[Special] 2021 MAMAMOO\nFAN MEETING VCR Hidden Clip\n\n🔗 
    # https://t.co/FUfUnGE0K8\n\n#MAMAMOO #무무 #무무투어 https://t.co/psEmDli6nx', ['http://pbs.twimg.com/media/EveC0FwVoAQQSkf.jpg']]
    # https://twitter.com/RBW_MAMAMOO/status/1366704850671525890?s=20
    def searchKeyword(self, keyword, rType = "recent", getLoc = False, lat=1.3521, lng=103.8198):
        #recent tweets
        recentTweets = []
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
        ).items(10):
            images = []
            if 'media' in tweet.entities:
                for media in tweet.extended_entities['media']:
                    files_location = str(media['media_url'])
                    images.append(files_location)
            recentTweets.append([tweet.user.screen_name, tweet.full_text, images])
        
        print("returning trends for", place)

        #other information
        #tweet.user.screen_name
        #tweet.full_text
        #tweet.id
        #tweet.created_at
        #tweet.retweet_count
        #tweet.favorite_count

        return recentTweets

    #true for worldwide, otherwise false and give own location (lat and lng)
    #leave location blank for singapore

    #return format
    #{'#DontCallMe4thWin': 32031, 'JUNGKOOK': 1039162, ... }
    #{'topic that is trending': tweet volume, ...}
    def trendingTopics(self, worldWide, lat=1.3521, lng=103.8198):
        topics = {} #create a dictionary to store name and tweet volume

        if worldWide:
            loc =  self.api.trends_closest(lat, lng)
            place = loc[0]['name']
            loc = loc[0]['woeid']
        else:
            loc = 1
            place = "World Wide"

        allTrends = self.api.trends_place(loc)
        print("returning trends for", place)
        
        trends = json.loads(json.dumps(allTrends, indent=1))
        for x in trends[0]["trends"]:
            #might wanna remove the #?
            topics[x["name"]] = x["tweet_volume"]
        
        return topics
        #need to parse...
        #return format of a single trend
        # {'trends': [{'name': '#UFC259', 'url': 'http://twitter.com/search?q=%23UFC259', 
        # 'promoted_content': None, 'query': '%23UFC259', 'tweet_volume': 408621}, {...} ]}
        # probably just want the name and tweet volume

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

    #returns city, state
    def userLoc(self):
        return self.user.location

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