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
    # any variable that is in a class but outside a method is static
    # static variables
    projectName = ''
    baseUrl = ''
    domainName = ''
    queueFile = ''
    crawledFile = ''
    resultFile = ''
    queue = set()
    crawled = set()
    result = set()
    word = ''

    # __init__ is the constructor name for all classes
    def __init__(self, projectName, baseUrl, domainName, word=''):
        """! Spider class initializer
        @param projectName name of the project, used for directory
        @param baseUrl url of the homepage to be crawled
        @param domainName domain name of the url
        @return an instance of the Spider class initialized with parameters above
        """
        #since these are static variables, gotta use Spider. instead of self.
        Spider.projectName = projectName
        Spider.baseUrl = baseUrl
        Spider.domainName = domainName
        Spider.queueFile = Spider.projectName + '/queue.txt'
        Spider.crawledFile = Spider.projectName + '/crawled.txt'
        Spider.resultFile = Spider.projectName + '/result.txt'
        Spider.word = word
        self.boot()
        self.crawl_page('First spider', Spider.baseUrl)

    # Creates directory and files for project on first run and starts the spider
    @staticmethod
    def boot():
        """! Creates directory and files for project on first run and starts the spider
        """
        create_project_dir(Spider.projectName)
        create_data_files(Spider.projectName, Spider.baseUrl)
        Spider.queue = file_to_set(Spider.queueFile)
        Spider.crawled = file_to_set(Spider.crawledFile)
        Spider.result = file_to_set(Spider.resultFile)

    @staticmethod
    def filter(pageUrl):
        print("filter")
        if Spider.word in pageUrl:
            Spider.result.add(pageUrl)

    # Updates user display, fills queue and updates files
    @staticmethod
    def crawl_page(threadName, pageUrl):
        """! Updates user display, fills queue and updates files
        @param threadName name of the thread 
        @param pageUrl url link
        """
        print("crawl_page")
        # check that it has not already been crawled 
        if pageUrl not in Spider.crawled:
            # print what you are crawling
            print(threadName + ' now crawling ' + pageUrl)
            print('Queue ' + str(len(Spider.queue)) + ' | Crawled  ' + str(len(Spider.crawled)))
            Spider.add_links_to_queue(Spider.gather_links(pageUrl))
            Spider.queue.remove(pageUrl) #done crawling, remove from set
            Spider.crawled.add(pageUrl) #move to crawled
            Spider.filter(pageUrl)
            Spider.update_files()

    # Converts raw response data into readable information and checks for proper html formatting
    @staticmethod
    def gather_links(pageUrl):
        """! Converts raw response data into readable information and checks for proper html formatting
        @param pageUrl url link
        @return a set of links 
        """
        print("gather_links")
        html_string = ''
        try:
            response = urlopen(pageUrl)
            # double check that it is a html file
            if 'text/html' in response.getheader('Content-Type'):
                html_bytes = response.read() # read raw response
                html_string = html_bytes.decode("utf-8") # convert to readable characters
            finder = LinkFinder(Spider.baseUrl, pageUrl) # create link finder object
            finder.feed(html_string)
        except Exception as e:
            print(str(e))
            return set() # return empty set
        return finder.page_links()

    # Saves queue data to project files
    @staticmethod
    def add_links_to_queue(links):
        """! Saves queue data to project files
        @param links
        """
        print("add_links_to_queue")
        for url in links:
            if (url in Spider.queue) or (url in Spider.crawled):
                continue
            # only crawl if url is in the same domain
            if Spider.domainName != get_domain_name(url):
                continue
            Spider.queue.add(url)

    @staticmethod
    def update_files():
        """! update sets to files, saves queued and crawled url into a txt file
        """
        print("update_files")
        set_to_file(Spider.queue, Spider.queueFile)
        set_to_file(Spider.crawled, Spider.crawledFile)
        set_to_file(Spider.result, Spider.resultFile)
        