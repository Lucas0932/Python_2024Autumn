from flask import Flask
app = Flask(__name__, static_folder = "static", static_url_path = "/static")

@app.route("/")
def home():
    return "<h1>2024 Autumn</h1>"

app.run()
