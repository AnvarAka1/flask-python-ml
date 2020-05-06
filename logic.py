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

    def applyImageProcessingTechniques(self, id):
        img = cv2.imread(f"./static/images/{self.img}")
        func = switchFunctions(id)
        filteredImg = func(img)
        self.fImg = f"./static/images/f{self.img}"
        cv2.imwrite(self.fImg, filteredImg)

    def setFilteredImage(self):
        img = cv2.imread(f"./static/images/{self.img}")
        filteredImg = gaussianBlur(img)
        self.fImg = f"./static/images/f{self.img}"
        cv2.imwrite(self.fImg, filteredImg)

    def getFilteredImage(self):
        return self.fImg
