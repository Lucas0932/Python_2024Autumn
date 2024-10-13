from flask import render_template
from flask import Flask
from flask import request
app = Flask(__name__)
@app.route("/investigation")
def index():
    return render_template("class4hw.html")
@app.route("/submit", methods = ["POST"])
def invest_submit():
    name = request.values["myname"]
    email = request.values["myemail"]
    intrest = request.values["choice"]
    return "表單成功提交!您的資料如下: <br> 姓名: " +  name + "<br> 信箱: " + email + "<br> 想要學的技術: " + intrest
app.run()