from youtube import *
from database import database

def setYoutubeChannelStats(channelUrl):
    data = getChannelStats(channelUrl)
    db = database('youtube')
    uid = db.getUniqueID(channelUrl)
    db.createTable(uid,'date','Vidcount','Subcount','Totalview')
    db.insertTable(data,uid,'date','Vidcount','Subcount','Totalview')

def getYoutubeChannelStats(channel):
    pass
