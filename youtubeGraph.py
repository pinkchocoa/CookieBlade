## @file youtubeGraph.py
#
# @brief this file contains retrival of youtube related information
#
# @section libraries_main Libraries/Modules
# - database(local)
#   - access to database class
# - itertools
#   - to flatten 2d list.
# - datetime
#   - to get today date

#imports
from youtube import *
from database import database
import datetime

## Documentation for setYoutubeChannelStats Method
# This method store data retive from crawler into the database.
def setYoutubeChannelStats(channelUrl):
    """! Get youtube channel information and save to database
    @param channelUrl;
    """
    data = []
    data.append(str(datetime.date.today()))
    temp = getChannelStats(channelUrl)
    for i in range(len(temp)):
        data.append(temp[i])
    db = database('youtube')
    uid = db.getUniqueID(channelUrl)
    db.createTable(uid,'date','created','Vidcount','Subcount','Totalview')
    db.insertTable(data,uid,'date','created','Vidcount','Subcount','Totalview')

## Documentation for getYoutubeChannelStats Method
# This method retive data the database.
def getYoutubeChannelStats(channelUrl):
    """! Get youtube channel information from database
    @param channelUrl;
    @return data; youtube channel stats
    """
    db = database('youtube')
    uid = db.getUniqueID(channelUrl)
    data = db.getTableData(uid)
    print("test")
    print(data)
    return data[len(data)-1] #return latest channel stats.

def setYoutubeChannelRevenue(channelUrl):
    pass

def getYoutubeChannelRevenue(channelUrl):
    pass