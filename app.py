
from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

# DB 관련
from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.dbchacha

# 차 정보 입력하기(POST) API

@app.route('/save', methods=['POST'])
def save_tea():
    name_receive = request.form['name_give']
    blend_receive = request.form['blend_give']
    benefit_receive = request.form['benefit_give']
    caffeine_receive = request.form['caffeine_give']
    desc_receive = request.form['desc_give']

    doc = {
        'name': name_receive,
        'blend': blend_receive,
        'benefit': benefit_receive,
        'caffeine': caffeine_receive,
        'desc' : desc_receive,

    }

    db.tealist.insert_one(doc)


    return jsonify({'msg': '차 등록이 완료되었습니다!'})



@app.route('/')
def home():
   return render_template('index.html')

#GET요청API코드
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
#   })

if __name__ == '__main__':
   app.run('0.0.0.0',port=5000,debug=True)