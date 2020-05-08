import cv2
import numpy as np

# Image denoising


# Denoise the image using Averaging function
def averaging(img):
    blur = cv2.blur(img,(5,5))
    return blur

# Denoise the image using Gaussian blur function,
# since it’s the fastest and most useful filter.
# Gaussian filtering is done by convolving each point in the input array
# with a Gaussian kernel and then summing them all to produce the output array
# Gaussian kernel is just a matrix of ones
# the more the size of the matrix, the more blurry image there will be

def gaussianBlur(img):
    kernel = np.ones((10, 10), np.float32) / 100
    blur = cv2.filter2D(img, -1, kernel)
    return blur

# Denoise the image using Median Filtering function
def medianFiltering(img):
    median = cv2.medianBlur(img,5)
    return median


# Denoise the image using Bilateral Filtering function
def bilateralFiltering(img):
    blur = cv2.bilateralFilter(img,9,75,75)
    return blur