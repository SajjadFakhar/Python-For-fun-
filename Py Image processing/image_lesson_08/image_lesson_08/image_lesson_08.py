

import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt

# here we are gonna do the corner detection 

# Read in the image
image = cv.imread('S:/imagedetectionnvideos/Learn_Python_codes-main/Learn_Python_codes-main/Image_processing/Images/arrows.jpg')
image_gr = cv.imread('S:/imagedetectionnvideos/Learn_Python_codes-main/Learn_Python_codes-main/Image_processing/Images/arrows.jpg',0 )

# In Harries we have to use the Gray photo
corners = cv.cornerHarris(image_gr, 3, 5, 0.04)
# 3 is the block size and will tell in which Cell_neighbourhood it should look for the corners
# k = 3 is the Kernell size and it should be odd
# dts = 0.04 is the Hrris argument that should be achived by try and error
# one of its use can be the detection of the leeters and with connecting them it could rebuild the text
# also in for checking and detecting of the health products on a belt it will be useful
corners_dilated = cv.dilate(corners, None)

# with the below code we can show the coordinates of the corners that harris detected
image[corners_dilated > 0.01*corners_dilated.max()] = [255,0,0]


plt.imshow(image)
plt.show()