import os
import cv2 as cv
import sys

# Changing directory
if "imageROI" in os.listdir("."):
    os.chdir("./imageROI")

filePath = "manCubeSword.jpg"

# Loading image
img = cv.imread(filePath)

# If image is not found
if img is None:
    sys.exit("Could not read the image.")
else:
    # Selecting ROI
    man = img[50:, 55:185]
    roiH = man.shape[0]
    roiW = man.shape[1]

    # Resizing ROI
    manResized = cv.resize(man, (int(roiW/2), int(roiH/2)))

    # Replacing scaled ROI on image
    img[20: 20+int(roiH/2), 15: 15+int(roiW/2)] = manResized
    
    # Saving edited image
    cv.imwrite(filePath.replace(".", "_edited."), img)

    print("Image Saved!")
