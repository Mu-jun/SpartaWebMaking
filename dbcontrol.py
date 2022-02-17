from pymongo import MongoClient
client = MongoClient('mongodb://test:test@54.180.2.121', 27017)
db = client.dbchacha

# # 저장 - 예시
# doc = {'name':'bobby','age':21}
# db.users.insert_one(doc)

# # 한 개 찾기 - 예시
# user = db.tealist.find_one({'name':'둥굴레차'})

# # 여러개 찾기 - 예시 ( _id 값은 제외하고 출력)
# same_ages = list(db.users.find({'age':21},{'_id':False}))

# # 바꾸기 - 예시
# db.users.update_one({'name':'bobby'},{'$set':{'age':19}})
# #여러개를 바꿀 때는 update_many가 있지만 위험해서 잘 쓰지 않는다.

# db.tealist.update_one({'name':'커피'},{'$set':{'benefit':'피로회복 힐링힐링'}})
# db.tealist.update_one({'name':'결명자차'},{'$set':{'like':0}})

scrap_list = list(db.scraps.find({'user_id':"123"}, {'_id': False}).sort("name"))

print(scrap_list)






# # 지우기 - 예시
# db.users.delete_one({'name':'bobby'})
# #여러개를 지울 때는 delete_many가 있지만 위험해서 잘 쓰지 않는다.
