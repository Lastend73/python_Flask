import flask as F
import model as m

app = F.Flask(__name__)

guestbook = m.guestbook
@app.route("/")
def home() :
    return F.render_template("list.html",guestbook = m.list())

@app.route("/write", methods=['post'])
def write() :
    
    gb_name = F.request.form.get("name",type=str)
    gb_content = F.request.form.get("content",type=str)
    m.save(name = gb_name, content= gb_content)
    return F.redirect("/")

@app.route("/delete", methods=['post'])
def delete() :

    gb_gno = F.request.form.get("gno",type=int)
    m.delete(gno=gb_gno)
    return F.redirect("/")

@app.route("/update", methods=['post'])
def update() :

    gb_gno = F.request.form.get("gno",type=int)
    gb_content = F.request.form.get("content",type=str)
    m.update(gno=gb_gno,content=gb_content)
    return F.redirect("/")

app.run()
 