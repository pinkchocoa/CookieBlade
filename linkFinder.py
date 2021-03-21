## @file linkFinder.py
#
# @brief this file contains the the general functions used for filo i/o purposes
#
# @author Jodie
#
# @section libraries_main Libraries/Modules
# - html.parser standard library (https://docs.python.org/3/library/html.parser.html)
#   - access to HTMLParser class
# - urllib standard library (https://docs.python.org/3/library/urllib.html)
#   - access to parse function

# Imports
from html.parser import HTMLParser
from urllib import parse

## Documentation for a LinkFinder Class
# this class looks for links in a bunch of HTML
# this class inherits from HTMLParser
class LinkFinder(HTMLParser):
    """! LinkFinder class
    this class looks for links in a bunch of HTML
    """
    def __init__(self, base_url, page_url):
        """! LinkFinder class initializer
        @param base_url base url
        @param page_url page url
        """
        super().__init__() # super() calls the init of HTMLParser class
        self.base_url = base_url
        self.page_url = page_url
        self.links = set()

    # this overrides the handle_starttag function under HTMLParser  
    # example of start tags are <html> <body> <h1> etc... 
    # When we call HTMLParser feed() this function is called when it encounters an opening tag <a>
    def handle_starttag(self, tag, attrs):
        """! this overrides the handle_starttag function under HTMLParser  
        example of start tags are <html> <body> <h1> etc... 
        When we call HTMLParser feed() this function is called when it encounters an opening tag <a>
        @param tag html tags
        @param attrs html attributes
        """
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
        """! this returns links that are parsed
        @return parsed links
        """
        return self.links

    def error(self, message):
        """! prints error message
        """
        print(message)
        pass