from flask import Flask, request, render_template, send_from_directory
from waitress import serve
from sql import *
import json


app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/ping")
def pong():
    return "pong", 200, {'Access-Control-Allow-Origin': '*', 'Access-Control-Allow-Methods': 'POST', 'Access-Control-Allow-Headers': 'Content-Type'}


@app.route("/add", methods=["POST", "OPTIONS"])
def addBookmark():
    # Handle preflight request
    if request.method == "OPTIONS":
        return "", 200, {'Access-Control-Allow-Origin': '*', 'Access-Control-Allow-Methods': 'POST', 'Access-Control-Allow-Headers': 'Content-Type'}


    try:
        data = request.get_json()
        if data is None:
            return "Error: No data", 400, {'Access-Control-Allow-Origin': '*'}

    except Exception as e:
        print(e)
        print("Invalid JSON format")
        return "Invalid JSON format", 400, {'Access-Control-Allow-Origin': '*'}
    
    try:
        addBM(data.get("name"), data.get("link"), data.get("folder"))
    except Exception as e:
        print("skipped folder")
        addBM(data.get("name"), data.get("link"))


    return "Successfully added to DB", 200, {'Access-Control-Allow-Origin': '*', 'Access-Control-Allow-Methods': 'POST', 'Access-Control-Allow-Headers': 'Content-Type'}


app.run(host="0.0.0.0", port=4321, debug=True)
#serve(app, host="0.0.0.0", port=4321)
#print("Server is runing")