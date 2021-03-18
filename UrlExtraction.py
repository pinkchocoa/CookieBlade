## @file UrlExtraction.py
#
# @brief this file contains the spider class
#
# @section No imports.

## Documentation for a Url Extraction Class.
# UrlExtraction gets link pass by user and identifies sitename and user unique ID on social platforms.
class UrlExtraction:

    #Get UniqueID based on social media sites.
    def getUniqueID(self,UserUrl):
        """! Extract Unqiue User ID based on site and return said ID.
        @param UserUrl Url link provided by user.
        @return uniqueID
        """

        if "youtube" in UserUrl:
            if "user" in UserUrl:
                uniqueID = UserUrl.replace("https://www.youtube.com/user/","")
                return uniqueID
            else:
                uniqueID = UserUrl.replace("https://www.youtube.com/channel/","") 
                return uniqueID
        elif "twitter" in UserUrl:
            uniqueID = UserUrl.replace("https://twitter.com/","")
            uniqueID = uniqueID.split("?",1)[0] #Split User ID from /ref/.. onwards in link.
            return uniqueID

    #Get Sitename based on Url provided by user.
    def getSiteName(self,UserUrl):
        """! Extract sitename based on Url provided by user.
        @param UserUrl Url link provided by user.
        @return sitename
        """

        UserUrl = UserUrl.replace("https://www.","")
        UserUrl = UserUrl.replace("https://","")
        sitename = UserUrl.split(".",1)[0] #Split sitename from .com/... onwards in link.
        return sitename