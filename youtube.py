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

    resultsList = []  # list to return result
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

    # convert the video ids into created date and put them into another list
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

    # Filter out the videos that are made in Year 2020
    # setting the filter for months (Year 2020)
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

    # Converting the list of dates type string into a list of dates type date
    dt_dates = []
    for d in datesList:
        datetimeobject = datetime.strptime(d, '%Y-%m-%d')
        datetimeobject = datetime.date(datetimeobject)
        dt_dates.append(datetimeobject)

    # Filtering done here and returns back a list of filtered dates type string
    # lists for the various months of 2020
    monthVids = [list() for x in range(12)]
    sortedmonthVids = []
    channelRevByMonth = []

    # sorting the list of dates into their respective months
    for d in dt_dates:
        if d >= janstart_date and d <= janend_date:
            d = str(d)
            monthVids[0].append(d)
        elif d >= febstart_date and d <= febend_date:
            d = str(d)
            monthVids[1].append(d)
        elif d >= marstart_date and d <= marend_date:
            d = str(d)
            monthVids[2].append(d)
        elif d >= aprstart_date and d <= aprend_date:
            d = str(d)
            monthVids[3].append(d)
        elif d >= maystart_date and d <= mayend_date:
            d = str(d)
            monthVids[4].append(d)
        elif d >= junstart_date and d <= junend_date:
            d = str(d)
            monthVids[5].append(d)
        elif d >= julstart_date and d <= julend_date:
            d = str(d)
            monthVids[6].append(d)
        elif d >= augstart_date and d <= augend_date:
            d = str(d)
            monthVids[7].append(d)
        elif d >= sepstart_date and d <= sepend_date:
            d = str(d)
            monthVids[8].append(d)
        elif d >= octstart_date and d <= octend_date:
            d = str(d)
            monthVids[9].append(d)
        elif d >= novstart_date and d <= novend_date:
            d = str(d)
            monthVids[10].append(d)
        elif d >= decstart_date and d <= decend_date:
            d = str(d)
            monthVids[11].append(d)
    # Store the number of vids made per month into a list to return
    sortedmonthVids.append(len(monthVids[0]))
    sortedmonthVids.append(len(monthVids[1]))
    sortedmonthVids.append(len(monthVids[2]))
    sortedmonthVids.append(len(monthVids[3]))
    sortedmonthVids.append(len(monthVids[4]))
    sortedmonthVids.append(len(monthVids[5]))
    sortedmonthVids.append(len(monthVids[6]))
    sortedmonthVids.append(len(monthVids[7]))
    sortedmonthVids.append(len(monthVids[8]))
    sortedmonthVids.append(len(monthVids[9]))
    sortedmonthVids.append(len(monthVids[10]))
    sortedmonthVids.append(len(monthVids[11]))

    # Store the amount of revenue earned per month into a list to return

    return sortedmonthVids
