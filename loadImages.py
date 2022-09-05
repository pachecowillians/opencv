import cv2 as cv
import sys

filePath = "man_cube_sword.jpg"

img = cv.imread(filePath)

if img is None:
    sys.exit("Could not read the image.")
else:
    cv.imwrite(filePath.replace(".", "1."), img)
