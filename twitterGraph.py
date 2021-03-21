## @file twitterGraph.py
#
# @brief this file uses the twitter class file classes and methods
#
# @author JunHao (20%)
# @author Jodie(80%)
#
# @section libraries_main Libraries/Modules
# - twitter (local)
#   - access to twitter classes and methods.
# - twitterDB(local)
#   - access to twitterDB methods.
# - UrlExtraction
#   - UrlExtraction methods
# - time
#   - check runing time for functions


#imports
from twitter import Twitter, TUser, TTweet  #contain class: Twitter(), Tuser(), TTweet() #twitter crawler.
import twitterDB                            #contains methods of twitterDB
from UrlExtraction import UrlExtraction
import time

## Documentation for twitterGraph Method
# This method saves tweets stats in database.
def twitterGraph(amount,URL_or_Username=""):
    """! get details of tweets by user.
    @param amount; amount of tweet to retrieve.
    @param URL_or_Username; By url or username.
    """
    start_time = time.time()
    likesList = ["Like Count"]
    rtList = ["RT Count"]
    dateList = ["Date"]
    RTcount = 0
    Likes = 0
    amount =10
    counter = 1
    if "twitter" in URL_or_Username:
        tUser = TUser.byURL(URL_or_Username)
    else:
        tUser = TUser.byID(URL_or_Username)

    tweets = tUser.userTweets(amount)
    for x in tweets:
        tid = x[0]
        date = x[1]
        fav = x[2]
        rt = x[3]
        if date in dateList:
            RTcount = RTcount + rt
            Likes = Likes + fav
            if counter == amount:
                rtList.append(RTcount)
                likesList.append(Likes)
                break
            counter = counter + 1

        else:
            dateList.append(date)
            rtList.append(RTcount)
            likesList.append(Likes)
            RTcount = rt
            Likes = fav
            counter = counter + 1

    if len(dateList)>1:
        dateList.pop()
    twitterDB.setTwitterGraphDB(URL_or_Username,rtList,likesList,dateList)
    print("--- %s seconds ---" % (time.time() - start_time))

## Documentation for twitterTrend Method
#This method saves twitter trends in database
def twitterTrend():
    """! Get Trending topics and save to database.
    """
    data = []
    t = Twitter()
    data = t.trendingTopics()
    twitterDB.setTwitterTrendDB(data)