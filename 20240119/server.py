# 사용자의 요청에 응답하는 서버 : 백앤드 + 화면

# 프레임워크 - 필요한 기능들을 부품화해서 조합하는 방식
# templates - hmtl, static - css, js

from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/hello")
def test() :
    test = request.args["hello"]

    #현재 서버의 모든 url을 출력해라
    print(app.url_map)

    return render_template("test.html",test= test)

# 어떤 작업을 하려면 화면을 보여준다(get) + 결과를 출력한다(post)
# 이름을 입력받아 출력 
@app.route("/name", methods = ['post'])
def name_result() :

    # get 방식 요청 데이터 : request.args 
    # get은 QueryString 방식으로 서버에 값을 전달한다
    # 형식은 URLencoded

    # urlencode 방식으로 저장하는거며 이를 방식은 QueryString

    # post방식 요청 데이터 : request.form
    name = request.form["name"]
    return render_template("name_result.html",name = name)

@app.route("/name", methods= [ 'get'])
def name_input() :
    return render_template("name_input.html")



# debug란 개발 모드, 배포모드는 relase
app.run()