import cv2
from functions import *


class Image:
    img = None
    fImg = None

    def __init__(self):
        self.img = None

    def setImage(self, image):
        self.img = image

    def getImage(self):
        return self.img

    def applyImageProcessingTechniques(self, id, number):
        img = cv2.imread(f"./static/images/{self.img}")
        func = switchFunctions(id, number)
        filteredImg = func(img)
        self.fImg = f"./static/images/f{self.img}"
        cv2.imwrite(self.fImg, filteredImg)

    def applyResize(self, width, height):
        img = cv2.imread(f"./static/images/{self.img}")
        resizedImg = cv2.resize(img, (int(width), int(height)))
        self.fImg = f"./static/images/f{self.img}"
        cv2.imwrite(self.fImg, resizedImg)
        self.fImg = f"f{self.img}"

    def applyClassification(self):
        img = f"./static/images/{self.img}"
        # returns results. Label and accuracy
        return classification(img)

    def getFilteredImage(self):
        return self.fImg
