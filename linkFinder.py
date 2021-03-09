from html.parser import HTMLParser
from urllib import parse

# this class inherits from HTMLParser
class LinkFinder(HTMLParser):

    def __init__(self, base_url, page_url):
        super().__init__() # super() calls the init of HTMLParser class
        self.base_url = base_url
        self.page_url = page_url
        self.links = set()

    # this overrides the handle_starttag function under HTMLParser  
    # example of start tags are <html> <body> <h1> etc... 
    # When we call HTMLParser feed() this function is called when it encounters an opening tag <a>
    def handle_starttag(self, tag, attrs):
        #use this to look for a link
        if tag == 'a':
            for (attribute, value) in attrs:
                if attribute == 'href':
                    # got to check if it is a full url
                    # or it is a relative link
                    # this function is from urllib, it checks if its relative or not
                    # before joining to make it a full url
                    url = parse.urljoin(self.base_url, value)
                    self.links.add(url) #add the full url into the set

    def page_links(self):
        return self.links

    def error(self, message):
        pass