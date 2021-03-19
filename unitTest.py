## @file uniTest.py
#
# @brief this file contain the test methods for unit testing
#
# @section libraries_main Libraries/Modules
# - All Imports are nesscary to run test.
# - unittest
#   - Allows the running of unittests.
# - import *
#   - this allow check of which method or class has not been check as it will be highlighted if unused.

#Imports
import unittest
from database import *
from UrlExtraction import *
from twitterGraph import *
from LinkValidation import *
from twitter import *
from youtube import *
from domain import *
from twitterDB import *
from general import *
from getLinks import *
from linkFinder import *
from youtubeGraph import *
from singleSpider import *
from spider import *

## Documentation for Testing Class
# The testing class is called and run allowing us to know which function failed.
# Assertion statement is not used for some due to varying return types.
# Error statement is autogenenrated in the test.
class Testing(unittest.TestCase):
    """! Testing class
    For Testing for class files and running python unit test.
    """
    
    def testDataBase(self):
        """! Database Test method.
        """
        data = [['Key1','1','2'],['key2','1','2']]
        test = database("unitTest")
        test.createTable('test','key','C1','C2')
        for x in range(len(data)):
            test.insertTable(data[x],'test','key','C1','C2')
        test.getTableData('test')

    def testTwitter(self):
        """! twitter crawler Test method.
        """
        test = Twitter()
        test.searchKeyword("Obama")
        test.trendingTopics()

        test = TUser("BarackObama")
        test.byID("BarackObama")
        test.byURL("https://twitter.com/BarackObama")
        test.followCount()
        test.tweetCount()
        test.userLoc()
        test.recentFollows()
        test.recentFriends()
        test.userFav()
        test.userTweets(1)

        test = TTweet("1371568939042537473")
        test.byID("1371568939042537473")
        test.byURL("https://twitter.com/BarackObama/status/1371568939042537473")
        test.favCount()
        test.RTCount()
        test.loc()
        test.getDate()

    def testYoutube(self):
        """! Youtube crawler Test method.
        """
        getChannelStats("https://www.youtube.com/channel/UCR1IuLEqb6UEA_zQ81kwXfg")
        getRevenueData("https://www.youtube.com/channel/UCR1IuLEqb6UEA_zQ81kwXfg")
        getTrendingVideo()
        getDBvids("SG")

    def testUrlExtraction(self):
        """! UrlExtraction Test method.
        """
        test = UrlExtraction()
        test.getUniqueID("https://www.youtube.com/channel/UCR1IuLEqb6UEA_zQ81kwXfg")
        test.getUniqueID("https://twitter.com/BarackObama")
        test.getSiteName("https://www.youtube.com/channel/UCR1IuLEqb6UEA_zQ81kwXfg")
        test.getSiteName("https://twitter.com/BarackObama")
        test.getUniqueID("")
        test.getSiteName("")

    def testTwitterGraphandDB(self):
        """! TwitterGraph and TwitterDB Test method.
        """ 
        twitterGraph(10,"https://twitter.com/BarackObama")
        getTwitterGraphDB("https://twitter.com/BarackObama")

    def testLinkValidation(self):
        """! LinkValidation Test method
        """
        test = LinkValidation()
        test.UrlValidation("https://twitter.com/BarackObama")
        test.InternetVaild()

    def testDomain(self):
        """! Domain Test method.
        """
        assert get_domain_name("https://twitter.com/BarackObama")
        assert get_sub_domain_name("https://twitter.com/BarackObama")

    def testGeneral(self):
        data = [1,2,3]
        create_project_dir('testGeneral')
        create_data_files('testGeneral', 'www.google.com')
        create_file('./testGeneral')
        write_file('./testGeneral/queue.txt',data)
        append_to_file('./testGeneral/queue.txt', data)
        file_to_set('./testGeneral/queue.txt')
        set_to_file('https://twitter.com/BarackObama', './testGeneral/queue.txt')
        delete_file_contents('./testGeneral/queue.txt')

    def testGetLinks(self):
        test = LinkFinder('https://www.raspberrypi.org','https://www.raspberrypi.org/documentation/configuration/wireless/wireless-cli.md')
        test.handle_starttag("a","href")
        test.getLinks()
        test.error("Unit Test")

    def testLinkFinder(self):
        test = LinkFinder('https://www.raspberrypi.org','https://www.raspberrypi.org/documentation/configuration/wireless/wireless-cli.md')
        test.handle_starttag("a","href")
        test.getLinks()
        test.error("Unit Test")

    def testYoutubeGraph(self):
        setYoutubeChannelStats("https://www.youtube.com/channel/UCR1IuLEqb6UEA_zQ81kwXfg")
        getYoutubeChannelStats("https://www.youtube.com/channel/UCR1IuLEqb6UEA_zQ81kwXfg")
        setYoutubeChannelRevenue("https://www.youtube.com/channel/UCR1IuLEqb6UEA_zQ81kwXfg")
        getYoutubeChannelRevenue("https://www.youtube.com/channel/UCR1IuLEqb6UEA_zQ81kwXfg")

    def testSingleSpiderandSpider(self):
        spidey(['articles'],"covid test", 3) #This use the spiderWorker and Spider class as well.

if __name__ == '__main__':
    unittest.main()