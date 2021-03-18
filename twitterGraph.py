## @file twitterGraph.py
#
# @brief this file uses the twitter class file classes and methods
#
# @section libraries_main Libraries/Modules
# - twitter (local)
#   - access to twitter classes and methods.
# - twitterDB(local)
#   - access to twitterDB methods.
# - UrlExtraction
#   - UrlExtraction methods


#imports
from twitter import Twitter, TUser, TTweet  #contain class: Twitter(), Tuser(), TTweet() #twitter crawler.
import twitterDB                            #contains methods of twitterDB
from UrlExtraction import UrlExtraction

## Documentation for twitterGraph Method
# This method saves tweets stats in database.
def twitterGraph(amount,URL_or_Username = ""):
    """! get details of tweets by user.
    @param amount; amount of tweet to retrieve.
    @param URL_or_Username; By url or username.
    """

    likesList = ["Like Count"]
    rtList = ["RT Count"]
    dateList = []
    tweety = []
    RTcount = 0
    Likes = 0
    counter = 1

    if URL_or_Username == "":
        return 'Empty URL/UserName'
    elif "twitter" in URL_or_Username:
        u = UrlExtraction()
        uid = u.getUniqueID(URL_or_Username)
        tUser = TUser.byID(uid)
    else:
        tUser = TUser.byID(URL_or_Username)


    tweets = tUser.userTweets(1)
    tweets = tweets[0][0]
    tTweet = TTweet(tweets)
    date = str(tTweet.getDate())
    date = date.split(" ",1)[0] #split date and time.
    dateList.append(date)

    tweets = tUser.userTweets(amount)
    for i in range(len(tweets)):
        tweety.append(tweets[i][0])

    for x in tweety:
            tTweet = TTweet(x)
            date = str(tTweet.getDate())
            date = date.split(" ",1)[0] #split date and time.
            if date in dateList:
                RTcount = RTcount + tTweet.RTCount()
                Likes = Likes + tTweet.favCount()
                if counter == amount:
                    rtList.append(RTcount)
                    likesList.append(Likes)
                    if len(dateList) >1:
                        #dateList.pop()
                        break
                counter = counter + 1

            else:
                dateList.append(date)
                rtList.append(RTcount)
                likesList.append(Likes)
                RTcount = tTweet.RTCount()
                Likes = tTweet.favCount()
                counter = counter + 1
    if len(dateList) > 1:
        pass
        #dateList.pop()
    twitterDB.setTwitterGraphDB(URL_or_Username,rtList,likesList,dateList)

## Documentation for twitterTrend Method
#This method saves twitter trends in database
def twitterTrend():
    """! Get Trending topics and save to database.
    """
    data = []
    t = Twitter()
    data = t.trendingTopics()
    twitterDB.setTwitterTrendDB(data)