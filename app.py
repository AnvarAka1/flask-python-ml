from flask import Flask, redirect, url_for, render_template, request, jsonify
from logic import Image
import os
import cv2
from functions import *
import logging
import sys

logging.basicConfig(level=logging.DEBUG)

app = Flask(__name__)
img = Image()
@app.route("/")
@app.route("/<error>")
def home(error=None):
    return render_template("index.html", image=img.getImage(), error=error)


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        name = request.form['name']
        return redirect(url_for("nameRoute", name=name))
    return render_template('login.html')


@app.route("/image", methods=["POST"])
def imageRoute():
    # check if the post request has the file part
    file = request.files['file']
    img.setImage(file.filename)
    file.save(os.path.join("static", "images", img.getImage()))
    return render_template('index.html', image=img.getImage())


# @app.errorhandler(404)
# def p404():
#     return redirect(url_for('home', error="Error! No such page!"))


@app.route("/processing", methods=["POST", "GET"])
def processingRoute():
    if(request.method == "POST"):
        json = request.json
        img.applyImageProcessingTechniques(int(json['processing']))
        return jsonify(img.getFilteredImage())

    if img.getImage() == None:
        return redirect(url_for('home', error="Error! Choose file first"))
    items = [
        {
            "id": 0,
            "title": "Blur the image"
        },
        {
            "id": 1,
            "title": "Convert to gray scale image"
        },
        {
            "id": 2,
            "title": "Convert to binary image"
        },
    ]
    return render_template('processing.html', image=img.getImage(), items=items)


@app.route("/<name>")
def nameRoute(name):
    return f"<h1>{name}</h1>"


if __name__ == "__main__":
    app.run(debug=True)
