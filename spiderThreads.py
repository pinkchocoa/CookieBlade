import threading
from queue import Queue
from spider import Spider
from domain import *
from general import *

class spiderWorker():
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
        self.crawl()
        print("end init")

    class SpiderThread(threading.Thread):
        def __init__(self, outerClass):
            super().__init__()
            self.outerClass = outerClass
            self.daemon = True
            self.start()
        def run(self):
            while self.outerClass.alive:
                result_links = file_to_set(self.outerClass.RESULT_FILE)
                if len(result_links) >= self.outerClass.NUMBER_OF_RESULTS:
                    print("enough results")
                    self.outerClass.alive = False
                    break
                url = self.outerClass.queue.get()
                Spider.crawl_page(threading.current_thread().name, url)
                self.outerClass.queue.task_done()
            

    # Create worker threads (will die when main exits)
    def create_workers(self):
        print("create_workers")
        for x in range(self.NUMBER_OF_THREADS):
            spiderWorker.SpiderThread(self)

    # Each queued link is a new job
    def create_jobs(self):
        print("create_jobs")
        for link in file_to_set(self.QUEUE_FILE):
            self.queue.put(link)
        self.queue.join()
        if self.alive:
            crawl()

    # Check if there are items in the queue, if so crawl them
    def crawl(self):
        print("crawl")
        queued_links = file_to_set(self.QUEUE_FILE)

        if self.alive and len(queued_links) > 0:
            print(str(len(queued_links)) + ' links in the queue')
            self.create_jobs()
        else:
            self.queue = Queue()

spiderWorker(['articles'], "covid test")
print("test")
print("test")
print("test")