## @file youtubeGraph.py
#
# @brief this file contains retrival of youtube related information
#
# @section libraries_main Libraries/Modules
# - database(local)
#   - access to database class
# - datetime
#   - to get today date
# - itertools
#   - to flatten 2d list.

#imports
from youtube import *
from database import database
import datetime
import itertools

## Documentation for setYoutubeChannelStats Method
# This method store data retrive from crawler into the database.
def setYoutubeChannelStats(channelUrl):
    """! Get youtube channel information and save to database
    @param channelUrl;
    """
    youtube = Channel()
    data = []
    data.append(str(datetime.date.today()))
    temp = youtube.searchurl(channelUrl)
    for i in range(len(temp)):
        data.append(temp[i])
    db = database('youtube')
    uid = db.getUniqueID(channelUrl)
    db.createTable(uid,'date','created','Vidcount','Subcount','Totalview')
    db.insertTable(data,uid,'date','created','Vidcount','Subcount','Totalview')

## Documentation for getYoutubeChannelStats Method
# This method retrive data the database.
def getYoutubeChannelStats(channelUrl):
    """! Get youtube channel information from database
    @param channelUrl;
    @return data; youtube channel stats. Date created, Vidcount, Subcount, TotalViews
    """
    db = database('youtube')
    uid = db.getUniqueID(channelUrl)
    data = db.getTableData(uid)
    data = data[len(data)-1]
    data.pop(0)
    return data #return latest channel stats.

##Documentation for getYoutubeTrends Method
# This method fetch youtube trend views in each trending category
def getYoutubeTrends(countryCode = "SG"):
    """! Get trending category information
    @param countryCode; Default SG. Supports MY and PH as well
    @return trendData; List type:[('totalmusicviews', #), ('totalsportsviews', #), ('totalgamesviews', #), ('totalnewsviews', #)]
    """
    youtube = youtubeVid()
    youtube.getTrendingVideo()
    trendData = youtube.getDBvids(countryCode)
    return trendData

##Documenetation for setRevenueData Method
# This method fetch the latest 12 months revenue data from a channel and save it to the database.
def setRevenueData(channelUrl):
    """!  Get channel past 12 months revenue data and save to the database.
    @param channelUrl;
    """
    data = []
    data.append(str(datetime.date.today()))
    db = database("youtubeRevenue")
    uid = db.getUniqueID(channelUrl)
    db.createTable(uid,'Date','jan','feb','mar','apr','may','jun','jul','aug','sep','oct','nov','dec')
    youtube = Channel()
    result = youtube.getRevenueData(channelUrl)
    result.pop(0) #get rid of amount of videos in said months.
    result = list(itertools.chain(*result)) #convert to 1d list
    for i in range(0,len(result)):
        data.append(result[i][1])
    db.insertTable(data,uid,'Date','jan','feb','mar','apr','may','jun','jul','aug','sep','oct','nov','dec')

##Documenetation for getRevenueData Method
# This method fetch the latest 12 months revenue data for a channel from the database.
def getRevenueData(channelUrl):
    """! Get channel most recently crawled past 12 months revenue data
    @param channelUrl;
    @return result; where ["Data",int janValue,...,int decValue]
    """
    db = database("youtubeRevenue")
    uid = db.getUniqueID(channelUrl)
    data = db.getTableData(uid)
    print(len(data))
    if len(data) > 1:
        data= data.pop()
    else:
        data = list(itertools.chain(*data)) #convert to 1d list
    print(data)
    result = []
    result.append(data[0])
    for i in range(1,len(data)):
        result.append(int(float(data[i])))
    print(result)
    return result

getRevenueData("https://www.youtube.com/channel/UCR1IuLEqb6UEA_zQ81kwXfg")