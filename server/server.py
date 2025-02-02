from flask import Flask, request, render_template, send_from_directory, jsonify
from waitress import serve
from sql import *
import json


app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/ping")
def pong():
    return jsonify({"message": "pong"}), 200, {'Access-Control-Allow-Origin': '*'}

def options_response():
    return "", 200, {
        'Access-Control-Allow-Origin': '*', 
        'Access-Control-Allow-Methods': 'POST', 
        'Access-Control-Allow-Headers': 'Content-Type',
    }

@app.route("/add", methods=["POST", "OPTIONS"])
def addBookmark():
    # Handle preflight request
    if request.method == "OPTIONS":
        return options_response()

    try:
        data = request.get_json()

        if not data:
            return jsonify({"message": "No data"}), 400, {'Access-Control-Allow-Origin': '*'}

        name = data.get("name")
        url = data.get("url")
        folder = data.get("folder")

        print("added name:  " + name)
        print("added url:  " + url)

        if url == None:
            return jsonify({"message": "Missing required fields"}), 418, {'Access-Control-Allow-Origin': '*'}


        if not folder:
            result = addBM(name, url)
        else:
            result = addBM(name, url, folder)


        if not result:
            return jsonify({"message": "Failed to add bookmark"}), 500, {'Access-Control-Allow-Origin': '*'}


        return jsonify({"message": "Bookmark added successfully"}), 201, {'Access-Control-Allow-Origin': '*'}


    except Exception as e:
        print(f"Error adding bookmark: {e}")
        return jsonify({"message": "Big internal server error. Check logs"}), 500, {'Access-Control-Allow-Origin': '*'}


@app.route("/get", methods=["POST", "OPTIONS"])
def doesLinkExsist():
    if request.method == "OPTIONS":
        return options_response();

    try:
        data = request.get_json()

        url = data.get("url")

        if not data:
            return jsonify({"message": "No data"}), 400, {'Access-Control-Allow-Origin': '*'}
    

        if getLink(url):
            return jsonify({"message": "URL exsists", "exsist": True}), 200, {'Access-Control-Allow-Origin': '*'}
        else:
            return jsonify({"message": "URL doesn't exsist", "exsist": False}), 200, {'Access-Control-Allow-Origin': '*'}
    
    except Exception as e:
        print(f"Error getting link: {e}")
        return jsonify({"message": "Big internal server error. Check logs"}), 500, {'Access-Control-Allow-Origin': '*'}



@app.route("/delete/one", methods=["POST", "OPTIONS"])
def deleteOne():
    if request.method == "OPTIONS":
        return options_response();

    try:
        data = request.get_json()

        url = data.get("url")

        deleteOneLink(url)

        return jsonify({"message": "Deleted bookmark"}), 200, {'Access-Control-Allow-Origin': '*'}
        
    except Exception as e:
        print(f"Error getting link: {e}")
        return jsonify({"message": "Big internal server error. Check logs"}), 500, {'Access-Control-Allow-Origin': '*'}

app.run(host="0.0.0.0", port=4321, debug=True)
#serve(app, host="0.0.0.0", port=4321)
#print("Server is runing")