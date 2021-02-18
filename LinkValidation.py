import os
import urllib.request

#Link validation

class LinkValidation:

    def __init__(self, URL):
        self.URL = URL
    
    #Check if URL is valid #Full URL is required including https://www.<site>.<com/org>
    def UrlValidation(self):
        try: #if URL can be opened than is valid
            urllib.request.urlopen(self.URL) 
            print("URL is valid")
            return True
        except: #if URL cannot be opened this bypass error generation and just tell us link is invalid
            print("URL is invalid")
            return False

    #Check if system is online
    def InternetVaild(self):
        response = os.system("ping google.com")
        if response == 0:
            pingstatus = True
            
        else:
            pingstatus = False
            print("Network is down,Please check your internet connection")
            
        return pingstatus

#testing
#urlCheck = LinkValidation("https://www.youtube.com/user/PewDiePie")
#urlCheck.InternetVaild()
#urlCheck.UrlValidation()
