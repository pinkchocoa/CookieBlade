import threading
from queue import Queue
from spider import Spider
from domain import *
from general import *
from twitter import *

PROJECT_NAME = 'reddit'
HOMEPAGE = 'https://www.reddit.com/'
DOMAIN_NAME = get_domain_name(HOMEPAGE)
QUEUE_FILE = PROJECT_NAME + '/queue.txt'
CRAWLED_FILE = PROJECT_NAME + '/crawled.txt'
NUMBER_OF_THREADS = 8

# Create worker threads (will die when main exits)
def create_workers():
    for _ in range(NUMBER_OF_THREADS):
        t = threading.Thread(target=work)
        t.daemon = True
        t.start()


# Do the next job in the queue
def work():
    while True:
        url = queue.get()
        Spider.crawl_page(threading.current_thread().name, url)
        queue.task_done()


# Each queued link is a new job
def create_jobs():
    for link in file_to_set(QUEUE_FILE):
        queue.put(link)
    queue.join()
    crawl()


# Check if there are items in the queue, if so crawl them
def crawl():
    queued_links = file_to_set(QUEUE_FILE)

    if len(queued_links) > 0:
        print(str(len(queued_links)) + ' links in the queue')
        create_jobs()


#queue = Queue() #create queue for spider threads
#Spider(PROJECT_NAME, HOMEPAGE, DOMAIN_NAME) #create first spider
#create_workers()
#crawl()

#twitter test

def testTweet():
    #tTweet = TTweet(1360670340934815750)
    tTweet = TTweet.byURL("https://twitter.com/twitter/statuses/1360670340934815750")
    print(tTweet.favCount())
    print(tTweet.RTCount())
    print(tTweet.loc())

def testUser():
    #tUser = TUser("LilyPichu")
    tUser = TUser.byURL("https://twitter.com/LilyPichu")
    print(tUser.tweetCount())
    print(tUser.followCount())

print("twitter test")
#t = Twitter()
#testTweet()
testUser()

#print(t.followCount("pinkchocoa"))
#print(t.followCount("LilyPichu"))
#print(t.searchKeyword("MAMAMOO"))
