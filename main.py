import os

# each website crawlled is a seperate project/folder

def fileExist(filename):
    if not os.path.exists(filename):
        return False
    return True

# function name: createDir
# parameters: directory
#               directory path
# return value: 
# description: if directory does not exist, create
def createDir(directory):
    #if directory does not exist, create
    if not fileExist(directory):
        print("Creating " + directory)
        os.mkdir(directory)
        
def writeNewFile(filename, data):
    f = open(filename, 'w') #open and write file
    f.write(data)
    f.close()

def appendFile(filename, data):
    with open(filename, 'a') as file: #open the file as a stream
        file.write(data + "\n")

def deleteContents(filename):
    with open(filename, 'w'):
        pass # write nothing into the file (therefore replaces contents)

def createCrawlQueue(name, base_url):
    #file path to store the queue
    queue = name + "/queue.txt"
    #file path to store crawled
    crawled = name + "/crawled.txt"

    if not fileExist(queue):
        writeNewFile(queue, base_url)
    if not fileExist(crawled):
        writeNewFile(crawled, "")


# main
print("start of codes")
createDir("test")
createCrawlQueue("test", "test.com")
deleteContents("test/queue.txt")

print("end of codes")