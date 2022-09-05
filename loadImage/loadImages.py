import os
import cv2 as cv
import sys

if "loadImage" in os.listdir("."):
    os.chdir("./loadImage")

filePath = "manCubeSword.jpg"

img = cv.imread(filePath)

if img is None:
    sys.exit("Could not read the image.")
else:
    cv.imwrite(filePath.replace(".", "1."), img)
    print("Image Saved!")
