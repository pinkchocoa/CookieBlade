from googleapiclient.discovery import build

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
        for stuff in range(0,15):
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
        video.dislikeCount = reply["items"][0]["statistics"]["viewCount"]
    except Exception as e:
        video.dislikeCount = 0
    return video

reply = scrapData()
for i in range(0,len(reply)):
    reply[i] = vidInfo(reply[i])
    print(reply[i].getDict())
