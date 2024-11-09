

import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

#image = cv.imread("S:/imagedetectionnvideos/Learn_Python_codes-main/Learn_Python_codes-main/Image_processing/Images/xray1.jpg", 0)
#image = cv.imread("S:/imagedetectionnvideos/Learn_Python_codes-main/Learn_Python_codes-main/Image_processing/Images/4seasons.jpg") # test for the coloful photo
image = cv.imread("S:/imagedetectionnvideos/Learn_Python_codes-main/Learn_Python_codes-main/Image_processing/Images/statue.jpg" , 0) # test for the coloful photo

# [chanell of the photo] could be 0 for black and white photos or any channel that we want
#img_hist= cv.calcHist([image], [chanell of the photo],mask of the photo ,[size of the histogram], [range of the histogram color])
#img_hist= cv.calcHist([image], [0],None,[256], [0,256]) 
#if we have numbers in horizontal axes near zero means that photo has regions that is darker
#if we have numbers in horizontal axes near 255 means that photo has regions that is lighter

# one thing that we could do is to optimize the histogram of the photo and increas the contrast of the photo
"""
w,h,c = image.shape #(width , hight , channel_colors)
mask = np.zeros(image.shape[0:2] , np.uint8) # check this what happened
mask[0:int(w/2) , 0:int(h/2)] = 255

colors = ['b','g','r']
for i , col in enumerate(colors):
    histogram = cv.calcHist([image] , [i] , None , [256] , [0 , 256])
    plt.plot(histogram , color = col)
"""

"""
for i , col in enumerate(colors):
    histogram = cv.calcHist([image] , [i] , mask , [256] , [0 , 256])
    plt.plot(histogram , color = col)
"""

# Equalization of the Histogram
img_hist= cv.calcHist([image], [0],None,[256], [0,256]) 
equalized_histogram = cv.equalizeHist(image)
img_equal_hist= cv.calcHist([equalized_histogram], [0],None,[256], [0,256])

clahe = cv.createCLAHE(clipLimit=2.0, tileGridSize=(8,8)) # it will equalize each part of the photo based on its piccel distriuation histogram
# tileGridSize=(8,8) operate like Kerenel
cl1 = clahe.apply(image)
cl_equal_hist= cv.calcHist([cl1], [0],None,[256], [0,256])


plt.subplot(231), plt.imshow(image, 'gray') , plt.title("Original Image")

plt.subplot(234), plt.plot(img_hist)

plt.subplot(232), plt.imshow(equalized_histogram, 'gray'),plt.title("Equalized Histogram")
plt.subplot(235), plt.plot(img_equal_hist)
plt.subplot(233), plt.imshow(cl1, 'gray'),plt.title("CLAHE")
plt.subplot(236), plt.plot(cl_equal_hist) 

plt.show()