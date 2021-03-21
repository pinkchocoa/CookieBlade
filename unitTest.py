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
    For Testing for Classes/Methods files and running python unit test.
    """
    
    #Ok
    def test_database_py_mkFolder_py(self):
        """! database.py and mkFolder.py Test
        """
        print("\nSTART of test_database_py_mkFolder_py\n")
        data = [['Key1','1','2'],['key2','1','2']]
        test = database("unitTest") #Invoking this cause the testing of mkFolder class and its methods as well.
        test.createTable('test','key','C1','C2')
        for x in range(len(data)):
            test.insertTable(data[x],'test','key','C1','C2')
        test.getTableData('test')

        #Exception testing
        test.createTable()
        test.insertTable(data)
        test.getTableData("")

        print("\nEND of test_database_py_mkFolder_py\n")

    #Ok
    def test_domain_py(self):
        """! Domain.py Test
        """
        print("\nSTART of test_domain_py\n")

        get_domain_name("https://twitter.com/BarackObama")
        get_sub_domain_name("https://twitter.com/BarackObama")

        print("\nEND of test_domain_py\n")

    #Ok
    def test_general_py(self):
        """! general.py Test
        """
        print("\nSTART of test_general_py\n")

        create_project_dir('testGeneral')
        create_file('testResult.txt')
        write_file('./testGeneral/queue.txt','test')
        append_to_file('./testGeneral/queue.txt', 'test')
        file_to_set('./testGeneral/queue.txt')
        set_to_file('https://twitter.com/BarackObama', './testGeneral/queue.txt')
        delete_file_contents('./testGeneral/queue.txt')

        print("\nEND of test_general_py\n")

    #Empty - Test by running main.py, Part of Ui
    def test_GUIWidegets_py(self):
        pass

    #Ok
    def test_LinkValidation_py(self):
        """! LinkValidation.py Test
        """
        print("\nSTART of test_LinkValidation_py\n")

        test = LinkValidation()
        test.UrlValidation("https://twitter.com/BarackObama")
        test.InternetVaild()

        print("\nEND of test_LinkValidation_py\n")

    #Empty - Test by running main.py. Main Program file.
    def test_main_py(self):
        pass

    #Ok: All class and methods in singleSpider.py,pider.py & linkFinder.py are fully covered within this test.
    def test_singleSpider_py_spider_py_linkFinder_py(self):
        """! singleSpider.py, spider.py & linkFinder.py Test
        """
        print("\nSTART of test_singleSpider_py_spider_py\n")

        #This also invokes spider.py & linkFinder.py.
        spidey(['articles'],"covid test", 3)

        print("\nEND of test_singleSpider_py_spider_py\n")

    #Ok
    def test_twitter_py(self):
        """! twitter.py Test
        """
        print("\nSTART of test_twitter_py\n")

        test = Twitter()
        test.searchKeyword("Obama")
        test.trendingTopics()

        test = TUser("BarackObama")
        test.byID("BarackObama")
        test.byURL("https://twitter.com/BarackObama")
        test.followCount()
        test.tweetCount()
        test.userLoc()
        test.userFav()
        test.userTweets(1)

        test = TTweet("1371568939042537473")
        test.byID("1371568939042537473")
        test.byURL("https://twitter.com/BarackObama/status/1371568939042537473")
        test.favCount()
        test.RTCount()
        test.loc()
        test.getDate()

        print("\nEND of test_twitter_py\n")

    #Ok
    def test_twitterGraph_py_twitterDB_py(self):
        """! TwitterGraph.py & TwitterDB.py Test
        """ 
        print("\nSTART of test_twitterGraph_py_twitterDB_py\n")

        #twitterTrend() also invoke t.trendingTopics() and setTwitterTrendDB()
        twitterTrend()

        #twitterGraph() also invoke setTwitterGraphDB() and checkTableTwitterGraph()
        twitterGraph(10,"https://twitter.com/BarackObama")
        
        getTwitterGraphDB("https://twitter.com/BarackObama")
        getTwitterTrendDB()
        
        print("\nEND of test_twitterGraph_py_twitterDB_py\n")

    #Ok
    def test_UrlExtraction_py(self):
        """! UrlExtraction.py Test
        """
        print("\nSTART of test_UrlExtraction_py\n")

        test = UrlExtraction()
        test.getUniqueID("https://www.youtube.com/channel/UCR1IuLEqb6UEA_zQ81kwXfg")
        test.getUniqueID("https://twitter.com/BarackObama")
        test.getSiteName("https://www.youtube.com/channel/UCR1IuLEqb6UEA_zQ81kwXfg")
        test.getSiteName("https://twitter.com/BarackObama")
        test.getUniqueID("")
        test.getSiteName("")

        print("\nEND of test_UrlExtraction_py\n")

    #Empty - Test by running main.py, Part of Ui
    def test_window_py(self):
        pass

    #Empty - Test by running main.py, Part of Ui
    def test_windowGen_py(self):
        pass

    #Ok: All class and methods in youtubeGraph.py and youtube.py are fully covered within this test.
    def test_youtubeGraph_py_youtube_py(self):
        """! youtubeGraph.py & youtube.py Test
        """
        print("\nSTART of test_youtubeGraph_py_youtube_py\n")

        #This also invokes youtube.py:
        #Class: Channel() 
        #Methods: Channel.searchurl()
        setYoutubeChannelStats("https://www.youtube.com/channel/UCR1IuLEqb6UEA_zQ81kwXfg")
        
        #This also invokes database.py and its related class and methods.
        getYoutubeChannelStats("https://www.youtube.com/channel/UCR1IuLEqb6UEA_zQ81kwXfg")
        
        #This also invokes youtube.py:
        #Class: youtubeVid(),YouTube() 
        #Methods: youtubeVid.getTrendingVideo(), youtubeVid.getDBvids() 
        #youtubeVid.scrapData(), youtubeVid.vidInfo(), youtubeVid.getDict()
        getYoutubeTrends("SG")

        #This also invokes youtube.py: 
        #Class: Channel()
        #Methods: Channel.getRevenueData()
        #This easily caps API limit so it is omitted as we tested it once.
        setRevenueData("https://www.youtube.com/channel/UCR1IuLEqb6UEA_zQ81kwXfg")
        
        #This also invokes database.py and its related class and methods.
        getRevenueData("https://www.youtube.com/channel/UCR1IuLEqb6UEA_zQ81kwXfg")
        
        print("\nEND of test_youtubeGraph_py_youtube_py\n")

#To be removed/Unused files:
# spiderThreads.py - Kept for reference. Test not needed.


if __name__ == '__main__':
    unittest.main()