from pickle import NONE
import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt

oli_leave = cv.imread("S:/Pest detection/Olive Images/3_leaves.jpg",1)
oliv_resize = cv.resize(oli_leave , None , fx = 1.5 ,fy = 1.5 )
olive_gray = cv.cvtColor(oliv_resize , cv.COLOR_BGR2GRAY)
#blue =oliv_resize[: ,: ,0]
kernel = np.ones((2,2) , np.uint8)
#[b,g,r] = cv.split(oliv_resize)

"""
if np.array_equal(b, blue):
    print("yes it is equal")
else:
    print("nope")
    """

# Mask
#_ , mask = cv.threshold(oliv_resize , 120 , 255 , cv.THRESH_BINARY) 
mask1 =cv.adaptiveThreshold(olive_gray ,255,cv.ADAPTIVE_THRESH_GAUSSIAN_C , cv.THRESH_BINARY,25,1,None)
#Closing
closed = cv.morphologyEx(mask1 ,cv.MORPH_CLOSE, kernel, iterations=1)
image = olive_gray - mask1
#print(none , g ,none)
#cv.imshow("Blue channel" , b)
#cv.imshow("Blue1 channel" , blue)
#cv.imshow("Green channel" , g)
#cv.imshow("Red channel" , r)
#cv.imshow("leaves" , oli_leave)
#cv.imshow("Mask" , mask)
cv.imshow("Addaptive Mask" , mask1)
cv.imshow("Ssubtracted" , image)
cv.imshow("Closed " , closed)

cv.waitKey(0)
cv.destroyAllWindows()


