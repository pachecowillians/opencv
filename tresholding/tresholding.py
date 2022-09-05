import os
import cv2 as cv
import sys
import numpy as np

# Setting folder directory
if "tresholding" in os.listdir("."):
    os.chdir("./tresholding")

filePath = "man.jpg"

# Reading image
img = cv.imread(filePath, cv.IMREAD_GRAYSCALE)

if img is None:
    sys.exit("Could not read the image.")
else:
    img = cv.medianBlur(img, 3)
    th = cv.adaptiveThreshold(img, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 5, 2)

    # Writing the filtered image on new file
    cv.imwrite(filePath.replace(".", "_edited."), th)

    print("Image Saved!")
