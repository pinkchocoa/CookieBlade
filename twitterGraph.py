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
    @return mainlist; Return list in the following format list = [[RTCountperDay,LikesperDay] * last 7 days]
    @return datelist; Return list of dates. with most recent to oldest date.
    """

    mainlist = []
    nestlist = []
    datelist = []
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
    datelist.append(date)

    tweets = tUser.userTweets(amount)
    for x in tweets:
            tTweet = TTweet(x)
            date = str(tTweet.getDate())
            date = date.split(" ",1)[0] #split date and time.
            if date in datelist:
                RTcount = RTcount + tTweet.RTCount()
                Likes = Likes + tTweet.favCount()
                if counter == amount:
                    nestlist.append(RTcount)
                    nestlist.append(Likes)
                    mainlist.append(nestlist)
                    nestlist = []
                    return mainlist, datelist
                counter = counter + 1

            else:
                datelist.append(date)
                nestlist.append(RTcount)
                nestlist.append(Likes)
                mainlist.append(nestlist)
                nestlist = []
                RTcount = tTweet.RTCount()
                Likes = tTweet.favCount()
                counter = counter + 1
    return mainlist, datelist


#Example:      
data1,data2= twitterGraph(10,"BarackObama")
print(data1)
print(data2)