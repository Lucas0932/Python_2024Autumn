from flask import Flask
app = Flask(__name__, static_folder = "static", static_url_path = "/static") # 建立 app 變數為 Flask 物件，__name__ 表示目前執行的程式
#路由設定
@app.route("/")
def index():
    return "Welcome to my Web!"
@app.route("/member/<name>")
def sayHi(name):
    return "Hello, our favorite member: " + name
@app.route("/admin/<level>")
def login(level):
    if level =="A":
        return "Login here!"
    else:
        return "You can not login in!"

app.run() # 執行