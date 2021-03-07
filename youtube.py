from googleapiclient.discovery import build

class youtube:
    api_key = 'AIzaSyA_JNhdO1UNp8ww2CATP-BwuWbwqWC3Zxw'
    youtube = build('youtube', 'v3', developerKey=api_key)

    def __init__(self, id):
        youtube.id = id
        self.channel_stat(youtube.id)

    @staticmethod
    def channel_stat(channel_id):
        request = youtube.youtube.channels().list(
            part='statistics',
            id=channel_id
        )
        reply = request.execute()
        return reply
