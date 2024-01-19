from flask import Flask, render_template, request


app= Flask(__name__)

@app.route("/name", methods = ['post'])
def name_result() :

    nai = request.form["nai"]
    irum = request.form["irum"]
    return render_template("name2_result.html",nai = nai,irum =irum)

@app.route("/name", methods= [ 'get'])
def name_input() :
    return render_template("name2_input.html")   

app.run()