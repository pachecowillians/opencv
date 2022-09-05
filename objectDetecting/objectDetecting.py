import os
import cv2 as cv
import sys
import numpy as np

# Setting folder directory
if "objectDetecting" in os.listdir("."):
    os.chdir("./objectDetecting")

filePath = "hat.jpg"

# Reading image
img = cv.imread(filePath)

if img is None:
    sys.exit("Could not read the image.")
else:

    # Convert to HSV color space
    hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)

    # Setting lower and upper bounds to color
    lower_yellow = np.array([20, 70, 100])
    upper_yellow = np.array([36, 255, 255])

    # Defining mask
    mask = cv.inRange(hsv, lower_yellow, upper_yellow)

    # Applying the mask on image
    result = cv.bitwise_and(img, img, mask=mask)

    # Writing the filtered image on new file
    cv.imwrite(filePath.replace(".", "_edited."), result)
    
    print("Image Saved!")
