## @file spider.py
#
# @brief this file contains the spider class
#
# @section libraries_main Libraries/Modules
# - urllib.request standard library (https://docs.python.org/3/library/urllib.request.html)
#   - access to urlopen function
# - linkFinder (local) 
#   - access to LinkFinder class
# - domain (local)
#   - access to get_domain_name and get_sub_domainName functions
# - general (local)
#   - access to functions used for file i/o

# Imports
from urllib.request import urlopen
from linkFinder import LinkFinder
from domain import *
from general import *

## Documentation for a Spider Class
# spider grabs a link from the queue, crawl, then dump the link into crawled
# we can make many spiders to make it faster
# but to prevent dupes crawl, we use the same queue/crawl file
class Spider:
    """! Spider class
    Defines the spider object used to crawl through webpages.
    """
    # __init__ is the constructor name for all classes
    def __init__(self, projectName, baseUrl, domainName, subDomain = '', word=[]):
        """! Spider class initializer
        @param projectName name of the project, used for directory
        @param baseUrl url of the homepage to be crawled
        @param domainName domain name of the url
        """
        #since these are static variables, gotta use Spider. instead of self.

        self.queue = set()
        self.crawled = set()
        self.result = set()
        self.projectName = projectName
        self.baseUrl = baseUrl
        self.domainName = domainName
        self.subDomain = subDomain
        #self.queueFile = self.projectName + '/queue.txt'
        #self.crawledFile = self.projectName + '/crawled.txt'
        #self.resultFile = self.projectName + '/result.txt'
        self.word = word
        self.boot()
        self.crawl_page('First spider', self.baseUrl)

    # Creates directory and files for project on first run and starts the spider
    def boot(self):
        """! Creates directory and files for project on first run and starts the spider
        """
        #create_project_dir(self.projectName)
        #create_data_files(self.projectName, self.baseUrl)
        #self.queue = file_to_set(self.queueFile)
        #self.crawled = file_to_set(self.crawledFile)
        #self.result = file_to_set(self.resultFile)
        self.add_links_to_queue([self.baseUrl])

    def filter(self, pageUrl):
        #print("filter")
        test = 0
        for x in self.word:
            if x in pageUrl:
                continue
            else:
                test = 1
        if test == 0:
            self.result.add(pageUrl)

    # Updates user display, fills queue and updates files
    def crawl_page(self, threadName, pageUrl):
        """! Updates user display, fills queue and updates files
        @param threadName name of the thread 
        @param pageUrl url link
        """
        # check that it has not already been crawled 
        if pageUrl not in self.crawled:
            # print what you are crawling
            #print(threadName + ' now crawling ' + pageUrl)
            #print('Queue ' + str(len(Spider.queue)) + ' | Crawled  ' + str(len(Spider.crawled)))
            self.add_links_to_queue(self.gather_links(pageUrl))
            self.queue.remove(pageUrl) #done crawling, remove from set
            self.crawled.add(pageUrl) #move to crawled
            self.filter(pageUrl)
            #self.update_files()

    # Converts raw response data into readable information and checks for proper html formatting
    def gather_links(self, pageUrl):
        """! Converts raw response data into readable information and checks for proper html formatting
        @param pageUrl url link
        @return a set of links 
        """
        #print("gather_links")
        html_string = ''
        try:
            response = urlopen(pageUrl)
            # double check that it is a html file
            if 'text/html' in response.getheader('Content-Type'):
                html_bytes = response.read() # read raw response
                html_string = html_bytes.decode("utf-8") # convert to readable characters
            finder = LinkFinder(self.baseUrl, pageUrl) # create link finder object
            finder.feed(html_string)
        except Exception as e:
            print(str(e))
            return set() # return empty set
        return finder.page_links()

    # Saves queue data to project files
    def add_links_to_queue(self, links):
        """! Saves queue data to project files
        @param links
        """
        #print("add_links_to_queue")
        for url in links:
            if (url in self.queue) or (url in self.crawled):
                continue
            # only crawl if url is in the same domain
            if self.domainName != get_domain_name(url):
                continue
            if self.subDomain not in url:
                continue
            self.queue.add(url)

    def update_files(self):
        """! update sets to files, saves queued and crawled url into a txt file
        """
        #print("update_files")
        set_to_file(self.queue, self.queueFile)
        set_to_file(self.crawled, self.crawledFile)
        set_to_file(self.result, self.resultFile)
        
