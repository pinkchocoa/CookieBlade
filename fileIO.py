import os

#file i/o 

# description:
# returns true if file exists, false if file does not exist
def fileExist(filename):
    return os.path.exists(filename)

# description: 
# if directory does not exist, create
def createDir(directory):
    if not fileExist(directory):
        print("Creating " + directory)
        os.mkdir(directory)

# description: 
# open and write file
def writeNewFile(filename, data):
    f = open(filename, 'w') # 'w' for write
    f.write(data)
    f.close()

# description:
# open the file as a stream and write to it
def appendFile(filename, data):
    with open(filename, 'a') as file: # 'a' for append
        file.write(data + "\n")

# description:
# delete contents in file
def deleteContents(filename):
    with open(filename, 'w'):
        pass # write nothing into the file (therefore replaces contents)

# description:
# create data storage for links to queue/crawl
def createCrawlQueue(name, baseUrl):
    #file path to store the queue
    queue = name + "/queue.txt"
    #file path to store crawled
    crawled = name + "/crawled.txt"

    if not fileExist(queue):
        writeNewFile(queue, baseUrl)
    if not fileExist(crawled):
        writeNewFile(crawled, "")

# description:
# use sets to prevent duplicates
def fileToSet(filename):
    results = set()
    with open(filename, 'rt') as f:
        for line in f:
            results.add(line.replace('\n', '')) # remove new line character
    return results

# description:
# convert set to file for saving
def setToFile(setname, filename):
    deleteContents(filename)
    for x in sorted(setname):
        appendFile(filename, x)

#end of file i/o