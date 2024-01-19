from flask import Flask ,render_template, request

app = Flask(__name__)

@app.route("/name",methods = ['get'])

def view():
    return render_template("city.html")

@app.route("/name",methods = ['post'])
def result():

    name = request.form["name"]
    city = request.form["city"]

    return render_template("city_result.html",name=name,city= city)

app.run()