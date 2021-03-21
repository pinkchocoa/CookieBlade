## @file singleSpider.py
#
# @brief this file contains the spiderWorker class
#
# @author Jodie
#
# @section libraries_main Libraries/Modules
# - queue standard library
#   - access to Queue data structure
# - spider (local)
#   - access to spider for crawling sites
# - domain (local)
#   - access to functions to extract domain names
# - general (local)
#   - access to generic file i/o 

# Import
from queue import Queue
from spider import Spider
from domain import *
from general import *

PROJECT_NAME = 'googleNews'
RESULT_FILE = 'result.txt'

## Documentation for a spiderWorker Class
# spiderWorker is a worker that crawls web pages
class spiderWorker:
    def __init__(self, filterList, topic=""):
        """! spiderWorker class initializer
        @param filterList filters for websites
        @param topic topic to crawl for
        """
        self.queue = Queue() #create queue for spider threads
        HOMEPAGE = 'https://news.google.com/search?q='
        DOMAIN_NAME = get_domain_name(HOMEPAGE)
        SUB_DOMAIN = get_sub_domain_name(HOMEPAGE)
        print(DOMAIN_NAME)
        for word in topic.split():
            HOMEPAGE += word
            HOMEPAGE += "+"
            print (HOMEPAGE)
        self.spidey = Spider(PROJECT_NAME, HOMEPAGE, DOMAIN_NAME, SUB_DOMAIN, filterList) #create first spider
        self.create_workers()
        #print("end init")

    def create_workers(self):
        """! starts the crawling process
        """
        self.create_jobs()
        self.work()

    # Each queued link is a new job
    def create_jobs(self):
        """! creates jobs for the worker by lining them up in a queue
        """
        #print("create_jobs")
        for link in self.spidey.queue:
            self.queue.put(link)
        pass

    def work(self):
        """! crawl site
        """
        #print("work")
        url = self.queue.get()
        self.spidey.crawl_page("1", url)

def spidey(filterList="", topic="", numResults=3):
    """! spidey creates a spider for you
    @param filterList filters for websites
    @param topic topic to crawl for
    @param numResutlts number of links to get
    @return set of links
    """
    topic = topic.replace("#", "")
    topic = topic.encode('ascii', 'ignore').decode()

    x = spiderWorker(filterList,topic)
    while len(x.spidey.result) < numResults:
        x.create_workers()

    create_file(RESULT_FILE)
    delete_file_contents(RESULT_FILE)
    set_to_file(x.spidey.result, RESULT_FILE)
    
    return x.spidey.result
