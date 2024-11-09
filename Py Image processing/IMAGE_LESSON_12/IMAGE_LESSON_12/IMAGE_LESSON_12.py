import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt

# Here we are gonna check and see the operation of the color space 

#image_bgr = cv.imread("S:/imagedetectionnvideos/Learn_Python_codes-main/Learn_Python_codes-main/Image_processing/Images/graphics.png")    #BGR
image_bgr = cv.imread("S:/imagedetectionnvideos/Learn_Python_codes-main/Learn_Python_codes-main/Image_processing/Images/blue_eyes.jpg")    #BGR
image_gr = cv.cvtColor(image_bgr, cv.COLOR_BGR2GRAY)

#blue_ch, green_ch, red_ch = cv.split(image) # wheneever it's lighter it means we have more of that color in this channel
image_rgb = cv.cvtColor(image_bgr, cv.COLOR_BGR2RGB)
# RGB
# BGR  opencv
# BGRA / RGBA 4 channel alpha opacity(Transparency)
# LAB another type of the color scale(check in the internet)
 
# HSV [20, 100, 100] # Hue Saturation Value , Hue = color , Saturation = the amount of that color , Value = How much is going to be darker or lighter 
image_hsv = cv.cvtColor(image_bgr, cv.COLOR_BGR2HSV)


"""
cv.imshow('IMAGE display', image)
#cv.imshow('Blue display', blue_ch)
#cv.imshow('RED display', red_ch)
#cv.imshow('Green display', green_ch)
cv.waitKey(0)
cv.destroyAllWindows()
"""

plt.imshow(image_hsv)
plt.show()