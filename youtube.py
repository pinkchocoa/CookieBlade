## @file youtube.py
#
# @brief this file uses the Youtube API to retrieve wanted data
#
# @author Nathaniel
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
# - apikey (local)
#   - this file contains the twitter api token/key

#Imports
from googleapiclient.discovery import build
from database import *
from urllib import parse
from datetime import datetime
import apikey #api keys are stored here

## Documentation for Youtube Class
# The Youtube class instantiate connection with the Youtube API
class Youtube:
    """! Youtube Class does the authentication and instantiation to the Youtube API
    """
    api_key = apikey.Y_ACCESS_KEY
    API_SERVICE_NAME = 'youtube'
    API_VERSION = 'v3'
    youtube = build(API_SERVICE_NAME, API_VERSION, developerKey=api_key)

## Documentation for youtubeVid Class
# The youtubeVid class contains methods related to crawling youtube videos
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
        videoCategory = ['10', '17', '20', '25']  # 10 - music, 17 - sports, 20 - gaming, 25 - news and politics
        nextPageToken = None
        for code in countryCode:
            for types in videoCategory:
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
        #Gets the Channel's subcount, totalviewno, totalvidno and appends it into the list
        response = Youtube.youtube.channels().list(
            part="snippet,statistics",
            id=id
        )
        try:
            reply = response.execute()
        except Exception as e:
            print(str(e))
            return ["YT API Limit Error","YT API Limit Error","YT API Limit Error","YT API Limit Error"]

        channelCreateDate = reply["items"][0]["snippet"]["publishedAt"]
        channelCreateDate = channelCreateDate[0:10]
        result.append(channelCreateDate)

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
        """! class that return back the revenue and total views per month for the past year
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
                return [[0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0]]

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
                return [[0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0]]

            dateMade = reply["items"][0]['snippet']['publishedAt']
            newdateMade = dateMade[0:10]
            datesList.append(newdateMade)

        #create a list of list based on the number of videos in the channel
        #3 things in each list inside the list - videoid, no of views, createdAt date
        mainList = []

        for idx, x in enumerate(mainList):
            x.append(resultsList[idx])

            response = Youtube.youtube.videos().list(
                part='statistics',
                id=x[0]
            )

            try:
                reply = response.execute()
            except Exception as e:
                print(str(e))
                return [[0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0]]

            viewcount = reply["items"][0]["statistics"]["viewCount"]
            x.append(viewcount)

            x.append(datesList[idx])

        #Filter out the videos that are made in the past 12 months
        #setting the filter for the months

        calendarEndDate = [31,28,31,30,31,30,31,31,30,31,30,31]
        calendarYear = datetime.now().year - 1
        calendarDates = []
        for idx, x in enumerate(calendarEndDate):
            dateString1 = str(calendarYear) + '-' + str(idx+1) + '-1'
            dateString2 = str(calendarYear) + '-' + str(idx+1) + '-' + str(x)
            dateString1 = datetime.date(datetime.strptime(dateString1, '%Y-%m-%d'))
            dateString2 = datetime.date(datetime.strptime(dateString2, '%Y-%m-%d'))
            calendarDates.append([dateString1,dateString2])

        #Converting the list of dates type string into a list of dates type date
        for x in mainList:
            datetimeobject = datetime.strptime(x[2], '%Y-%m-%d')
            datetimeobject = datetime.date(datetimeobject)
            x[2] = datetimeobject

        #Filtering done here and returns back a list of filtered dates type string
        #lists for the past 12 months
        monthVids = [list() for x in range(12)]
        sortedmonthVids = []
        channelRevByMonth = []

        #sorting the list of dates into their respective months
        for d in mainList:
            for idx, x in enumerate(calendarDates):
                if d[2] >= x[0] and d[2] <= x[1]:
                    d[2] = str(d[2])
                    monthVids[idx].append(d)

        for i in range(0,12):
            #Store the number of vids made per month into a list to return
            sortedmonthVids.append(len(monthVids[i]))
            #Store the amount of revenue earned per month into a list to return
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
        revList = [v for k, v in revDict.items()]

        finalresult = [sortedmonthVids, revList]
        return finalresult
