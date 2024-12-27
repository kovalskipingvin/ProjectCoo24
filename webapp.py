from flask import Flask

app = Flask(__App__)

@app.route("/")
def index():
    return "Congratulations, it's a web app!"
