from flask import Flask , render_template, request
import datetime

app = Flask(__name__)
# 태어난 년도를 입력받아 나이를 출력
@app.route("/nai_view")
def nai_view() :
    return render_template("nai_view.html")
# 년도를 입력받는 화면 결과를 출력하는 화면

@app.route("/nai_result")
def nai_result() :
    this_year = datetime.datetime.now().year
    birth_year = int(request.args["birth_year"])
    print(birth_year)
    result = this_year - birth_year
    return render_template("nai_result.html",result = result)
    
app.run()