from queue import Queue
from spider import Spider
from domain import *
from general import *


class spiderWorker:
    NUMBER_OF_THREADS = 1
    NUMBER_OF_RESULTS = 3
    PROJECT_NAME = 'googleNews'
    QUEUE_FILE = PROJECT_NAME + '/queue.txt'
    CRAWLED_FILE = PROJECT_NAME + '/crawled.txt'
    RESULT_FILE = PROJECT_NAME + '/result.txt'
    queue = Queue() #create queue for spider threads
    alive = True
    def __init__(self, filterList, topic=""):
        HOMEPAGE = 'https://news.google.com/search?q='
        DOMAIN_NAME = get_domain_name(HOMEPAGE)
        SUB_DOMAIN = get_sub_domain_name(HOMEPAGE)
        print(DOMAIN_NAME)
        for word in topic.split():
            HOMEPAGE += word
            HOMEPAGE += "+"
            print (HOMEPAGE)
        
        Spider(self.PROJECT_NAME, HOMEPAGE, DOMAIN_NAME, SUB_DOMAIN, filterList) #create first spider
        self.create_workers()
        print("end init")

    def create_workers(self):
        self.create_jobs()
        self.work()

    # Each queued link is a new job
    def create_jobs(self):
        print("create_jobs")
        for link in file_to_set(self.QUEUE_FILE):
            self.queue.put(link)

    def work(self):
        print("work")
        url = self.queue.get()
        Spider.crawl_page("1", url)
    
spiderWorker(['articles'], "covid test")
print("test")