# 이름과 나이를 입력받아 다음과 같은 출력한다
# 홍길동님은 성년입니다 or 홍길동님은 미성년입니다
# 단 성년인 경우 글자색은 파랑, 미성년인 경우 글자색은 빨강

from flask import Flask, render_template, request
app = Flask(__name__)

@app.route("/work", methods = ['get'])
def work():
    return render_template("work_input.html")

@app.route("/work", methods = ['post'])
def work_input():
    irum = request.form.get('irum',type=str)
    nai = request.form.get('nai',type=int)
     
    is_adult = nai >= 18

    return render_template("/work_result1.html",irum=irum, nai=nai, is_adult= is_adult)

    # if 나 for는 flask 또는 html에서 가능
app.run(debug=True)