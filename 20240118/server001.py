# flask 설치
# terminal에 가서 pip install flask
# 프런트 는 cdn 파이썬은 pip

from flask import Flask
from flask import request
# class는 -> 사용자 정의 자료형을 만드는방법. 파이썬은 모든 타입의 클래스

# __name__은 현재 파일이름  -> Flsak 웹서버 객체를 생성
# 서버는 사용자 요청을 기달리다가 요청이 들어오면 처리해주는 프로그램이다
# Flask 웹서버는 5000번 포트로 사용자 요청을 대기한다

app = Flask(__name__)

# annotation(@) : 
# @app.route("주소") -> 127.0.0.1:5500/"주소"를 치면 결과가 나옴
@app.route("/hello")
def abc():
    return "hello flask123"

@app.route("/hello1")
def insa():
    return "안녕하세요"

@app.route("/hello3")
def add():
    #  사용자 요청정보가 담긴 변수
    val = request.args["val"]
    return val

@app.route("/hello2")
def times():
    # request로 전달받은 값은 무조건 글자
    val = int(request.args["val"])
    result = val*val
    return f"제곱 결과는 {result}입니다"

@app.route("/key")
def key() :
    val = int(request.args["val"])
    result = val-105
    return f"적정체중은 {result}cm 입니다"

# 400 = 잘못된 요청 ex) val 값을 안넘김
# 200 = 성공
# 403 = 권한없음
# 404 = 요청한 문서 없음
# 405 = 메소드 매칭 안됨 ex) get인대 post로 넘기거나 반대
# 500 = 계산중 오류 
app.run()