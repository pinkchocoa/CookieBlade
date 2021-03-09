# https://docs.python.org/3/library/html.parser.html
from html.parser import HTMLParser
# https://docs.python.org/3/library/urllib.html
from urllib import parse



# this class inherits from HTMLParser
class LinkFinder(HTMLParser):
    def __init__(self, baseUrl, pageUrl):
        super().__init__() # super() calls the init of HTMLParser class
        self.baseUrl = baseUrl
        self.pageUrl = pageUrl
        self.links = set()

    # this overrides the handle_starttag function under HTMLParser
    # example of start tags are <html> <body> <h1> etc... 
    def handle_starttag(self, tag, attrs): 
        #use this to look for a link
        if tag == "a":
            for attribute, value in attrs:
                if attribute == "href":
                    # got to check if it is a full url
                    # or it is a relative link
                    # this function is from urllib, it checks if its relative or not
                    # before joining to make it a full url
                    url = parse.url.join(self.baseUrl, value)
                    self.links.add(url) #add the full url into the set
    
    def getLinks(self):
        return links

    def error(self, message):
        pass
