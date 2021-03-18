from database import database
from twitterGraph import twitterGraph

db = database('testDB')
uid = db.getUniqueID("https://twitter.com/BarackObama")
db.createTable(uid,"Date","Rt","Fav")

data = twitterGraph(10,uid)
print(data)