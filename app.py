
from flask import Flask, render_template, request, jsonify
import hashlib
import jwt
import datetime

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False #한글 깨짐 현상 해결코드

# DB 관련
from pymongo import MongoClient
client = MongoClient('localhost', 27017)
# client = MongoClient('localhost', 27017)
db = client.dbchacha

# 차 정보 입력하기(POST) API

@app.route('/save', methods=['POST'])
def save_tea():
    name_receive = request.form['name_give']             #차 이름입니다
    blend_receive = request.form['blend_give']           #대분류1 블렌딩
    benefit_receive = request.form['benefit_give']       #대분류2 효능
    caffeineOX_receive = request.form['caffeineOX_give'] #대분류3 카페인 "함유여부"
    caffeine_receive = request.form['caffeine_give']     #상세1 카페인 "함량"
    desc_receive = request.form['desc_give']             #상세2 맛 색 향 등
    caution_receive = request.form['caution_give']       #상세3 주의사항
    img_receive = request.form['img_give']               #상세4 이미지 주소

    doc = {
        'name': name_receive,
        'blend': blend_receive,
        'benefit': benefit_receive,
        'caffeineOX': bool(caffeineOX_receive),
        'caffeine': int(caffeine_receive),
        'desc': desc_receive,
        'caution': caution_receive,
        'img': img_receive,
    }

    db.tealist.insert_one(doc)

    return jsonify({'msg': '차 등록이 완료되었습니다!'})

@app.route('/')
def home():
   return render_template('index.html')

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

if __name__ == '__main__':
   app.run('0.0.0.0',port=5000,debug=True)

"""    #GET요청API코드
@app.route('/test', methods=['GET'])
def test_get():
   title_receive = request.args.get('title_give')
   print(title_receive)
   return jsonify({'result':'success', 'msg': 'GET!'})


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