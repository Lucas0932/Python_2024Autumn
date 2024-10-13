from flask import render_template
from flask import Flask
from flask import request
app = Flask(__name__)
#------------------------------------------------------------------------------------------
# @app.route("/question")
# def index():
#     return render_template("class4.html")
#------------------------------------------------------------------------------------------
# @app.route("/<host>")
# def index(host):
#     return render_template("class4.html", host = host)
#------------------------------------------------------------------------------------------
# @app.route("/")
# def index():
#     print("請求方法", request.method)
#     print("通訊協定", request.scheme)
#     print("主機名稱", request.host)
#     print("路徑", request.path)
#     print("完整的網址", request.url)
#     return "Hello Flask" 
#------------------------------------------------------------------------------------------
# @app.route("/")
# def index():
#     print("瀏覽器作業系統", request.headers.get("user-agent"))
#     print("語言偏好", request.headers.get("accept-language"))
#     print("引薦網址", request.headers.get("referrer"))
#     return "Hello Flask"
#------------------------------------------------------------------------------------------
# @app.route("/", methods = ["GET"])
# def index():
#     name = request.args.get("name")
#     print("使用者名稱是", name)
#     return "Hello Flask"
#------------------------------------------------------------------------------------------
# @app.route("/login")
# def login():
#     return "<form method = 'post' action = '/submit'> <input type = 'text' name = 'username' /> <button type = 'submit'>Submit</button></form>"
# @app.route("/submit", methods = ["POST"])
# def submit():
#     username = request.values["username"]
#     return "Hello " + username + "!"
#-----------------------------------------------------------------------------------------
@app.route("/fruit")
def fruit():
    return "<form method = 'post' action = '/submit'> 你最喜歡的水果是: <input type = 'text' name = 'fruit' /> <button type = 'submit'>Submit</button></form>"
@app.route("/submit", methods = ["POST"])
def submit():
    fruit = request.values["fruit"]
    print("Favorite Fruit:", fruit)
    return "我也最喜歡 " + fruit + "!"
#------------------------------------------------------------------------------------------
app.run()