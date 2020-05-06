import cv2
import numpy as np

# Image denoising
# Denoise the image using Gaussian blur function,
# since it’s the fastest and most useful filter.
# Gaussian filtering is done by convolving each point in the input array
# with a Gaussian kernel and then summing them all to produce the output array
# Gaussian kernel is just a matrix of ones
# the more the size of the matrix, the more blurry image there will be


def gaussianBlur(img):
    kernel = np.ones((5, 5), np.float32) / 25
    dst = cv2.filter2D(img, -1, kernel)
    return dst


# Before detecting the edges, convert the 3-channel color image to 1 channel gray image
def convertToGrayImage(img):
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    return img

# apply binarization technique to reduce the features from image


def convertToBinary(img):
    img = cv2.threshold(img, 120, 255, cv2.THRESH_BINARY)[1]
    return img

# use 2D filter to find the edges
# find contours in the thresholded image and initialize the
# shape detector


def findContoursInImage(img):
    cnts = cv2.findContours(
        thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)
    sd = ShapeDetector()


def switchFunctions(id):
    switcher = {
        0: gaussianBlur,
        1: convertToGrayImage,
        2: convertToBinary,
    }
    return switcher.get(id, lambda :'Invalid')
