from tinydb import TinyDB
db=TinyDB('db.json')
#db.truncate()
data=db.all()

for i in data:
    print(i['user_id'])
    print(i['username'])