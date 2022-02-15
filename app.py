
from flask import Flask, render_template, request, jsonify
from flask_jwt_extended import *
import hashlib
from hashlib import *
import jwt
import datetime
import chachaconfig

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False #한글 깨짐 현상 해결코드

# configure Flask App with Flask RESTFUL API
# Flask RESTFUL API로 Flask App 구성
#api = Api(app)

app.config['JWT_SECRET_KEY'] = chachaconfig.jwt_key
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = datetime.timedelta(minutes=5)
app.config['JWT_REFRESH_TOKEN_EXPIRES'] = datetime.timedelta(days=10)
app.config['PROPAGATE_EXCEPTIONS'] = True

# configure Flask App with JWT support
# JWT 지원으로 Flask App 구성
jwt = JWTManager(app)

# DB 관련
from pymongo import MongoClient
client = MongoClient('localhost', 27017)
# client = MongoClient('mongodb://test:test@54.180.2.121', 27017)
db = client.dbchacha

# 차 정보 입력하기(POST) API

@app.route('/save', methods=['POST'])
def save_tea():
    print(request.is_json)
    tea_receive = request.get_json()
    print(tea_receive)
    
    name_receive = tea_receive['name_give']                              #차 이름입니다
    type_receive = tea_receive['type_give']                              #대분류1 차의 종류
    benefit_receive = tea_receive['benefit_give']                        #대분류2 효능
    caffeineOX_receive = tea_receive['caffeineOX_give']                  #대분류3 카페인 "함유여부" 없으면 "0" 있으면 "1"
    caffeine_receive = tea_receive['caffeine_give']                      #상세1 카페인 "함량"
    benefitdetail_receive = tea_receive['benefitdetail_give']            #상세2 상세효능
    desc_receive = tea_receive['desc_give']                              #상세2 상세설명
    caution_receive = tea_receive['caution_give']                        #상세3 주의사항
    img_receive = tea_receive['img_give']                                #상세4 이미지 주소

    doc = {
        'name': name_receive,
        'type': type_receive,
        'benefit': benefit_receive,
        'caffeineOX': caffeineOX_receive,
        'caffeine': caffeine_receive,
        'benefitdetail': benefitdetail_receive,
        'desc': desc_receive,
        'caution': caution_receive,
        'img': img_receive,
    }

    db.tealist.insert_one(doc)

    return jsonify({'msg': '차 등록이 완료되었습니다!'})

@app.route('/')
def home():
   return render_template('save_tea.html')

# 회원가입 및 로그인, 로그인 테스트 페이지 코드 test by 승신
#***************************************************************************************************

# [회원가입 API]
# id, pw, nickname을 받아서, mongoDB에 저장합니다.
# 저장하기 전에, pw를 sha256 방법(=단방향 암호화. 풀어볼 수 없음)으로 암호화해서 저장합니다.
@app.route('/sign/signup', methods=['POST'])
def api_register():
    id_receive = request.form['id_give']
    pw_receive = request.form['pw_give']
    nickname_receive = request.form['nickname_give']

    pw_hash = hashlib.sha256(pw_receive.encode('utf-8')).hexdigest()

    doc2 = {'id': id_receive, 'pw': pw_hash, 'nick': nickname_receive}

    db.user.insert_one(doc2)

    return jsonify({'result': '어, 그래 가입 됐다. 가라.'})

# [로그인 API]
# id, pw를 받아서 맞춰보고, 토큰을 만들어 발급합니다.
@app.route('/sign/log_in', methods=['POST'])
def api_login():
    id_receive = request.form['id_give']
    pw_receive = request.form['pw_give']

    # 회원가입 때와 같은 방법으로 pw를 암호화합니다.
    pw_hash = hashlib.sha256(pw_receive.encode('utf-8')).hexdigest()

    # id, 암호화된pw을 가지고 해당 유저를 찾습니다.
    result = db.user.find_one({'id': id_receive, 'pw': pw_hash})

    # 찾으면 JWT 토큰을 만들어 발급합니다.
    if result is not None:
        # JWT 토큰에는, payload와 시크릿키가 필요합니다.
        # 시크릿키가 있어야 토큰을 디코딩(=풀기) 해서 payload 값을 볼 수 있습니다.
        # 아래에선 id와 exp를 담았습니다. 즉, JWT 토큰을 풀면 유저ID 값을 알 수 있습니다.
        # exp에는 만료시간을 넣어줍니다. 만료시간이 지나면, 시크릿키로 토큰을 풀 때 만료되었다고 에러가 납니다.
        payload = {
            'id': id_receive,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(seconds=5)
        }

        SECRET_KEY = "I'M SECRET SEUNGSHIN BRO"

        token = jwt.encode(payload, SECRET_KEY, algorithm='HS256')

        # token을 줍니다.
        return jsonify({'success': '어 그래 로그인 됐다. 와라.', 'token': token})
    # 찾지 못하면
    else:
        return jsonify({'fail': '너 뭐 잘못 했냐?'})

@app.route('/sign')
def signup_page():
   return render_template('01_login.html')

#***************************************************************************************************
# mu-jun's function code

@app.route('/sign/checkID', methods=['POST'])
def checkID():
    
    id_receive = request.get_json().upper()
    
    result = db.users.find_one({'id': id_receive})
    
    if result is not None:
        return jsonify({'fail': '사용할 수 없는 ID입니다.'})
    else:
        return jsonify({'success': '사용 가능한 ID입니다.'})
    
@app.route('/sign/checkNickname', methods=['POST'])
def checkNickname():
    
    nickname_receive = request.get_json().upper()
    
    result = db.users.find_one({'id': nickname_receive})
    
    if result is not None:
        return jsonify({'fail': '사용할 수 없는 별명입니다.'})
    else:
        return jsonify({'success': '사용 가능한 별명입니다.'})

def hash_pass(password, id):
    personal_key = id[:8].encode('utf-8')
    password = password+chachaconfig.salt_key
    
    for i in range(chachaconfig.iteration_num):
        password = password.encode('utf-8')
        password = blake2s(password,person=personal_key).hexdigest()
        
    return password

@app.route('/sign/signup_test', methods=['POST'])
def signup():
    
    id_receive = request.form['id_give'].upper()
    pass_receive = request.form['pass_give']
    nickname_receive = request.form['nickname_give'].upper()
    
    hashed_password = hash_pass(pass_receive,id_receive)
           
    doc = {
        'id': id_receive,
        'password': hashed_password,
        'nickname': nickname_receive
    }
    
    print(doc)
    db.users.insert_one(doc)
    
    return jsonify({'success': '가입완료!'})

@app.route('/sign/signin_test', methods=['POST'])
def api_signin():
    
    id_receive = request.form['id_give'].upper()
    pass_receive = request.form['pass_give']
    
    hashed_password = hash_pass(pass_receive,id_receive)
    
    user = db.users.find_one({'id':id_receive})
    
    print(user)
    
    if(hashed_password == user['password']):
        access_token = create_access_token(identity=user['id'])
        refresh_token = create_refresh_token(identity=user['id'])
    
        return jsonify({'success':'환영합니다.'+user['nickname']+'님','access_token':access_token, 'refresh_token':refresh_token})
    else:
        return jsonify({'fail':'ID와 비밀번호를 확인해주세요.'})

@app.route('/sign/change_pass', methods=['POST'])
@jwt_required()
def api_change_pass():
    current_user = get_jwt_identity()
    
    print(type(current_user))
    print(current_user)
    
    pass_receive = request.form['pass_give']
    new_password = request.form['new_pass_give']
    
    hashed_password = hash_pass(pass_receive,current_user)
    new_password = hash_pass(new_password,current_user)
    
    user = db.users.find_one({'id':current_user})
    
    print(user)
    
    if(hashed_password == user['password']):
        db.users.update_one({'id':current_user},{'$set':{'password':new_password}})    
        return jsonify({'success':'비밀번호가 변경되었습니다.'})
    else:
        return jsonify({'fail':'기존 비밀번호가 틀렸습니다.'})

# @app.route('/sign/delete_user', methods=['POST'])
# @jwt_required()
# def api_delete_user():
#     current_user = get_jwt_identity()
    
#     return jsonify({'success':'회원탈퇴완료'})

@app.route('/refresh', methods=['GET'])
@jwt_required(refresh=True)
def refresh():
    current_user = get_jwt_identity()
    access_token = create_access_token(identity=current_user)
    return jsonify(access_token=access_token, current_user=current_user)

@app.route('/sign_test')
def sign_page():
   return render_template('sign_test.html')

#***************************************************************************************************
if __name__ == '__main__':
   app.run('0.0.0.0',port=5000,debug=True)

"""    #GET요청API코드
@app.route('/test', methods=['GET'])
def test_get():
   title_receive = request.args.get('title_give')
   print(title_receive)
   return jsonify({'result':'success', 'msg': '이 요청은 GET!'})
#GET확인코드
# $.ajax({
#     type: "GET",
#     url: "/test?title_give=봄날은간다",
#     data: {},
#     success: function(response){
#        console.log(response)
#     }
#   })

#POST요청API코드
@app.route('/test', methods=['POST'])
def test_post():
   title_receive = request.form['title_give']
   print(title_receive)
   return jsonify({'result':'success', 'msg': '이 요청은 POST!'})
   
#POST확인코드
# $.ajax({
#     type: "POST",
#     url: "/test",
#     data: { title_give:'봄날은간다' },
#     success: function(response){
#        console.log(response)
#     }
#   }) """
