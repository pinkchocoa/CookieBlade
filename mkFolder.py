## @file mkFolder.py
#
# @brief This file contains the mkFolder class
#
# @author JunHao
#
# @section libraries_main Libraries/Modules
# - os standard libary (https://docs.python.org/3/library/os.html)
#   - access to folder creation funtions
# - UrlExtraction (local)
#   - access to UrlExtraction class

# Imports
import os
from UrlExtraction import UrlExtraction

## Documentation for a mkFolder Class.
# mkFolder class creates sub folders based on folder existance
# help organaize the files for the crawler program
class mkFolder(UrlExtraction):
    """! mkFolder class
    creates sub folders based on folder existance
    """
    #Check/create data folder
    def createDirectory(self):
        """! Create data in program source folder.
        """
        if os.path.isdir('./data') == False:
            os.mkdir("data")
            pass
        else:
            pass

    #Generic sub folder creator
    def createDataFolder(self,UserUrl):
        """! Create subfolder based on sitename within data folder.
        @param UserUrl Url link provided by user.
        @return sitename
        """
        self.createDirectory()
        sitename = self.getSiteName(UserUrl)
        UserUrl = "./data/" + sitename
        if os.path.isdir(UserUrl):
            return sitename
        else:
            os.mkdir(UserUrl)
            return sitename    