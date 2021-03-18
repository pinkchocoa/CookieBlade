## @file twitterGraph.py
#
# @brief this file uses the twitter class file classes and methods
#
# @section libraries_main Libraries/Modules
# - twitter (local)
#   - access to twitter classes and methods.


#imports
from twitter import Twitter, TUser, TTweet #contain class: Twitter(), Tuser(), TTweet() #twitter crawler.

## Documentation for twitterGraph Method
# This method return tweets stats in a list.
def twitterGraph(amount,URL_or_Username = ""):
    """! get details of tweets by user.
    @param amount; amount of tweet to retrieve.
    @param URL_or_Username; By url or username.
    @return rtList; Return list in the following format list = [[RTCountperDay] * last x days]
    @return likesList; Return list in the following format list = [[LikesperDay] * last x days]
    @return datelist; Return list of dates. with most recent to oldest date.
    """

    likesList = []
    rtList = []
    dateList = []
    RTcount = 0
    Likes = 0
    counter = 1

    if URL_or_Username == "":
        return 'Empty URL/UserName'
    elif "twitter" in URL_or_Username:
        tUser = TUser.byURL(URL_or_Username)
    else:
        tUser = TUser.byID(URL_or_Username)


    tweets = tUser.userTweets(1)
    tTweet = TTweet(tweets[0])
    date = str(tTweet.getDate())
    date = date.split(" ",1)[0] #split date and time.
    dateList.append(date)

    tweets = tUser.userTweets(amount)
    for x in tweets:
            tTweet = TTweet(x)
            date = str(tTweet.getDate())
            date = date.split(" ",1)[0] #split date and time.
            if date in dateList:
                RTcount = RTcount + tTweet.RTCount()
                Likes = Likes + tTweet.favCount()
                if counter == amount:
                    rtList.append(RTcount)
                    likesList.append(Likes)
                    dateList.pop()
                    return rtList,likesList,dateList
                counter = counter + 1

            else:
                dateList.append(date)
                rtList.append(RTcount)
                likesList.append(Likes)
                RTcount = tTweet.RTCount()
                Likes = tTweet.favCount()
                counter = counter + 1
    dateList.pop()
    return rtList,likesList,dateList
