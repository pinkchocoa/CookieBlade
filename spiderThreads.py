import threading
from queue import Queue
from spider import Spider
from domain import *
from general import *

NUMBER_OF_THREADS = 8
NUMBER_OF_RESULTS = 5
PROJECT_NAME = 'googleNews'
QUEUE_FILE = PROJECT_NAME + '/queue.txt'
CRAWLED_FILE = PROJECT_NAME + '/crawled.txt'
RESULT_FILE = PROJECT_NAME + '/result.txt'
queue = Queue() #create queue for spider threads
alive = True

class MyWorker(threading.Thread):
    def __init__(self):
        super().__init__()
        self.daemon = True
        self.start()
    def run(self):
        global alive
        while alive:
            result_links = file_to_set(RESULT_FILE)
            if len(result_links) >= NUMBER_OF_RESULTS:
                print("enough results")
                alive = False
                break
            url = queue.get()
            Spider.crawl_page(threading.current_thread().name, url)
            queue.task_done()

# Create worker threads (will die when main exits)
def create_workers():
    for x in range(NUMBER_OF_THREADS):
        MyWorker()

# Each queued link is a new job
def create_jobs():
    for link in file_to_set(QUEUE_FILE):
        queue.put(link)
    queue.join()
    crawl()

# Check if there are items in the queue, if so crawl them
def crawl():
    global alive
    queued_links = file_to_set(QUEUE_FILE)

    if alive and len(queued_links) > 0:
        print(str(len(queued_links)) + ' links in the queue')
        create_jobs()

def createSpider(filterList, topic=""):
    HOMEPAGE = 'https://news.google.com/search?q='
    DOMAIN_NAME = get_domain_name(HOMEPAGE)
    SUB_DOMAIN = get_sub_domain_name(HOMEPAGE)
    print(DOMAIN_NAME)
    for word in topic.split():
        HOMEPAGE += word
        HOMEPAGE += "+"
        print (HOMEPAGE)
    
    Spider(PROJECT_NAME, HOMEPAGE, DOMAIN_NAME, SUB_DOMAIN, filterList) #create first spider
    create_workers()
    crawl()
    

createSpider(['articles'], "covid test")
print("test")