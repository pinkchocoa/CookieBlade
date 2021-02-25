import os
from UrlExtraction import UrlExtraction

#class does not return anything only create folders
class mkFolder(UrlExtraction):

    #Check/create data folder
    def createDirectory(self):
        if os.path.isdir('./data') == False:
            os.mkdir("data")
            pass
        else:
            pass
    #ENDOFMETHOD

    #Generic sub folder creator
    def createDataFolder(self,UserUrl):
        self.createDirectory()
        sitename = self.getSiteName(UserUrl)
        UserUrl = "./data/" + sitename
        if os.path.isdir(UserUrl):
            return sitename
        else:
            os.mkdir(UserUrl)
            return sitename
    #ENDOFMETHOD