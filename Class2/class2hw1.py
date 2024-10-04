from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>2024 Autumn</h1>"

app.run()