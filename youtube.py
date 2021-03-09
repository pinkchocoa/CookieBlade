from googleapiclient.discovery import build
import re

api_key = 'AIzaSyA_JNhdO1UNp8ww2CATP-BwuWbwqWC3Zxw'
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
            "dislikeCount" : self.dislikeCount
        }
        return videoDetail

def scrapData():
    VidList = []
    countryCode = ['SG','MY','PH','KR','JP','TH','ID','TW']
    nextPageToken = None
    for code in countryCode:
        for stuff in range(0,5):
            #request details
            request = youtube.videos().list(
                part='snippet',
                maxResults=10,
                chart='mostPopular',
                regionCode=code,
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
    return video

# def playlistlength(playListID):
#     request = youtube.playlistItems().list(
#         part='contentDetails',
#         playlistId=playListID
#     )
#     try:
#         response = request.execute()
#     except Exception as e:
#         print(str(e))

class channel():
    country = ''
    totalVid = 0
    subCount = 0
    totalview = 0
    channelbd = ''
    channelid = ''
    description = ''
    channel_name = ''
    channel_thumbnail = ''
    channelVids = []

    def channelDetail(self):
        channelDetail = {
            "country" : self.country,
            "totalVideos" : self.totalVid,
            "subCount" : self.subCount,
            "totalview" : self.totalview,
            "channelbirthdate" : self.channelbd,
            "channel id" : self.channelid,
            "description" : self.description,
            "channel name" : self.channel_name,
            "channel thumbnail" : self.channel_thumbnail,
            "channel Videos" : self.channelVids
        }
        return channelDetail

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
        chn.country = response["items"][0]["snippet"]["country"]
        chn.channelbd = response["items"][0]["snippet"]["publishedAt"]
        chn.channelid = response["items"][0]["id"]
        chn.description = response["items"][0]["snippet"]["description"]
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
        channel.subCount = response["items"][0]["statistics"]["subscriberCount"]
        channel.totalview = response["items"][0]["statistics"]["viewCount"]
        return channel


    def getChannelVid(chnvid):
        nextPageToken = None
        for result in range(0,25):
            channel = youtube.search().list(
                part='snippet',
                channelId=chnvid.channelid,
                type='video',
                videoDefinition='any',
                maxResults=50,
                videoType='any',
                pageToken = nextPageToken
            )
            try:
                response = channel.execute()
                nextPageToken = response.get('nextPageToken')
            except Exception as e:
                print(str(e))


            for vidId in response['items']:
                chnvid.channelVids.append(vidId["id"]["videoId"])
        return chnvid
