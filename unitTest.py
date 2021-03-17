## @file uniTest.py
#
# @brief this file contain the test methods
#
# @section libraries_main Libraries/Modules
# - All Imports are nesscary to run test.
# - unittest
#   - Allows the running of unittests.

#Imports
import unittest
from database import database
from UrlExtraction import UrlExtraction
from twitterGraph import twitterGraph
from LinkValidation import LinkValidation
from twitter import Twitter,TUser,TTweet
from youtube import *
from domain import get_domain_name,get_sub_domain_name

## Documentation for Testing Class
# The testing class is called and run allowing us to know which function failed.
# Assertion statement is not used due to varying return types.
# Error statement is autogenenrated in the test.
class Testing(unittest.TestCase):
    """! Testing class
    For Testing for class files and running python unit test.
    """
    
    def testDB(self):
        """! Database Test method.
        """
        data = ['Key1','1','2']
        test = database("unitTest")
        test.createTable('test','key','C1','C2')
        test.insertTable(data,'test','key','C1','C2')
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
        getRevenueData("https://www.youtube.com/channel/UCR1IuLEqb6UEA_zQ81kwXfg") #Not working
        getTrendingVideo()
        getDBvids("SG")

    def testUrlExtraction(self):
        """! UrlExtraction Test method.
        """
        test = UrlExtraction()
        test.getUniqueID("https://www.youtube.com/channel/UCOmHUn--16B90oW2L6FRR3A")
        test.getUniqueID("https://twitter.com/BarackObama")
        test.getSiteName("https://www.youtube.com/channel/UCOmHUn--16B90oW2L6FRR3A")
        test.getSiteName("https://twitter.com/BarackObama")
        test.getUniqueID("")
        test.getSiteName("")

    def testTwitterGraph(self):
        """! TwitterGraph Test method.
        """ 
        twitterGraph(1,"https://twitter.com/BarackObama") # Run this if you really need to as API call is slow,

    def testLinkValidation(self):
        """! LinkValidation Test method
        """
        test = LinkValidation()
        test.UrlValidation("https://twitter.com/BarackObama")
        test.InternetVaild()

    def testDomain(self):
        """! Domain Test method.
        """
        get_domain_name("https://twitter.com/BarackObama")
        get_sub_domain_name("https://twitter.com/BarackObama")

if __name__ == '__main__':
    unittest.main()