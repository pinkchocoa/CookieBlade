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
#   - access to mkFolder function

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
    def __init__(self, dataBaseName):
        """! database class initializer
        @param dataBaseName; any name you want it to be.
        """
        self.dataBaseName = dataBaseName
        self.arg = self.__createDB() #Create Database on init.
       
    #Get current data Format: Year/Month/Day
    def __getDate(self):
        """! get current date from system.
        @return date in string format
        """

        date = datetime.date.today()
        return str(date)

    #create DB based on given data base name #double underscore indicates private method. 
    def __createDB(self):
        """! create database based on social media sites.
        @return String argument used to create the database.
        """

        self.createDirectory() #create data folder if not exist.
        #String Argurment to create database based on site.
        arg = './data/' + self.dataBaseName + '.db'
        #create database if not exist else connect to database.
        db = sqlite3.connect(arg)
        db.close() #close database
        return arg #return database location

    #create custom table with min arg: tablename, primary key col and atleast 1 col. #Max 2000 col #data stored at text. #11/3/21
    def createTable(self, *argument):
        """! Create custom table based on *argument
        @param *argument; where ('tablename', 'primary key', '1 col name') MUST BE PROVIDED. 
        """

        #connect to DB
        connect = sqlite3.connect(self.arg)
        db = connect.cursor()

        #Custom Argument string phrase and execute
        tableArg = 'CREATE TABLE IF NOT EXISTS ' + argument[0] + '(' + argument[1] + ' text PRIMARY KEY, ' #argument[0] = tablename, argument[1] = primary key
        last = len(argument)
        for i in range(2, len(argument)-1):
            tableArg = tableArg + argument[i] + ' text, ' #append till 2nd last argument.
        tableArg = tableArg + argument[last-1] + ' text)' #add last argument.
        db.execute(tableArg)

        #Create Unqiue index for replace function of SQLite3
        tableArg = 'CREATE UNIQUE INDEX ' + 'IF NOT EXISTS ' + 'idx_' + argument[0] + '_' + argument[1]  + ' ON ' + argument[0] + ' (' + argument[1] + ')'
        db.execute(tableArg)
        connect.commit() #save database
        db.close() #close database

    #insert data into table in database #12/3/21
    def insertTable(self, data, *argument):
        """! insert data into table based on userid and site.
        @param data; data list to be stored in db
        @param *argument;  where ('tablename', 'primary key', '1 col name') MUST BE PROVIDED.
        """
        connect = sqlite3.connect(self.arg)
        db = connect.cursor()

        #Append tableArg according to *argument
        last = len(argument)
        tableArg = 'REPLACE INTO ' + argument[0] + ' ('
        for i in range(1,len(argument)-1):
            tableArg = tableArg  + argument[i] + ', '
        tableArg = tableArg + argument[last-1] + ') VALUES ('
        for i in range(1,len(argument)-1):
            tableArg = tableArg + '?, '
        tableArg = tableArg + '?)'
        #Pass string argurment with data to insert into database.
        db.execute(tableArg,(data))
        connect.commit() #save database
        db.close    #close database

    #retrieve user data from database. #good but user need remember the table style inforamtion. #11/3/21
    def getTableData(self, tableName, argCol='*', argWhere = ''):
        """! retrieve data from database based on UserID and site.
        @param tableName; E.g., 'tableName'
        @param argCol; E.g., '<Col_name or PRIMARY KEY>' default '*'
        @param argWhere; E.g., 'WHERE <Col_name or PRIMARY KEY> = <#>' param argCol must be entered if using this parameter.
        @return templist; where data is in python 2d list format.
        """
        templist = []
        connect = sqlite3.connect(self.arg)
        db = connect.cursor()
        #String Argurment to retrieve data from database.
        tableArg = 'SELECT ' + argCol + ' FROM ' + tableName + ' ' + "'" + argWhere + "'"
        db.execute(tableArg)     
        rows = db.fetchall()
        for row in rows:
            templist.append(list(row))
        return templist