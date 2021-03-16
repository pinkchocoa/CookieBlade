from googleapiclient.discovery import build
from datetime import timedelta
from urllib import parse
from datetime import datetime
import re

api_key = 'AIzaSyB3ely6qW_YfbjHIFVODyufGs9exzVqnM4'
youtube = build('youtube', 'v3', developerKey=api_key)

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
    countryCode = ['SG', 'MY', 'KR', 'JP', 'PH', 'ID']
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


def vidInfo(video):
    #video statistics
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
def searchurl(input):
    #converting the url input to just the channel id
    url_parsed = parse.urlparse(input).path
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


#Function to return back the revenue and total views per month for the year of 2020
def getRevenueData(input):

    # converting the url input to just the channel id
    url_parsed = parse.urlparse(input).path
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


# print(searchurl("https://www.youtube.com/channel/UCbaGn5VkOVlcRgIWAHcrJKA"))
# print(getRevenueData("https://www.youtube.com/channel/UCbaGn5VkOVlcRgIWAHcrJKA"))
