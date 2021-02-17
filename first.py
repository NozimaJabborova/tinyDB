from tinydb import TinyDB
db=TinyDB('db.json')
user1={'user_id':1,'username':'Nozima'}
user2={'user_id':2,'username':'Nigora'}
user3={'user_id':3,'username':'Shaxlo'}
user4={'user_id':4,'username':'Dildora'}
db.insert(user1)
db.insert(user2)
db.insert(user3)
db.insert(user4)
