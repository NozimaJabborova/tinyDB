from tinydb import TinyDB, Query
db=TinyDB('db.json')
#db.truncate()

q=Query()
db.remove(q.user_id==2)
db.remove(q.user_id==4)
data=db.all()
for i in data:
    print(i['user_id'])
    print(i['username'])
