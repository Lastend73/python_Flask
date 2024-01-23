import flask as F
import dao
app = F.Flask(__name__)

# 방명록 출력
@app.route("/")
def 출력():
    result = dao.findall()
    return F.render_template("list.html",list = result)

# 방명록 추가 : 화면을 보여주고 입력을 받는다
@app.route("/write",methods = ['post'])
def 추가():
    nickname = F.request.form.get("name",type=str)
    content = F.request.form.get("content",type=str)
    dao.save(nickname = nickname, content=content )
    return F.redirect("/")

# 방명록 삭제
@app.route("/delete" , methods=['post'])
def 삭제():
    bno = F.request.form.get('bno',type=int)
    dao.delete(bno)
    return F.redirect("/")

app.run()