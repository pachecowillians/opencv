import os
import numpy as np
import cv2 as cv

if "drawingFunctions" in os.listdir("."):
    os.chdir("./drawingFunctions")

# Create a black image
img = np.zeros((512, 512, 3), np.uint8)

# Draw a diagonal blue line with thickness of 5 px
cv.line(img, (0, 0), (255, 255), (255, 0, 0), 5)

cv.circle(img, (255, 255), 100, (0, 0, 255), -1)

cv.rectangle(img, (155, 155), (355, 355), (0, 255, 0), 3)

cv.imwrite("./drawingFunctions.jpg", img)

print("Image Saved!")
