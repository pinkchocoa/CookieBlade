from googleapiclient.discovery import build
from database import *
from urllib import parse
from datetime import datetime


api_key = 'AIzaSyA_JNhdO1UNp8ww2CATP-BwuWbwqWC3Zxw'
youtube = build('youtube', 'v3', developerKey=api_key)

#database to store trending vid info

class youtubeVid():
    # object variable
    title = ''
    videoID = ''
    thumbnail = ''
    channelID = ''
    publishedAt = ''
    countryTrending = ''
    viewCount = 0
    likeCount = 0
    dislikeCount = 0
    revenue = 0

    def getDict(self):
        videoDetail = {
            "title" : self.title,
            "videoID" : self.videoID,
            "thumbnail" : self.thumbnail,
            "channelID" : self.channelID,
            "publishedAt" : self.publishedAt,
            "countryTrending" : self.countryTrending,
            "viewCount" : self.viewCount,
            "likeCount" : self.likeCount,
            "dislikeCount" : self.dislikeCount,
            "revenue" : self.revenue
        }
        return videoDetail

class channel():
    country = ''
    totalVid = 0
    subCount = 0
    totalview = 0
    channelbd = ''
    channelid = ''
    channel_name = ''
    channel_thumbnail = ''

    #channel dictionary for top trending object
    def channelDetail(self):
        channelDetail = {
            "country" : self.country,
            "totalVideos" : self.totalVid,
            "subCount" : self.subCount,
            "totalview" : self.totalview,
            "channelbirthdate" : self.channelbd,
            "channel id" : self.channelid,
            "channel name" : self.channel_name,
            "channel thumbnail" : self.channel_thumbnail,
        }
        return channelDetail #Return data in a dictionary

    def getChannelDetail(chan):
        channelList = []
        request = youtube.channels().list(
            part='snippet',
            id=chan['channelID']
        )
        #execute the request
        try:
            response = request.execute()
        except Exception as e:
            print(str(e))
        #appending the channel info
        chn = channel()
        try:
            chn.country = response["items"][0]["snippet"]["country"]
        except Exception as e:
            chn.country = ""
        chn.channelbd = response["items"][0]["snippet"]["publishedAt"]
        chn.channelid = response["items"][0]["id"]
        chn.channel_name = response["items"][0]["snippet"]["title"]
        chn.channel_thumbnail = response["items"][0]["snippet"]["thumbnails"]["default"]["url"]
        channelList.append(chn)
        return channelList

    def getChannelStat(channel):
        statrequest = youtube.channels().list(
            part='statistics',
            id=channel.channelid
        )
        try:
            response = statrequest.execute()
        except Exception as e:
            print(str(e))
        channel.totalVid = response["items"][0]["statistics"]["videoCount"]
        try:
            channel.subCount = response["items"][0]["statistics"]["subscriberCount"]
        except Exception as e:
            channel.subCount = 0
        channel.totalview = response["items"][0]["statistics"]["viewCount"]
        return channel


    #List of vids ids from a channel
    def getChannelVid(chnvid):
        nextPageToken = None
        for result in range(0,1):
            channel = youtube.search().list(
                part='snippet',
                channelId=chnvid.channelid,
                type='video',
                videoDefinition='any',
                maxResults=5,
                videoType='any',
                pageToken=nextPageToken
            )
            try:
                response = channel.execute()
                nextPageToken = response.get('nextPageToken')
            except Exception as e:
                print(str(e))

            for vidId in response['items']:
                chnvid.channelVids.append(vidId["id"]["videoId"])
        return chnvid

#Function to crawl for top trending videos for a list of countries
def scrapData():
    VidList = []
    countryCode = ['SG', 'MY', 'PH']
    videoCategory = ['10', '17', '20', '25',] #10 - music, 17 - sports, 20 - gaming, 25 - news and politics
    nextPageToken = None
    for code in countryCode:
        for types in videoCategory:
            for pages in range(0,1):
                #request details
                request = youtube.videos().list(
                    part='snippet',
                    maxResults=5,
                    chart='mostPopular',
                    regionCode=code,
                    videoCategoryId=types,
                    pageToken=nextPageToken
                )

                #getting a request
                try:
                    response = request.execute()
                    nextPageToken = response.get('nextPageToken')
                except Exception as e:
                    print(str(e))

                #storing the details into each video object
                for item in response['items']:
                    video = youtubeVid()
                    video.title = item['snippet']['title']
                    video.videoID = item['id']
                    video.thumbnail = item['snippet']['thumbnails']['default']['url']
                    video.channelID = item['snippet']['channelId']
                    video.publishedAt = item['snippet']['publishedAt']
                    video.countryTrending = code
                    VidList.append(video)
    return VidList


def vidInfo(videoUrl):
    #video statistics
    video = videoUrl
    info = youtube.videos().list(
    part='statistics',
    id=video.videoID
    )
    try:
        reply = info.execute()
    except Exception as e:
        print(str(e))
    video.viewCount = reply["items"][0]["statistics"]["viewCount"]
    try:
        video.likeCount = reply["items"][0]["statistics"]["likeCount"]
    except Exception as e:
        video.likeCount = 0
    try:
        video.dislikeCount = reply["items"][0]["statistics"]["dislikeCount"]
    except Exception as e:
        video.dislikeCount = 0
    video.revenue = str(round(int(video.viewCount) * 0.02, 2))
    return video


#############################################################
#Functions below for searching information by getting input
#############################################################

#Function to return a list of subs, totalviewno, totalvidno and created-at-date from a channel
def getChannelStats(channelUrl):
    #converting the url input to just the channel id
    url_parsed = parse.urlparse(channelUrl).path
    id = url_parsed.split('/')[-1]

    result = [] #list that contains results to return

    #Gets the Channel's createAt date and appends it into the list
    response = youtube.channels().list(
        part='snippet',
        id=id
    )
    try:
        reply = response.execute()
    except Exception as e:
        print(str(e))

    channelCreateDate = reply["items"][0]["snippet"]["publishedAt"]
    channelCreateDate = channelCreateDate[0:10]
    result.append(channelCreateDate)

    #Gets the Channel's subcount, totalviewno, totalvidno and appends it into the list
    response = youtube.channels().list(
        part='statistics',
        id=id
    )
    try:
        reply = response.execute()
    except Exception as e:
        print(str(e))

    try:
        channelTotalVid = reply["items"][0]["statistics"]["videoCount"]
    except Exception as e:
        channelTotalVid = 0
    try:
        subCount = reply["items"][0]["statistics"]["subscriberCount"]
    except Exception as e:
        subCount = 0
    try:
        channelTotalView = reply["items"][0]["statistics"]["viewCount"]
    except Exception as e:
        channelTotalView = 0
    result.append(channelTotalVid)
    result.append(subCount)
    result.append(channelTotalView)

    return result


#Function to return back the revenue and total views per month for the year of 2020 #Broken
def getRevenueData(channelUrl):

    # converting the url input to just the channel id
    url_parsed = parse.urlparse(channelUrl).path
    id = url_parsed.split('/')[-1]

    resultsList = []
    datesList = []

    # Get a list of the channel's videos and put them into a list
    nextPageToken = None
    for result in range(0, 2):
        response = youtube.search().list(
            part='snippet',
            channelId=id,
            type='video',
            videoDefinition='any',
            maxResults=5,
            videoType='any',
            pageToken=nextPageToken
        )
        try:
            reply = response.execute()
            nextPageToken = reply.get('nextPageToken')
        except Exception as e:
            print(str(e))

        for vidId in reply['items']:
            resultsList.append(vidId["id"]["videoId"])

    #convert the video ids into created date and put them into another list
    for id in range(0, len(resultsList)):
        response = youtube.videos().list(
            part='snippet',
            id=resultsList[id]
        )
        try:
            reply = response.execute()
        except Exception as e:
            print(str(e))
        dateMade = reply["items"][0]['snippet']['publishedAt']
        newdateMade = dateMade[0:10]
        datesList.append(newdateMade)


    #create a list of list based on the number of videos in the channel
    #I want 3 things in each list inside the list
    #first - videoid, second - no of views, third - createdAt date
    mainList = [list() for x in range(len(resultsList))]

    for i in range(0, len(mainList)):
        mainList[i].append(resultsList[i])

    for i in range(0, len(mainList)):
        response = youtube.videos().list(
            part='statistics',
            id=mainList[i][0]
        )
        try:
            reply = response.execute()
        except Exception as e:
            print(str(e))
        viewcount = reply["items"][0]["statistics"]["viewCount"]
        mainList[i].append(viewcount)

    for i in range(0, len(mainList)):
        mainList[i].append(datesList[i])


    #Filter out the videos that are made in Year 2020
    #setting the filter for months (Year 2020)
    start_date = datetime.strptime('2020-1-1', '%Y-%m-%d')
    janstart_date = datetime.date(start_date)
    end_date = datetime.strptime('2020-1-31', '%Y-%m-%d')
    janend_date = datetime.date(end_date)
    start_date = datetime.strptime('2020-2-1', '%Y-%m-%d')
    febstart_date = datetime.date(start_date)
    end_date = datetime.strptime('2020-2-29', '%Y-%m-%d')
    febend_date = datetime.date(end_date)
    start_date = datetime.strptime('2020-3-1', '%Y-%m-%d')
    marstart_date = datetime.date(start_date)
    end_date = datetime.strptime('2020-3-31', '%Y-%m-%d')
    marend_date = datetime.date(end_date)
    start_date = datetime.strptime('2020-4-1', '%Y-%m-%d')
    aprstart_date = datetime.date(start_date)
    end_date = datetime.strptime('2020-4-30', '%Y-%m-%d')
    aprend_date = datetime.date(end_date)
    start_date = datetime.strptime('2020-5-1', '%Y-%m-%d')
    maystart_date = datetime.date(start_date)
    end_date = datetime.strptime('2020-5-31', '%Y-%m-%d')
    mayend_date = datetime.date(end_date)
    start_date = datetime.strptime('2020-6-1', '%Y-%m-%d')
    junstart_date = datetime.date(start_date)
    end_date = datetime.strptime('2020-6-30', '%Y-%m-%d')
    junend_date = datetime.date(end_date)
    start_date = datetime.strptime('2020-7-1', '%Y-%m-%d')
    julstart_date = datetime.date(start_date)
    end_date = datetime.strptime('2020-7-31', '%Y-%m-%d')
    julend_date = datetime.date(end_date)
    start_date = datetime.strptime('2020-8-1', '%Y-%m-%d')
    augstart_date = datetime.date(start_date)
    end_date = datetime.strptime('2020-8-31', '%Y-%m-%d')
    augend_date = datetime.date(end_date)
    start_date = datetime.strptime('2020-9-1', '%Y-%m-%d')
    sepstart_date = datetime.date(start_date)
    end_date = datetime.strptime('2020-9-30', '%Y-%m-%d')
    sepend_date = datetime.date(end_date)
    start_date = datetime.strptime('2020-10-1', '%Y-%m-%d')
    octstart_date = datetime.date(start_date)
    end_date = datetime.strptime('2020-10-31', '%Y-%m-%d')
    octend_date = datetime.date(end_date)
    start_date = datetime.strptime('2020-11-1', '%Y-%m-%d')
    novstart_date = datetime.date(start_date)
    end_date = datetime.strptime('2020-11-30', '%Y-%m-%d')
    novend_date = datetime.date(end_date)
    start_date = datetime.strptime('2020-12-1', '%Y-%m-%d')
    decstart_date = datetime.date(start_date)
    end_date = datetime.strptime('2020-12-31', '%Y-%m-%d')
    decend_date = datetime.date(end_date)

    #Converting the list of dates type string into a list of dates type date
    for d in range(0, len(mainList)):
        datetimeobject = datetime.strptime(mainList[d][2], '%Y-%m-%d')
        datetimeobject = datetime.date(datetimeobject)
        mainList[d][2] = datetimeobject

    #Filtering done here and returns back a list of filtered dates type string
    #lists for the various months of 2020
    monthVids = [list() for x in range(12)]
    sortedmonthVids = []
    channelRevByMonth = []

    #sorting the list of dates into their respective months
    for d in mainList:
        if d[2] >= janstart_date and d[2] <= janend_date:
            d[2] = str(d[2])
            monthVids[0].append(d)
        elif d[2] >= febstart_date and d[2] <= febend_date:
            d[2] = str(d[2])
            monthVids[1].append(d)
        elif d[2] >= marstart_date and d[2] <= marend_date:
            d[2] = str(d[2])
            monthVids[2].append(d)
        elif d[2] >= aprstart_date and d[2] <= aprend_date:
            d[2] = str(d[2])
            monthVids[3].append(d)
        elif d[2] >= maystart_date and d[2] <= mayend_date:
            d[2] = str(d[2])
            monthVids[4].append(d)
        elif d[2] >= junstart_date and d[2] <= junend_date:
            d[2] = str(d[2])
            monthVids[5].append(d)
        elif d[2] >= julstart_date and d[2] <= julend_date:
            d[2] = str(d[2])
            monthVids[6].append(d)
        elif d[2] >= augstart_date and d[2] <= augend_date:
            d[2] = str(d[2])
            monthVids[7].append(d)
        elif d[2] >= sepstart_date and d[2] <= sepend_date:
            d[2] = str(d[2])
            monthVids[8].append(d)
        elif d[2] >= octstart_date and d[2] <= octend_date:
            d[2] = str(d[2])
            monthVids[9].append(d)
        elif d[2] >= novstart_date and d[2] <= novend_date:
            d[2] = str(d[2])
            monthVids[10].append(d)
        elif d[2] >= decstart_date and d[2] <= decend_date:
            d[2] = str(d[2])
            monthVids[11].append(d)

    #Store the number of vids made per month into a list to return
    for i in range(0,12):
        sortedmonthVids.append(len(monthVids[i]))


    #Store the amount of revenue earned per month into a list to return
    for i in range(0,12):
        monthRev = 0
        for j in range(0,len(monthVids[i])):
            #formula to calculate revenue here
            monthRev += int(monthVids[i][j][1]) * 0.02
        channelRevByMonth.append(monthRev)

    revDict = {
        "jan" : channelRevByMonth[0],
        "feb" : channelRevByMonth[1],
        "mar" : channelRevByMonth[2],
        "apr" : channelRevByMonth[3],
        "may" : channelRevByMonth[4],
        "jun" : channelRevByMonth[5],
        "jul" : channelRevByMonth[6],
        "aug" : channelRevByMonth[7],
        "sep" : channelRevByMonth[8],
        "oct" : channelRevByMonth[9],
        "nov" : channelRevByMonth[10],
        "dec" : channelRevByMonth[11]
    }
    revList = [(k, v) for k, v in revDict.items()]

    finalresult = [sortedmonthVids, revList]
    return finalresult

#Get trending video #return dictionary of video info #No return type
def getTrendingVideo():

    reply = scrapData()
    path = '1009Project' + '/crawled.txt'
    tuser = database('TrendVideo')
    tuser.createTable('TrendVideo', 'key', 'C1', 'C2', 'C3', 'C4', 'C5', 'C6', 'C7', 'C8', 'C9', 'C10')
    for i in range(0, len(reply)):
        reply[i] = vidInfo(reply[i])
        TrendVidsInfo = reply[i].getDict()
        TrendVidsInfoList = [(v) for k, v in TrendVidsInfo.items()]
        TrendVidsInfoList.insert(0, i)
        tuser.insertTable(TrendVidsInfoList, 'TrendVideo', 'key', 'C1', 'C2', 'C3', 'C4', 'C5', 'C6', 'C7', 'C8', 'C9', 'C10')

#function to retrieve a list of trend vids info based on the input and sorted by category #supports only SG,MY,PH
def getDBvids(countryCode):
    #variables
    totalmusicviews = 0
    totalsportsviews = 0
    totalgamesviews = 0
    totalnewsviews = 0
    datalist = []
    tuser = database('TrendVideo')
    templist = tuser.getTableData('TrendVideo')
    if countryCode == "SG": #SG
        #viewcounts for music
        for i in range(0,5):
            totalmusicviews += int(templist[i][7])
        datalist.append(totalmusicviews)
        #viewcounts for sports
        for i in range(5, 10):
            totalsportsviews += int(templist[i][7])
        datalist.append(totalsportsviews)
        #viewcounts for gaming
        for i in range(10,15):
            totalgamesviews += int(templist[i][7])
        datalist.append(totalgamesviews)
        #viewcounts for news & politics
        for i in range(15,20):
            totalnewsviews += int(templist[i][7])
        datalist.append(totalnewsviews)

        # dictionary for dbinfo
        dbdict = {
            "totalmusicviews": datalist[0],
            "totalsportsviews": datalist[1],
            "totalgamesviews": datalist[2],
            "totalnewsviews": datalist[3]
        }
        dbdatalist = [(k, v) for k, v in dbdict.items()]

        return dbdatalist

    elif countryCode == "MY": #MY
        # viewcounts for music
        for i in range(20, 25):
            totalmusicviews += int(templist[i][7])
        datalist.append(totalmusicviews)
        # viewcounts for sports
        for i in range(25, 30):
            totalsportsviews += int(templist[i][7])
        datalist.append(totalsportsviews)
        # viewcounts for gaming
        for i in range(30, 35):
            totalgamesviews += int(templist[i][7])
        datalist.append(totalgamesviews)
        # viewcounts for news & politics
        for i in range(35, 40):
            totalnewsviews += int(templist[i][7])
        datalist.append(totalnewsviews)

        # dictionary for dbinfo
        dbdict = {
            "totalmusicviews": datalist[0],
            "totalsportsviews": datalist[1],
            "totalgamesviews": datalist[2],
            "totalnewsviews": datalist[3]
        }
        dbdatalist = [(k, v) for k, v in dbdict.items()]

        return dbdatalist

    elif countryCode == "PH": #PH
        # viewcounts for music
        for i in range(40, 45):
            totalmusicviews += int(templist[i][7])
        datalist.append(totalmusicviews)
        # viewcounts for sports
        for i in range(45, 50):
            totalsportsviews += int(templist[i][7])
        datalist.append(totalsportsviews)
        # viewcounts for gaming
        for i in range(50, 55):
            totalgamesviews += int(templist[i][7])
        datalist.append(totalgamesviews)
        # viewcounts for news & politics
        for i in range(55, 60):
            totalnewsviews += int(templist[i][7])
        datalist.append(totalnewsviews)

        # dictionary for dbinfo
        dbdict = {
            "totalmusicviews": datalist[0],
            "totalsportsviews": datalist[1],
            "totalgamesviews": datalist[2],
            "totalnewsviews": datalist[3]
        }
        dbdatalist = [(k, v) for k, v in dbdict.items()]

        return dbdatalist

#HOW TO USE FOR NOW
#########################################################################################################
#Firstly, populate the database with trending vid info by calling the getTrendingVideo() once
#To test if there's data in the database, install DB Browser (SQLite) to check
#
#Functions to usable:
#getDBvids() assumes that the input to get a particular country's trending vid is a number, which will then return a list
#searchurl returns back a list of subs, totalviewno, totalvidno and created-at-date from a channel
#getRevenueData returns back a list containing (1)a list containing the no of list made each month ?
#                                              (2)a list containing the total amount of revenue earned for each month ?
#
#To note:
#url format: 'https://www.youtube.com/channel/(replace with own channel id)'
#Example below:
# x = searchurl('https://www.youtube.com/channel/UCR1IuLEqb6UEA_zQ81kwXfg')
# getTrendingVideo()
# y = getDBvids('SG')
# print(x)
# print(y)

# print(getRevenueData('https://www.youtube.com/channel/UCtUId5WFnN82GdDy7DgaQ7w'))