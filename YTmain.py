from YTfile import *
from youtube import *
from database import *


def main():
    boot()
    getTrendingVideo()

def boot():
    create_folder_dir('1009Project')
    create_data_files('1009Project')

#Get trending video #return dictionary of video info
def getTrendingVideo():
    tuser = database('TrendVideo')  # DB name must be given to start.
    tuser.createTable('TrendVideo', 'key', 'C1', 'C2', 'C3', 'C4', 'C5', 'C6', 'C7', 'C8', 'C9', 'C10')

    tuser1 = database('TrendChannel')  # DB name must be given to start.
    tuser1.createTable('TrendChannel', 'key', 'C1', 'C2', 'C3', 'C4', 'C5', 'C6', 'C7', 'C8')

    reply = scrapData()
    path = '1009Project' + '/crawled.txt'
    for i in range(0, len(reply)):
        reply[i] = vidInfo(reply[i])
        TrendVidsInfo = reply[i].getDict()
        TrendVidsInfoList = [(v) for k, v in TrendVidsInfo.items()]
        TrendVidsInfoList.insert(0, i)
        tuser.insertTable(TrendVidsInfoList, 'TrendVideo', 'key', 'C1', 'C2', 'C3', 'C4', 'C5', 'C6', 'C7', 'C8', 'C9', 'C10')

        # VidChannelInfo = channel.getChannelDetail(TrendVidsInfo)
        # for j in range(0, len(VidChannelInfo)):
        #     VidChannelInfo[j] = channel.getChannelStat(VidChannelInfo[j])
        #     # VidChannelInfo[j] = channel.getChannelVid(VidChannelInfo[j])
        #     VidChannelInfo = VidChannelInfo[j].channelDetail()
        #     VidChannelInfo = [(v) for k, v in VidChannelInfo.items()]
        #     VidChannelInfo.insert(0, i)
        #     tuser1.insertTable(VidChannelInfo, 'TrendChannel', 'key', 'C1', 'C2', 'C3', 'C4', 'C5', 'C6', 'C7', 'C8')



#HOW TO USE FOR NOW
#########################################################################################################

#For this to run, you need the other file youtube.py
#To use the functions elsewhere, just import everything that's in this file
#To test if there's data in the database, install DB Browser (SQLite) to check

#Functions to usable:
#searchurl returns back a list of subs, totalviewno, totalvidno and created-at-date from a channel
#getRevenueData returns back a list of videos made by a channel sorted by month in 2020 for now
#main populates the data base with top trending videos for certain categories and countries

#url must be in this format for now: 'https://www.youtube.com/channel/(replace with own channel id)'

#x = searchurl('https://www.youtube.com/channel/UCo_IB5145EVNcf8hw1Kku7w')
#print(x)
