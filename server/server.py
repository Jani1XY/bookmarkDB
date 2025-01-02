from flask import Flask, request, render_template, send_from_directory
from waitress import serve


app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/ping")
def pong():
    return "pong", 200, {'Access-Control-Allow-Origin': '*', 'Access-Control-Allow-Methods': 'POST', 'Access-Control-Allow-Headers': 'Content-Type'}





app.run(host="0.0.0.0", port=4321, debug=True)
#serve(app, host="0.0.0.0", port=4321)
#print("Server is runing")


# Thanks Google Gemini