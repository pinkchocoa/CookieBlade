## @file twitterDB.py
#
# @brief this file contains database access methods for twitter.
#
# @author JunHao
#
# @section libraries_main Libraries/Modules
# - database(local)
#   - access to database class.
# - itertools
#   - to flatten 2d list.
# - ast
#   - to convert string to dict type.
# - datetime
#   - to get today date.


#imports
from database import database
import itertools
import ast
import datetime

## Documentation for setTwitterGraphDB Method
# This method store data retive from crawler into the database.
def setTwitterGraphDB(tlink,*argument):
    """! save data from twitter crawl to database.
    @param tlink; twitter url or username
    @param *argument; rtData,favData,dateData
    """
    checkTableTwitterGraph(tlink) #check table integrity before working on it.
    db = database('twitter')
    uid = db.getUniqueID(tlink)
    db.createTable(uid,'Date','Rt','Fav')

    rtData = argument[0]
    favData = argument[1]
    dateData = argument[2]
    data = []
    for x in range(0,len(dateData)):
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
    for i in range(1,len(rtData)):
        rtData[i] = int(rtData[i])
    favData = db.getTableData(uid,'Fav')
    favData = list(itertools.chain(*favData))
    for i in range(1,len(favData)):
        favData[i] = int(favData[i])
    dateData.pop(0)
    return rtData,favData,dateData

##Documentation for checkTableTwitterGraph Method
# This method checks the table intergriy for twittergraph.
def checkTableTwitterGraph(tlink):
    """! Check table if faulty drop table.
    @param tlink; twitter url.
    """
    db = database('twitter')
    uid = db.getUniqueID(tlink)
    data = db.getTableData(uid,'*','ORDER BY ROWID ASC LIMIT 1')
    try:
        if (data[0][0]!='Date' or data[0][1]!='RT Count' or data[0][2]!='Like Count'):
            db.deleteTable(uid)
    except:
        db.deleteTable(uid)

## Documentation for setTwitterTrendDB Method
# This method store twitter trend in database.
def setTwitterTrendDB(trendData):
    """! store twitter trend in database by date.
    @param trendData; twitter trend data.
    """
    data = []
    data.append(str(datetime.date.today()))
    data.append(str(trendData))
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