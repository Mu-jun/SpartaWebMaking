from pymongo import MongoClient
client = MongoClient('mongodb://test:test@54.180.2.121', 27017)
db = client.dbchacha

# # 바꾸기 - 예시
# db.users.update_one({'name':'bobby'},{'$set':{'age':19}})
# #여러개를 바꿀 때는 update_many가 있지만 위험해서 잘 쓰지 않는다.

db.tealist.update_one({'name':'커피'},{'$set':{'benefit':'피로회복 힐링힐링'}})

# # 지우기 - 예시
# db.users.delete_one({'name':'bobby'})
# #여러개를 지울 때는 delete_many가 있지만 위험해서 잘 쓰지 않는다.
