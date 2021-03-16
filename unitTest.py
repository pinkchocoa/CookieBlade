
import unittest
from database import database
from UrlExtraction import UrlExtraction
from twitterGraph import twitterGraph
from LinkValidation import LinkValidation
from twitter import Twitter,TUser,TTweet
from youtube import *


class Testing(unittest.TestCase):

    # def test_string(self):
    #     a = 'some'
    #     b = 'some'
    #     self.assertEqual(a, b)

    # def test_boolean(self):
    #     a = True
    #     b = True
    #     self.assertEqual(a, b)
    
    def testDB(self): #includes mkfolder class methods
        data = ['Key1','1','2']
        test = database("unitTest")
        test.createTable('test','key','C1','C2')
        test.insertTable(data,'test','key','C1','C2')
        test.getTableData('test')

    def testTwitter(self):
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
        pass

    def testUrlExtraction(self):
        test = UrlExtraction()
        test.getUniqueID("https://www.youtube.com/channel/UCOmHUn--16B90oW2L6FRR3A")
        test.getUniqueID("https://twitter.com/BarackObama")
        test.getSiteName("https://www.youtube.com/channel/UCOmHUn--16B90oW2L6FRR3A")
        test.getSiteName("https://twitter.com/BarackObama")
        test.getUniqueID("")
        test.getSiteName("")

    def testTwitterGraph(self): #Testing method.
        #twitterGraph(1,"https://twitter.com/BarackObama") - Run this if you really need to as API call is slow,
        pass

    def testLinkValidation(self):
        test = LinkValidation()
        test.UrlValidation("https://twitter.com/BarackObama")
        #test.InternetVaild() - This takes awhile as well.


if __name__ == '__main__':
    unittest.main()