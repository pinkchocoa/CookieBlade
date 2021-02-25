#Extract Sitename and User unique ID in links.
class UrlExtraction:

    #get User ID of major social media sites. Add Custom replace input requrie to support more sites.
    def getUniqueID(self,UserUrl):
        if "youtube" in UserUrl:
            if "user" in UserUrl:
                uniqueID = UserUrl.replace("https://www.youtube.com/user/","")
                return uniqueID
            else:
                uniqueID = UserUrl.replace("https://www.youtube.com/channel/","") 
                return uniqueID
        elif "twitter" in UserUrl:
            uniqueID = UserUrl.replace("https://twitter.com/","")
            uniqueID = uniqueID.split("?",1)[0]                     #split user name from ref in Url if Url contain ref/etc..
            return uniqueID
    #ENDOFMETHOD

    #Get Sitename
    def getSiteName(self,UserUrl):
        UserUrl = UserUrl.replace("https://www.","")
        UserUrl = UserUrl.replace("https://","")
        sitename = UserUrl.split(".",1)[0]
        return sitename
    #ENDOFMETHOD