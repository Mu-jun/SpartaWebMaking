from pymongo import MongoClient
client = MongoClient('mongodb://test:test@52.78.104.136', 27017)
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


"""
scrap_id1 = db.tealist.find_one({'name': '세작'})
scrap_id2 = db.tealist.find_one({'name': '대작'})
id_list = []
id_list.append(scrap_id1['_id'])
id_list.append(scrap_id2['_id'])

print(id_list)
db.users.update_one({'id': "123"}, {'$set': {'scrap_id': id_list}}, True)
"""
"""
scrap_list = list(db.users.find({'id': '123'}))
a = scrap_list[0]['scrap_id']
for i in a:
   b = list(db.tealist.find({'_id':i},{'_id':False}))
   print(b)
"""
"""
check_id_list = list(db.users.find({'id': '123'}))
a = check_id_list[0]['scrap_id']
print(a)
"""

# check_scrap_id = list(db.users.find({'id': '123'}))[0]['scrap_id']
# for i in range(len(check_scrap_id)):
#    a = check_scrap_id[i]
#    check_tealist = list(db.tealist.find({'_id':a}))[0]['_id']

#check_scrap_id = list(db.users.find({'id': '123'}))[0]['scrap_id'][0]
#print(check_scrap_id)
#check_tealist = list(db.tealist.find({'_id': check_scrap_id}))[0]['_id']
#print(check_tealist)
#check_id_list = list(db.users.find({'id': '123'}))[0]['scrap_id']
#print(check_id_list)


"""
if db.users.find({'id': '123'})[0]['scrap_id'] == None:
    scrap_id = db.tealist.find_one({'name': '대작'})['name']
    db.users.update_one({'id': '123'}, {'$set': {'scrap_id': scrap_id}},True)
else:
    scrap_id = db.tealist.find_one({'name': '세작'})['name']
    users_scrap_list = db.users.find({'id': '123'})[0]['scrap_id']

    a = users_scrap_list+','+scrap_id

    db.users.update_one({'id':'123'},{'$set': {'scrap_id': a}},True)
"""
"""
check_scrap_id = list(db.users.find({'id': '123'}))[0]['scrap_id']
a = check_scrap_id.split(',')
print(a)
print(len(a))
success_count = 0
for i in a:
    check_tealist = list(db.tealist.find({'name': i}))[0]['name']
    print(check_tealist)
    if check_tealist in a:
        success_count += 1
        print(success_count)
        if success_count == len(a):
             return jsonify({'alreadyScrap': '이미 찜 하셨습니다.'})
    else:
        new_like = current_like + 1
        db.tealist.update_one({'name': name_receive}, {'$set': {'like': new_like}})
        if db.users.find({'id': current_user})[0]['scrap_id'] == None:
            scrap_id = db.tealist.find_one({'name': name_receive})['name']
            db.users.update_one({'id': current_user}, {'$set': {'scrap_id': scrap_id}}, True)
        else:
            scrap_id = db.tealist.find_one({'name': name_receive})['name']
            users_scrap_list = db.users.find({'id': current_user})[0]['scrap_id']

            a = users_scrap_list + ',' + scrap_id

            db.users.update_one({'id': '123'}, {'$set': {'scrap_id': a}}, True)
        return jsonify({'successScrap': '좋아요, 찜 완료.'})
"""
"""
check_id_list = list(db.users.find({'id': '123'}))[0]['scrap_id']
a = check_id_list.split(',')
all_scraps = []
for i in a:
    check_tealist = list(db.tealist.find({'name': i}))[0]
    print(check_tealist)
    all_scraps.append(check_tealist)
print(all_scraps)
"""

db.users.update_one({'id': '345'}, {'$set': {'scrap_id': None}}, True)
# a = "".join([str(i) for i in check_scrap_id]) # 문자열 만들기

# check_scrap_id = db.users.find_one({'id': '123'})['scrap_id']
# print(check_scrap_id)

# check_id_list = db.users.find_one({'id': '123'})['scrap_id']
# print(check_id_list)


# # 지우기 - 예시
# db.users.delete_one({'name':'bobby'})
# #여러개를 지울 때는 delete_many가 있지만 위험해서 잘 쓰지 않는다.
