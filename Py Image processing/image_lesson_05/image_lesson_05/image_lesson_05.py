import numpy as num
import cv2 as cv
import matplotlib.pyplot as plt

#img1 = cv.imread("C:/Users/39334/OneDrive/Desktop/Resources/bookpage.webp")
img1 = cv.imread("C:/Users/39334/OneDrive/Desktop/Resources/brain.jpg")
#img1 = cv.imread("C:/Users/39334/OneDrive/Desktop/Resources/pathology.jpg") # to see the use of OTSU

imggray = cv.cvtColor(img1 , cv.COLOR_BGR2GRAY)
#Thrshold has 2 out puts that most of the time of the time one of them is our desired one 
ret,thresold = cv.threshold(imggray , 200, 255 , cv.THRESH_BINARY) # Manual thresholding

# OTSU Thrsholding (it will analyze the photo and after that will clarify the thresold automatically)
ret2,thresold2 = cv.threshold(imggray ,0 , 255 ,cv.THRESH_BINARY + cv.THRESH_OTSU)
# Notice that this ret2 is the autimatic threshold that it considered by itself
print(ret2) # The threshold that OTSU considered

# when the light is too different so we should consider a addaptive threshold
# it will analyze the photo and consider defferent threshold for different parts
#ret3,thresold3 = (Input , max_Value , desired_method ,how to do threshold , dimension of threshold in the photo,weight decreasing from the dimension)  )
thresold3 = cv.adaptiveThreshold(imggray , 255 ,cv.ADAPTIVE_THRESH_GAUSSIAN_C , cv.THRESH_BINARY , 25 ,1,None)
thresold3_rgb = cv.cvtColor(thresold3 , cv.COLOR_RGB2BGR)
#cv.imshow("Original image" , img1)
#cv.imshow("THRESOLD" , thresold)
cv.imshow("THRESOLD OTSU" , thresold2)
cv.imshow("THRESOLD Adaptive" , thresold3)

cv.imshow("gray" , imggray)
 
cv.waitKey(0)
cv.destroyAllWindows()
#plt.imshow(thresold3_rgb,thresold3)
#plt.show()
