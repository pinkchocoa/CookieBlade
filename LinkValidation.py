## @file LinkValidation.py
#
# @brief this file contains the LinkValidation Class
#
# @section libraries_main Libraries/Modules
# - os standard library (https://docs.python.org/3/library/os.html)
#   - access to os ping function command.
# - urllib.request standard library (https://docs.python.org/3/library/urllib.request.html)
#   - access to urlopen function
# - UrlExtraction (local)
#   - access to UrlExtraction class

# Imports
import os
import urllib.request
from UrlExtraction import UrlExtraction

## Documentation for a LinkValidation Class
# LinkValidation class checks if given link is supported
# also check if host system is online.
class LinkValidation(UrlExtraction):

    # __init__ is the constructor name for all classes
    def __init__(self):
        """! LinkValidation class initializer
        @return an instance of the LinkValidation Class with the initialized list below.
        """

        #List of supported sites.
        self.Sitelist = ["youtube", "twitter"]
    
    #Check if URL is valid and site is supported
    def UrlValidation(self, UserUrl):
        """! Check if Url is valid and site is supported.
        @return True or False
        """

        sitename = self.getSiteName(UserUrl)
        if sitename in self.Sitelist: #check if site is supported
            try: #if URL can be opened than is valid
                urllib.request.urlopen(UserUrl) 
                print("URL is valid")
                return True
            except: #if URL cannot be opened this bypass error generation and just tell us link is invalid
                print("URL is invalid or internet is down")
                return False
        else:
            return False

    #Check if system is online
    def InternetVaild(self):
        """! Check if system is online
        @return pingstatus
        """

        response = os.system("ping google.com")
        if response == 0:
            pingstatus = True
            return pingstatus
        else:
            pingstatus = False
            print("Network is down,Please check your internet connection")
            return pingstatus