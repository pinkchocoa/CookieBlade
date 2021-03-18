## @file twitterDB.py
#
# @brief this file contains database access methods for twitter.
#
# @section libraries_main Libraries/Modules
# - database(local)
#   - access to database class
# - itertools
#   - to flatten 2d list.


#imports
from database import database
import itertools

## Documentation for setTwitterGraphDB Method
# This method store data retive from crawler into the database.
def setTwitterGraphDB(tlink,*argument):
    """! save data from twitter crawl to database.
    @param tlink; twitter url or username
    @param *argument; rtData,favData,dateData
    """
    db = database('twitter')
    uid = db.getUniqueID(tlink)
    db.createTable(uid,"Date","Rt","Fav")

    rtData = argument[0]
    favData = argument[1]
    dateData = argument[2]

    for x in range(0,len(rtData)):
        data = []
        data.append(dateData[x])
        data.append(rtData[x])
        data.append(favData[x])
        db.insertTable(data,uid,'Date','Rt','Fav')

## Documentation for getTwitterGraphDB Method
# This method retrive twitter data from database.
def getTwitterGraphDB(tlink):
    """! retrive twitter related data from database.
    @param tlink; twitter URL or username
    @return rtData,favData,dateData;
    """
    db = database('twitter')
    uid = db.getUniqueID(tlink)
    dateData = db.getTableData(uid,'Date')
    dateData = list(itertools.chain(*dateData))
    dateData.reverse()
    rtData = db.getTableData(uid,'Rt')
    rtData = list(itertools.chain(*rtData))
    favData = db.getTableData(uid,'Fav')
    favData = list(itertools.chain(*favData))
    return rtData,favData,dateData