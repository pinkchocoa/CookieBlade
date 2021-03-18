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
from database import database #contain database class and its methods
import itertools #contain itertools method like chain.
import ast #contain method to convert str to dict
import datetime

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

## Documentation for setTwitterTrendDB Method
# This method store twitter trend in database.
def setTwitterTrendDB(trendData):
    """! store twitter trend in database by date.
    @param trendData; twitter trend data.
    """
    data = []
    data.append(str(datetime.date.today()))
    data.append(str(trenddata))
    db = database('twitter')
    db.createTable('trends','date','dict')
    db.insertTable(list(data),'trends','date','dict')

## Documentation for getTwitterTrendDB Method
# This method retrive twitter trend data from database.
def getTwitterTrendDB():
    """! retrive twitter trend data from database.
    @return data; return trend data as a dictionary.
    """
    db = database('twitter')
    strArg = "WHERE date = " + str(datetime.date.today())
    data = db.getTableData('trends','dict',strArg)
    data = ast.literal_eval(data[0][0]) #convert str to dict
    return data