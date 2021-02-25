import sqlite3
import datetime
from mkFolder import mkFolder

#Database manipulation. #Database is stored locally.
class database(mkFolder):


    #Get current data Format: Year/Month/Day
    def getDate(self):
        date = datetime.date.today()
        return str(date) #for database text format.
    #ENDOFMETHOD

    #create DB based on Social media sites.
    def createDB(self, UserUrl):
        sitename = self.getSiteName(UserUrl)
        self.createDirectory()
        arg = './data/' + sitename + '.db'
        db = sqlite3.connect(arg)
        db.close()
        return arg #return database location
    #ENDOFMETHOD

    #create table for youtube uid #can extend for more data if need to.
    def createYoutubeTable(self, UserUrl):
        arg = self.createDB(UserUrl)
        uid = self.getUniqueID(UserUrl)
        connect = sqlite3.connect(arg)
        db = connect.cursor()
        #append this string argument to increase data type in table.
        tableArg = 'CREATE TABLE ' + 'IF NOT EXISTS ' + uid + '(' + 'Date text PRIMARY KEY, ' + 'totalViews interger, ' + 'totalSubs interger' + ')'
        db.execute(tableArg)
        #Create Unqiue index for replace function of SQLite3
        tableArg = 'CREATE UNIQUE INDEX ' + 'IF NOT EXISTS ' + 'idx_' + uid + '_Date ON ' + uid +' (Date)'
        db.execute(tableArg)
        #save the database
        connect.commit()
        db.close()
    #ENDOFMETHOD

    #create table for twitter #can extend for more data if need to.
    def createTiwitterTable(self, UserUrl):
        arg = self.createDB(UserUrl)
        uid = self.getUniqueID(UserUrl)
        connect = sqlite3.connect(arg)
        db = connect.cursor()

        #append this string argument to increase data type in table.
        tableArg = 'CREATE TABLE ' + 'IF NOT EXISTS ' + uid + '(' + 'Date text PRIMARY KEY, ' + 'followersCount interger, ' + 'tweetCount interger' + ')'
        db.execute(tableArg)

        #Create Unqiue index for replace function of SQLite3
        tableArg = 'CREATE UNIQUE INDEX ' + 'IF NOT EXISTS ' + 'idx_' + uid + '_Date ON ' + uid +' (Date)'
        db.execute(tableArg)

        #save the database
        connect.commit()
        db.close()
    #ENDOFMETHOD

    #Insert data into youtube type database #data pass has to follow table coloum format
    def insertYoutubeDB(self, UserUrl, data):
        arg = self.createDB(UserUrl)
        uid = self.getUniqueID(UserUrl)
        self.createYoutubeTable(UserUrl)
        connect = sqlite3.connect(arg)
        db = connect.cursor()

        #append this string if need to support more data
        #increase '?' marks for more data REPLACE function automatically overwrite exisit entries of same dates
        tableArg = 'REPLACE INTO ' + uid + ' (Date, totalViews, totalSubs) VALUES (?, ?, ?)'

        #add data[] to this line for more data support
        db.execute(tableArg,(self.getDate(), data[0], data[1]))

        #save the database.
        connect.commit()
        db.close
    #ENDOFMETHOD

    #Insert data into youtube type database #data pass has to follow table coloum format
    def insertTwitterDB(self, UserUrl, data):
        arg = self.createDB(UserUrl)
        uid = self.getUniqueID(UserUrl)
        self.createTiwitterTable(UserUrl)
        connect = sqlite3.connect(arg)
        db = connect.cursor()

        #append this string if need to support more data
        #increase '?' marks for more data REPLACE function automatically overwrite exisit entries of same dates
        tableArg = 'REPLACE INTO ' + uid + ' (Date, followersCount, tweetCount) VALUES (?, ?, ?)'

        #add data[] to this line for more data support
        db.execute(tableArg,(self.getDate(), data[0], data[1]))

        #save the database.
        connect.commit()
        db.close
    #ENDOFMETHOD

    #retirve User Youtube information
    def getYoutubeDB(self, UserUrl):
        arg = self.createDB(UserUrl)
        uid = self.getUniqueID(UserUrl)
        connect = sqlite3.connect(arg)
        db = connect.cursor()

        #return entire database in a list
        tableArg = 'SELECT * FROM ' + uid
        db.execute(tableArg) 
        return db.fetchall()
    #ENDOFMETHOD

    #retirve User Youtube information
    def getTwitterDB(self, UserUrl):
        arg = self.createDB(UserUrl)
        uid = self.getUniqueID(UserUrl)
        connect = sqlite3.connect(arg)
        db = connect.cursor()

        #return entire database in a list
        tableArg = 'SELECT * FROM ' + uid
        db.execute(tableArg) 
        return db.fetchall()
    #ENDOFMETHOD