from fileIO import *

# each website crawlled is a seperate project/folder

# description:
# create a queue of links to crawl
def createCrawlQueue(name, baseUrl):
    #file path to store the queue
    queue = name + "/queue.txt"
    #file path to store crawled
    crawled = name + "/crawled.txt"

    if not fileExist(queue):
        writeNewFile(queue, baseUrl)
    else:
        appendFile(queue, baseUrl)
    if not fileExist(crawled):
        writeNewFile(crawled, "")



