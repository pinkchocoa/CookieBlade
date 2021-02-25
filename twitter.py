import tweepy #twitter api (https://docs.tweepy.org/) pip install tweepy
import apikey #api keys are stored here

class Twitter:
    CONSUMER_KEY = apikey.T_CONSUMER_KEY
    CONSUMER_SECRET = apikey.T_CONSUMER_SECRET
    ACCESS_TOKEN = apikey.T_ACCESS_TOKEN
    ACCESS_SECRET = apikey.T_ACCESS_SECRET
    api = ""

    def __init__(self):
        auth = tweepy.OAuthHandler(self.CONSUMER_KEY, self.CONSUMER_SECRET)
        auth.set_access_token(self.ACCESS_TOKEN, self.ACCESS_SECRET)
        self.api = tweepy.API(auth)

        try:
            self.api.verify_credentials()
        except Exception as e:
            logger.error("Error creating API", exc_info=True)
            raise e
            logger.info("API created")

    def printHomePage(self, username):
        public_tweets = self.api.home_timeline(username)
        for tweet in public_tweets:
            print(tweet.text)

    def followCount(self, username):
        user = self.api.get_user(username)
        return user.followers_count
        # followers = []
        # for page in tweepy.Cursor(self.api.followers, screen_name=username, wait_on_rate_limit=True,count=200).pages():
        #     try:
        #         followers.extend(page)
        #     except tweepy.TweepError as e:
        #         print("Going to sleep:", e)
        #         time.sleep(60)
        # return len(followers)

    def likeCount(self, username):
        pass

    
    