## @file database.py
#
# @brief this contains the database class.
#
# @section libraries_main Libraries/Modules
# - sqlite3 standard library (https://docs.python.org/3/library/sqlite3.html)
#   - access to sqlite3 database function
# - datetime standard library (https://docs.python.org/3/library/datetime.html)
#   - access to datetime function
# - mkFolder (local)
#   - access to mkFolder and UrlExtraction function.

# Imports
import sqlite3
import datetime
from mkFolder import mkFolder

## Documentation for a database Class
# database creates database and tables
# table can be inserted with data for storage
# table can also be retrieve for data of user
class database(mkFolder):
    """! database class
    This class inherits the mkFolder class for directory creation.
    This class contains methods specifically related to the database.
    """

    #init
    def __init__(self, UserUrl):
        """! database class initializer
        @param UserUrl
        """
        self.UserUrl = UserUrl
        self.arg = self.__createDB(UserUrl)
        self.uid = self.getUniqueID(UserUrl)        

    #Get current data Format: Year/Month/Day
    def __getDate(self):
        """! get current date from system.
        @return date in string format
        """

        date = datetime.date.today()
        return str(date)

    #create DB based on Social media sites. double underscore indicates private method.
    def __createDB(self, UserUrl):
        """! create database based on social media sites.
        @param UserUrl Url link provided by user.
        @return String argument used to create the database.
        """

        sitename = self.getSiteName(UserUrl)
        self.createDirectory() #create data folder if not exist.
        #String Argurment to create database based on site.
        arg = './data/' + sitename + '.db'
        #create database if not exist else connect to database.
        db = sqlite3.connect(arg)
        db.close() #close database
        return arg #return database location

    #create Table for database. double underscore indicates private method.
    def __createTableDB(self):
        """! create table based on user ID and sites database.
        """

        connect = sqlite3.connect(self.arg)
        db = connect.cursor()
        #String Argurment for Table based on User ID with support for up to 10 Data in text.
        tableArg = 'CREATE TABLE ' + 'IF NOT EXISTS ' + self.uid + '(' + 'Date text PRIMARY KEY, ' + 'C1 text, ' + 'C2 text, ' + 'C3 text, ' + 'C4 text, ' + 'C5 text, ' + 'C6 text, ' + 'C7 text, ' + 'C8 text, ' + 'C9 text, ' + 'C10 text' + ')'
        db.execute(tableArg)
        #Create Unqiue index for replace function of SQLite3
        tableArg = 'CREATE UNIQUE INDEX ' + 'IF NOT EXISTS ' + 'idx_' + self.uid + '_Date ON ' + self.uid +' (Date)'
        db.execute(tableArg)
        connect.commit() #save database
        db.close() #close database

    #insert data into table in database
    def insertTableDB(self, data):
        """! insert data into table based on userid and site.
        @param data data in list to be stored in database table
        """
        self.__createTableDB() #Ensure table for user ID exist else create it.
        connect = sqlite3.connect(self.arg)
        db = connect.cursor()
        #String Argurment for data insertion into table with variable data.
        tableArg = 'REPLACE INTO ' + self.uid + ' (Date, C1, C2, C3, C4, C5, C6, C7, C8, C9, C10) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)'
        #Pass string argurment with data to insert into database.
        db.execute(tableArg,(self.__getDate(), data[0], data[1], data[2], data[3], data[4], data[5], data[6], data[7], data[8], data[9]))
        connect.commit() #save database
        db.close    #close database

    #retrieve user data from database. #convert to SQL retrival method with Argmuent as paramenters
    def getTableDB(self, argCol='*', argWhere = ''):
        """! retrieve data from database based on UserID and site.
        @param argCol E.g., '<C# or Date>'
        @param argWhere E.g., 'WHERE <C# or Date> = <#>
        @return data in python 2d list format
        """
        templist = []
        connect = sqlite3.connect(self.arg)
        #connect.row_factory = sqlite3.Row
        db = connect.cursor()
        #String Argurment to retrieve data from database.
        tableArg = self.__setTableArg(argCol, argWhere)
        db.execute(tableArg)     
        #return db.fetchone() #return data in a list.
        rows = db.fetchall()
        for row in rows:
            templist.append(list(row))
        return templist

    #def parse format (col, filter) where col = C1 or C2 default *. where argWhere = 'WHERE C1 = 198'
    def __setTableArg(self, argCol='*', argWhere = ''):
        """! set table arugment to be pass.
        @param argCol, default: '*' or 'C#'
        @param argWhere default: '' or 'WHERE <C# or Date> = <#>'
        @return tableArg string arugment to be executed.
        """
        tableArg = 'SELECT ' + argCol + ' FROM ' + self.uid + ' ' + argWhere
        return tableArg



#Testing
# tuser = database("https://twitter.com/johnnywharris")
# templist = tuser.getTableDB()
# print(templist[0][1])