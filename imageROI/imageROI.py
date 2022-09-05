import os
import cv2 as cv
import sys

if "imageROI" in os.listdir("."):
    os.chdir("./imageROI")

filePath = "manCubeSword.jpg"

img = cv.imread(filePath)

if img is None:
    sys.exit("Could not read the image.")
else:
    cv.imwrite(filePath.replace(".", "_edited."), img)
    print("Image Saved!")
