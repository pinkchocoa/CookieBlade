import tweepy #twitter api
import apikey #api keys are stored here

auth = tweepy.OAuthHandler(apikey.T_CONSUMER_KEY, apikey.T_CONSUMER_SECRET)
auth.set_access_token(apikey.T_ACCESS_TOKEN, apikey.T_ACCESS_SECRET)

api = tweepy.API(auth)

public_tweets = api.home_timeline()
for tweet in public_tweets:
    print(tweet.text)