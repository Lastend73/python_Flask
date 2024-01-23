import flask as f
import dao
app = f.Flask(__name__)

@app.route("/")
def main() :
    result = dao.findall()
    return f.render_template("list.html",list = result)

@app.route("/read")
def read() :
    bno = f.request.args.get("bno",type=int)
    board = dao.findone(bno = bno)
    return f.render_template("read.html",board=board)

@app.route("/write")
def write() :
    return f.render_template("write.html")

@app.route("/write", methods=['post'])
def write_post() :
    title = f.request.form.get("title",type=str)
    nickname = f.request.form.get("nickname",type=str)
    content = f.request.form.get("content",type=str)
    dao.save(title = title, nickname= nickname, content = content)
    return f.redirect("/")

app.run(debug=True)