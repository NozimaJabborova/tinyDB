from tinydb import TinyDB, Query
db=TinyDB('db.json')
#db.truncate()
data=db.all()
q=Query()
user=db.search(q.user_id==3)
print(user)