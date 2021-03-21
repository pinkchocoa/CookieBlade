## @file youtube.py
#
# @brief this file uses the Youtube API to retrieve wanted data
#
# @section libraries_main Libraries/Modules
# - googleapiclient.discovery
#   - access to youtube API
# - database
#   - required to store data crawled from youtube
# - urllib
#   - access to urllib to parse certain urls
# - datetime
#   - setting the conditions for filtering of data needed

#Imports
from googleapiclient.discovery import build
from database import *
from urllib import parse
from datetime import datetime
import apikey #api keys are stored here

class Youtube:

    api_key = apikey.Y_ACCESS_KEY
    youtube = build('youtube', 'v3', developerKey=api_key)

class youtubeVid(Youtube):
    """! youtubeVid Class inherits the youtube class variables
    This class contains methods related to crawling youtube videos
    """
    # class variable
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
        """! class method that creates a dictionary
        """
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

    #Get trending video #No return type
    def getTrendingVideo(self):
        """! class method that gets data from other class methods to store in a database
        """
        reply = self.scrapData()
        tuser = database('TrendVideo')
        tuser.createTable('TrendVideo', 'key', 'C1', 'C2', 'C3', 'C4', 'C5', 'C6', 'C7', 'C8', 'C9', 'C10')
        for i in range(0, len(reply)):
            reply[i] = self.vidInfo(reply[i])
            TrendVidsInfo = reply[i].getDict()
            TrendVidsInfoList = [(v) for k, v in TrendVidsInfo.items()]
            TrendVidsInfoList.insert(0, i)
            tuser.insertTable(TrendVidsInfoList, 'TrendVideo', 'key', 'C1', 'C2', 'C3', 'C4', 'C5', 'C6', 'C7', 'C8', 'C9', 'C10')
        
    # Function to crawl for top trending videos for a list of countries
    def scrapData(self):
        """! class method that crawls for top trending videos on youtube
        The data crawled is based on 3 countries SG, MY & PH
        The categories are music, sports, gaming, and news & politics
        @return a list of video details objects
        """

        VidList = []
        countryCode = ['SG', 'MY', 'PH']
        videoCategory = ['10', '17', '20', '25', ]  # 10 - music, 17 - sports, 20 - gaming, 25 - news and politics
        nextPageToken = None
        for code in countryCode:
            for types in videoCategory:
                for pages in range(0, 1):
                    # request details
                    request = Youtube.youtube.videos().list(
                        part='snippet',
                        maxResults=5,
                        chart='mostPopular',
                        regionCode=code,
                        videoCategoryId=types,
                        pageToken=nextPageToken
                    )

                    # getting a request
                    try:
                        response = request.execute()
                        nextPageToken = response.get('nextPageToken')
                    except Exception as e:
                        print(str(e))
                        break

                    # storing the details into each video object
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

    def vidInfo(self, video):
        """! class method that crawls for top trending videos on youtube
        @param object of the class youtubeVids
        @return a list of video details objects
        """
        # video statistics
        info = Youtube.youtube.videos().list(
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

    # function to retrieve a list of trend vids info based on the input and sorted by category #supports only SG,MY,PH
    def getDBvids(self, countryCode):
        """! class method that retrieves data from the database and returns it
        @param countrycode of the country to retrieve data of
        @return a list of views for each popular category
        """
        # variables
        totalmusicviews = 0
        totalsportsviews = 0
        totalgamesviews = 0
        totalnewsviews = 0
        datalist = []
        tuser = database('TrendVideo')
        templist = tuser.getTableData('TrendVideo')

        countryList = [0,20,40]
        if countryCode == "SG":
            x = 0
        elif countryCode == "MY":
            x = 20
        elif countryCode == "PH":
            x = 40

        for idx, i in enumerate(range(x, 20+x)):
            if idx < 5: # viewcounts for music
                totalmusicviews += int(templist[i][7])
            elif idx < 10: # viewcounts for sports
                totalsportsviews += int(templist[i][7])
            elif idx < 15: # viewcounts for gaming
                totalgamesviews += int(templist[i][7])
            elif idx < 20: # viewcounts for news & politics
                totalnewsviews += int(templist[i][7])

        datalist.append(totalmusicviews)
        datalist.append(totalsportsviews)
        datalist.append(totalgamesviews)
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

class Channel(Youtube):
    """! Channel Class inherits the variables in the youtube class
    This class contains methods specifically related to a channel
    """

    #Function to return a list of subs, totalviewno, totalvidno and created-at-date from a channel
    def searchurl(self, input):
        """! class method that creates a TTweet instance with username
        @param a youtube url containing a channel id
        @return a list of results - date of channel creation, video count, subscriber count and view count
        """
        #converting the url input to just the channel id
        url_parsed = parse.urlparse(input).path
        id = url_parsed.split('/')[-1]

        result = [] #list that contains results to return

        #Gets the Channel's createAt date and appends it into the list
        response = Youtube.youtube.channels().list(
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
        response = Youtube.youtube.channels().list(
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
    def getRevenueData(self, input):
        """! class method that creates a TTweet instance with username
        @param a youtube url containing a channel id
        @return a list of vids created and ad-revenue earned by the channel in the past 12 months
        """
        # converting the url input to just the channel id
        url_parsed = parse.urlparse(input).path
        id = url_parsed.split('/')[-1]

        resultsList = []
        datesList = []

        # Get a list of the channel's videos and put them into a list
        nextPageToken = None
        for result in range(0, 20):
            response = Youtube.youtube.search().list(
                part='snippet',
                channelId=id,
                type='video',
                videoDefinition='any',
                maxResults=50,
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
            response = Youtube.youtube.videos().list(
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
        #3 things in each list inside the list - videoid, no of views, createdAt date
        mainList = [list() for x in range(len(resultsList))]

        for i in range(0, len(mainList)):
            mainList[i].append(resultsList[i])

        for i in range(0, len(mainList)):
            response = Youtube.youtube.videos().list(
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


        #Filter out the videos that are made in the past 12 months
        #setting the filter for the months
        start_date = datetime.strptime('2020-3-1', '%Y-%m-%d')
        janstart_date = datetime.date(start_date)
        end_date = datetime.strptime('2020-3-31', '%Y-%m-%d')
        janend_date = datetime.date(end_date)
        start_date = datetime.strptime('2020-4-1', '%Y-%m-%d')
        febstart_date = datetime.date(start_date)
        end_date = datetime.strptime('2020-4-30', '%Y-%m-%d')
        febend_date = datetime.date(end_date)
        start_date = datetime.strptime('2020-5-1', '%Y-%m-%d')
        marstart_date = datetime.date(start_date)
        end_date = datetime.strptime('2020-5-31', '%Y-%m-%d')
        marend_date = datetime.date(end_date)
        start_date = datetime.strptime('2020-6-1', '%Y-%m-%d')
        aprstart_date = datetime.date(start_date)
        end_date = datetime.strptime('2020-6-30', '%Y-%m-%d')
        aprend_date = datetime.date(end_date)
        start_date = datetime.strptime('2020-7-1', '%Y-%m-%d')
        maystart_date = datetime.date(start_date)
        end_date = datetime.strptime('2020-7-31', '%Y-%m-%d')
        mayend_date = datetime.date(end_date)
        start_date = datetime.strptime('2020-8-1', '%Y-%m-%d')
        junstart_date = datetime.date(start_date)
        end_date = datetime.strptime('2020-8-31', '%Y-%m-%d')
        junend_date = datetime.date(end_date)
        start_date = datetime.strptime('2020-9-1', '%Y-%m-%d')
        julstart_date = datetime.date(start_date)
        end_date = datetime.strptime('2020-9-30', '%Y-%m-%d')
        julend_date = datetime.date(end_date)
        start_date = datetime.strptime('2020-10-1', '%Y-%m-%d')
        augstart_date = datetime.date(start_date)
        end_date = datetime.strptime('2020-10-31', '%Y-%m-%d')
        augend_date = datetime.date(end_date)
        start_date = datetime.strptime('2020-11-1', '%Y-%m-%d')
        sepstart_date = datetime.date(start_date)
        end_date = datetime.strptime('2020-11-30', '%Y-%m-%d')
        sepend_date = datetime.date(end_date)
        start_date = datetime.strptime('2020-12-1', '%Y-%m-%d')
        octstart_date = datetime.date(start_date)
        end_date = datetime.strptime('2020-12-31', '%Y-%m-%d')
        octend_date = datetime.date(end_date)
        start_date = datetime.strptime('2021-1-1', '%Y-%m-%d')
        novstart_date = datetime.date(start_date)
        end_date = datetime.strptime('2021-1-31', '%Y-%m-%d')
        novend_date = datetime.date(end_date)
        start_date = datetime.strptime('2021-2-1', '%Y-%m-%d')
        decstart_date = datetime.date(start_date)
        end_date = datetime.strptime('2021-2-28', '%Y-%m-%d')
        decend_date = datetime.date(end_date)

        #Converting the list of dates type string into a list of dates type date
        for d in range(0, len(mainList)):
            datetimeobject = datetime.strptime(mainList[d][2], '%Y-%m-%d')
            datetimeobject = datetime.date(datetimeobject)
            mainList[d][2] = datetimeobject

        #Filtering done here and returns back a list of filtered dates type string
        #lists for the past 12 months
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
                monthRev = round(monthRev,2)
            channelRevByMonth.append(monthRev)

        #revenue dictionary
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





#HOW TO USE FOR NOW
#########################################################################################################
#Firstly, populate the database with trending vid info by calling the getTrendingVideo() once
#To test if there's data in the database, install DB Browser (SQLite) to check
#
#Functions to usable:
#getDBvids() assumes that the input to get a particular country's trending vid is a number, which will then return a list
#searchurl returns back a list of subs, totalviewno, totalvidno and created-at-date from a channel
#getRevenueData returns back a list containing (1)a list containing the no of list made each month
#                                              (2)a list containing the total amount of revenue earned for each month
#

#To note:
#url must be in this format for now: 'https://www.youtube.com/channel/(replace with own channel id)'
#Example below:
# x = Channel().searchurl('UC0NwzCHb8Fg89eTB5eYX17Q')
# print(x)
