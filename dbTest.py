#This contains the test case for database
from database import database

def testDB():
    #Create/Connect to Database with given name
    uTest = database('testDB')

    #Test 1:
    data = ['Key1','1','2'] #data count to be same amount as key + col.

    #Create Table with given name, key, columns
    uTest.createTable('test1','key','C1','C2')

    #Insert Data into table with the structure declared.
    uTest.insertTable(data,'test1','key','C1','C2')

    #Retrive all of the data in the table
    datalist = uTest.getTableData('test1') 
    print(datalist)
    #End of test 1.

    #Test 2:
    data = ['Key2','1']
    uTest.createTable('test2','key','C1')
    uTest.insertTable(data,'test2','key','C1')

    #Special Argument for specific columns
    datalist = uTest.getTableData('test2','C1')
    print(datalist)

    #Test 3: Retriving specific information in table test1
    datalist = uTest.getTableData('test1','*','WHERE C1=1')
    print(datalist)
    datalist = uTest.getTableData('test1','C1')
    print(datalist)

testDB()