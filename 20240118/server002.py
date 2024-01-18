from flask import Flask, request, render_template

app = Flask(__name__)

# 사용자가 입력한 값을 html로 출력한다
@app.route("/sample1")
def sample1():
    val = request.args["val"]

    # html에게 값을 넘기기 위해서는 
    # 서버 폴더 밑에 templates 파일을 만들고 밑에다가 html문서를 넣어야 합니다

    # render_template("넘길 html",넘길 값)
    return render_template("sample1.html",result=val)

#/add?val=10&val2=100
@app.route("/add")
def sample2():
    val1 = int(request.args["val1"])
    val2 = int(request.args["val2"])
    result = val1 + val2
    return render_template("sample2.html",result=result)

@app.route("/add_view")
def add_view():
    return render_template("sample2_view.html")

app.run()