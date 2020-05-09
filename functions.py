import cv2
import numpy as np
from blur import *
from keras.models import load_model
from keras.preprocessing import image
import numpy as np
import tensorflow as tf

# Before detecting the edges, convert the 3-channel color image to 1 channel gray image


def convertToGrayImage(img):
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    return img

# apply binarization technique to reduce the features from image


def convertToBinary(img):
    img = convertToGrayImage(img)
    img = cv2.threshold(img, 120, 255, cv2.THRESH_BINARY)[1]
    return img

# use 2D filter to find the edges
# find contours in the thresholded image and initialize the
# shape detectors


def do_canny(img):
    # Canny edge detector with threshold values 50 and 150
    image = convertToGrayImage(img)
    image = gaussianBlur(img)
    image = convertToBinary(img)
    return cv2.Canny(image, 50, 150)


def resize(img, width, height):
    image = cv2.resize(img, width, height)
    return image


def toGray(img):
    image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    return image


def toHLS(img):
    image = cv2.cvtColor(img, cv2.COLOR_BGR2HLS)
    return image


def toHSV(img):
    image = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    return image


def toLAB(img):
    image = cv2.cvtColor(img, cv2.COLOR_BGR2LAB)
    return image


def toLUV(img):
    image = cv2.cvtColor(img, cv2.COLOR_BGR2LUV)
    return image


def toXYZ(img):
    image = cv2.cvtColor(img, cv2.COLOR_BGR2XYZ)
    return image


# ------------------ CLASSIFICATION --------------------
graph = tf.get_default_graph()
with graph.as_default():
    # load model at very first
    model = load_model("./static/" + 'model_design.h5')

# call model to predict an image


def getResult(imagePath):
    data = image.load_img(imagePath, target_size=(150, 150, 3))
    data = np.expand_dims(data, axis=0)
    data = data * 1.0 / 255

    with graph.as_default():
        predicted = model.predict(data)
        return predicted


# processing uploaded file and predict it
def classification(img):
    indices = {0: 'Cat', 1: 'Dog', 2: 'Not normal', 3: 'Normal'}
    result = getResult(img)
    predicted_class = np.asscalar(np.argmax(result, axis=1))
    accuracy = round(result[0][predicted_class] * 100, 2)
    label = indices[predicted_class]
    results = {
        "label": label,
        "accuracy": accuracy
    }
    return results


def switchFunctions(id, number):
    # number:
    # 0 - processing
    # 1 - blurring
    # 2 - colors

    processingSwitcher = {
        0: gaussianBlur,
        1: convertToGrayImage,
        2: convertToBinary,
        3: do_canny
    }
    blurringSwitcher = {
        0: averaging,
        1: gaussianBlur,
        2: medianFiltering,
        3: bilateralFiltering,
    }
    colorSwitcher = {
        0: toGray,
        1: toHLS,
        2: toHSV,
        3: toLAB,
        4: toLUV,
        5: toXYZ
    }
    switcher = None
    if number == 0:
        switcher = processingSwitcher.get(id, lambda: 'Invalid')
    elif number == 1:
        switcher = blurringSwitcher.get(id, lambda: 'Invalid')
    elif number == 2:
        switcher = colorSwitcher.get(id, lambda: "Invalid")
    return switcher
