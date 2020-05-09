from flask import Flask, redirect, url_for, render_template, request, jsonify
from flask_cors import CORS
from logic import Image
import os
import cv2
from functions import *
from items import *
import logging
import time
import sys
logging.basicConfig(level=logging.DEBUG)

app = Flask(__name__)
CORS(app)
img = Image()
@app.route("/")
@app.route("/<error>")
def home(error=None):
    return render_template("index.html", image=img.getImage(), error=error)


@app.route("/image", methods=["POST"])
def imageRoute():
    # check if the post request has the file part
    file = request.files['file']
    img.setImage(file.filename)
    file.save(os.path.join("static", "images", img.getImage()))
    return render_template('index.html', image=img.getImage())


@app.route("/classification", methods=["GET", "POST"])
def classificationRoute():
    if(request.method == "POST"):
        json = request.json
        results = img.applyClassification()
        return jsonify(results)
    if img.getImage() == None:
        return redirect(url_for('home', error="Error! Choose file first"))

    return render_template('index.html', image=img.getImage())


@app.route("/processing", methods=["POST", "GET"])
def processingRoute():
    if(request.method == "POST"):
        json = request.json
        img.applyImageProcessingTechniques(int(json['mt']), 0)
        return jsonify(img.getFilteredImage())

    if img.getImage() == None:
        return redirect(url_for('home', error="Error! Choose file first"))

    return render_template('processing.html', image=img.getImage(), items=getPItems())


@app.route("/blur", methods=["POST", "GET"])
def blurringRoute():
    if(request.method == "POST"):
        json = request.json
        img.applyImageProcessingTechniques(int(json['mt']), 1)
        return jsonify(img.getFilteredImage())

    if img.getImage() == None:
        return redirect(url_for('home', error="Error! Choose file first"))

    return render_template('blur.html', image=img.getImage(), items=getBItems())


@app.route("/colors", methods=["POST", "GET"])
def colorRoute():
    if(request.method == "POST"):
        json = request.json
        img.applyImageProcessingTechniques(int(json['mt']), 2)
        return jsonify(img.getFilteredImage())

    if img.getImage() == None:
        return redirect(url_for('home', error="Error! Choose file first"))

    return render_template('color.html', image=img.getImage(), items=getCItems())


@app.route("/resize", methods=["POST", "GET"])
def resizeRoute():
    if(request.method == "POST"):
        width = request.form['width']
        height = request.form['height']
        if(width == "" or height == "" or int(width) < 1 or int(height) < 1):
            return render_template('resize.html', image=img.getImage(), error="Enter both width and height properly")
        img.applyResize(width=width, height=height)

        return render_template('resize.html', image=img.getImage(), resizedImg=f"{img.getFilteredImage()}?_={int(round(time.time() * 1000))}")
    if img.getImage() == None:
        return redirect(url_for('home', error="Error! Choose file first"))
    return render_template('resize.html', image=img.getImage())


@app.route("/tutorial", methods=["POST", "GET"])
def tutorialRoute():

    if request.method == "POST":
        return jsonify({"items": getTutorialItems(), "result": img.applyClassification()})
    if img.getImage() == None:
        return redirect(url_for('home', error="Error! Choose file first"))
    return render_template("tutorial.html", image=img.getImage(), items=getTutorialItems())


if __name__ == "__main__":
    app.run(debug=True)
