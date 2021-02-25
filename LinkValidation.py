import os
import subprocess
import urllib.request
from UrlExtraction import UrlExtraction

#Link validation

class LinkValidation(UrlExtraction):

    #do i even need this?
    def __init__(self):
        self.Sitelist = ["facebook", "youtube", "twitter", "reddit", "instagram"] #list needs to appended to add support to sites.
    
    #Check if URL is valid
    def UrlValidation(self, UserUrl):
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
    #ENDOFMETHOD

    #Check if system is online #might get rid if this?
    def InternetVaild(self):
        response = os.system("ping google.com")
        if response == 0:
            pingstatus = True
            return pingstatus
        else:
            pingstatus = False
            print("Network is down,Please check your internet connection")
            return pingstatus
    #ENDOFMETHOD