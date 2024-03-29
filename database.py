## @file database.py
#
# @brief this contains the database class.
#
# @author JunHao
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

    #Init Constructor
    def __init__(self, dataBaseName):
        """! database class initializer
        @param dataBaseName; any name you want it to be.
        @return an instance of database class
        """
        self.__dataBaseName = dataBaseName
        self.__arg = self.__createDB() #Create Database on init.
        self.connect = sqlite3.connect(self.__arg)
        self.db = self.connect.cursor()
       
    #Get current data Format: Year/Month/Day
    def __getDate(self):
        """! get current date from system.
        @return date in string format
        """

        date = datetime.date.today()
        return str(date)

    #Create database based on given name on init.
    def __createDB(self):
        """! create database based on social media sites.
        @return String argument used to create the database.
        """

        self.createDirectory() #create data folder if not exist.
        #String Argurment to create database based on site.
        arg = './data/' + self.__dataBaseName + '.db'
        #create database if not exist else connect to database.
        try:
            sqlite3.connect(arg)
        except:
            print("__createDB: database creation failed.")

        return arg #return database location

    #Create a table with custom tablename, primary key and variable column names and amount.
    def createTable(self, *argument):
        """! Create custom table based on *argument
        @param *argument; tablename, primary key, variable column names and amount.
        E.g., createTable('tablename','key','column name')
        """
        #Custom Argument string phrase and execute
        try:
            tableArg = 'CREATE TABLE IF NOT EXISTS ' + "'" + argument[0] + "'" + '(' + argument[1] + ' text PRIMARY KEY, ' #argument[0] = tablename, argument[1] = primary key
            last = len(argument)
            for i in range(2, len(argument)-1):
                tableArg = tableArg + argument[i] + ' text, ' #append till 2nd last argument.
            tableArg = tableArg + argument[last-1] + ' text)' #add last argument.
        except:
            print("createTable: tableArg string failed.")

        try:
            self.db.execute(tableArg)
        except:
            print("createTable: db.execute() failed.")

        try:
            #Create Unqiue index for replace function of SQLite3
            tableArg = 'CREATE UNIQUE INDEX ' + 'IF NOT EXISTS ' + 'idx_' +  argument[0] + '_' + argument[1]  + ' ON ' + argument[0] + ' (' + argument[1] + ')'
            self.db.execute(tableArg)
            self.connect.commit()    
        except:
            print("createTable: Unqiue index creation failed.")

    #Save data to table in database. where *argument must match the one provided in createTable.
    def insertTable(self, data, *argument):
        """! insert data into table based on userid and site.
        @param data; 1D python list.
        @param *argument;  tablename, primary key, variable column names and amount.
            E.g., insertTable(data,'tablename','key','column name')
        """
        #Create tableArg string according to *argument
        try:
            last = len(argument)
            tableArg = 'REPLACE INTO ' + "'" + argument[0] + "'" + ' ('
            for i in range(1,len(argument)-1):
                tableArg = tableArg  + argument[i] + ', '
            tableArg = tableArg + argument[last-1] + ') VALUES ('
            for i in range(1,len(argument)-1):
                tableArg = tableArg + '?, '
            tableArg = tableArg + '?)'
        except:
            print("insertTable: tableArg string failed.")

        #Execute tableArg with data.
        try:
            self.db.execute(tableArg,data)
            self.connect.commit()

        except:
            print("insertTable: db.execute() failed.")

    #Retrieve data from database. With custom SELECT and WHERE arguments supported.
    #if WHERE argument is used, * needs to be provided in argCol.
    def getTableData(self, tableName, argSELECT='*', argWHERE = ''):
        """! retrieve data from database based on UserID and site.
        @param tableName;
        @param argCol; E.g., '<Column or Primary Key name.>'
        @param argWhere; E.g., 'WHERE <Column or Primary Key name.> = <Matching value/text>'
                E.g., getTableData('tableName','*','WHERE key = #')
        @return data; 2D python list.
        """
        data = []
        #String Argurment to retrieve data from database.
        try:
            tableArg = 'SELECT ' + argSELECT + ' FROM ' + "'" + tableName + "'" + ' ' + "'" + argWHERE + "'"
        except:
            print("getTableData: tableArg string failed.")
        
        try:
            self.db.execute(tableArg)     
            rows = self.db.fetchall()
            for row in rows:
                data.append(list(row))
        except:
            print("getTableData: db.execute() failed./Table not exist.")

        return data

    #Delete table in database.
    def deleteTable(self,tableName):
        """! Delete the table given.
        @param tableName;
        """
        try:
            tableArg = 'DROP TABLE ' + tableName
            self.db.execute(tableArg)
            self.connect.commit()

        except:
            print("deleteTable: Table Delete failed./Table does not Exist.")

    #Close the database.
    def dbClose(self):
        """! Close the database.
        """
        self.db.close()
        self.connect.close()