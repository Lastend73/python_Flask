#  12 -2 겨울   회색
#  3-5 봄       초록
#  6-8 여를     파랑
#  9 - 10 가을  퍼플

from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/start", methods=["get"])
def view():
    return render_template("/start.html")

@app.route("/start", methods=["post"])
def result():
    
    month = request.form.get("month",type=int)
    print(request.form)

    season = '겨울'
    style='winter'

    if 3<=month<=5 :
        season = '봄'
        style='spring'

    elif 6<=month<=8 :
        season = '여름'
        style='summer'

    elif 9<=month<=11 :
        season = '가을'
        style='fall'
    

    return render_template("/start_result.html", season = season, style= style,month=month)

app.run()