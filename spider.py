from urllib.request import urlopen
from getLinks import LinkFinder
from fileIO import *



# spider grabs a link from the queue, crawl, then dump the link into crawled
# we can make many spiders to make it faster
# but to prevent dupes crawl, we use the same queue/crawl file
class Spider:

    # any variable that is in a class but outside a method is static
    # static variables
    projName = ""
    baseUrl = ""
    domainName = ""
    queueFile = ""
    crawledFile = ""
    queue = set()
    crawled = set()

    # __init__ is the constructor name for all classes
    def __init__(self, projName, baseUrl, domainName):
        #since these are static variables, gotta use Spider. instead of self.
        Spider.projName = projName
        Spider.baseUrl = baseUrl
        Spider.domainName = domainName
        Spider.queueFile = projName + "/queue.txt"
        Spider.crawledFile = projName + "/crawled.txt"

        self.boot()
        self.crawlPage("first", Spider.baseUrl)
    
    # this is to declare static method
    @staticmethod
    def boot():
        # first spider's job to create directories
        createDir(Spider.projName)
        createCrawlQueue(Spider.projName, Spider.baseUrl)
        Spider.queue = fileToSet(queueFile)
        Spider.crawled = fileToSet(crawledFile)

    @staticmethod
    def updateFiles():
        setToFile(queue, queueFile)
        setToFile(crawled, crawledFile)

    def crawlPage(threadName, pageUrl):
        # check that it has not already been crawled 
        if pageUrl not in Spider.crawled:
            # print what you are crawling
            print(theadName + "crawling" + pageUrl)
            print("Links queued: " + str(len(Spider.queue)) + "| Links crawled: " + str(len(Spider.crawled)))
            Spider.addToQueue(Spider.getLinks(pageUrl) )
            Spider.queue.remove(pageUrl) #done crawling, remove from set
            Spider.crawled.add(pageUrl) #move to crawled
            Spider.updateFiles()


