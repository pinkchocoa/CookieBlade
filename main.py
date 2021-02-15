import threading
from queue import Queue
from general import *
from spider import Spider
from domain import *

# main
#defines
PROJECT_NAME = "twitter"
HOMEPAGE = "https://google.com"
DOMAIN_NAME = extractDomainName(HOMEPAGE)
QUEUE_FILE = PROJECT_NAME + "/queue.txt"
CRAWLED_FILE = PROJECT_NAME + "/crawled.txt"
NUM_OF_THREADS = 8

threadQueue = Queue()
Spider(PROJECT_NAME, HOMEPAGE, DOMAIN_NAME)


print("start of codes")


print("end of codes")
#end of main