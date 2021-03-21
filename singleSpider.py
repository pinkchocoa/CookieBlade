from queue import Queue
from spider import Spider
from domain import *
from general import *

PROJECT_NAME = 'googleNews'
RESULT_FILE = 'result.txt'

class spiderWorker:
    alive = True
    def __init__(self, filterList, topic=""):
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
        self.create_jobs()
        self.work()

    # Each queued link is a new job
    def create_jobs(self):
        #print("create_jobs")
        for link in self.spidey.queue:
            self.queue.put(link)
        pass

    def work(self):
        #print("work")
        url = self.queue.get()
        self.spidey.crawl_page("1", url)

def spidey(filterList="", topic="", numResults=3):
    print("crawling")

    topic = topic.replace("#", "")
    topic = topic.encode('ascii', 'ignore').decode()
    print("topic: ", topic)

    x = spiderWorker(filterList,topic)
    while len(x.spidey.result) < numResults:
        x.create_workers()

    create_file(RESULT_FILE)
    delete_file_contents(RESULT_FILE)
    set_to_file(x.spidey.result, RESULT_FILE)
    
    return x.spidey.result

#print(spidey(['articles'],"covid test", 3))
#print("again")
#print(spidey(['articles'],"SeninleyizErdoğan", 3))
#print("test")