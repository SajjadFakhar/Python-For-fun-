
import numpy as num
import cv2 as cv
import matplotlib.pyplot as plt

img_gray = cv.imread("C:/Users/39334/OneDrive/Desktop/Resources/car.jpg" , cv.IMREAD_GRAYSCALE)
img_colour = cv.imread("C:/Users/39334/OneDrive/Desktop/Resources/car.jpg" , cv.IMREAD_COLOR)
img_unchanged = cv.imread("C:/Users/39334/OneDrive/Desktop/Resources/car.jpg" , cv.IMREAD_UNCHANGED)

cv.imwrite("C:/Users/39334/OneDrive/Desktop/Resources/car3.jpg" ,img_gray )

#resized = cv.resize(img , dsize= [600 , 200] ,fx = 0.0,fy = 0.0)
resized = cv.resize(img_colour , None ,fx = 0.5,fy = 0.5)
'''
cv.imshow("original gray image" , img_gray)
cv.imshow("resize image" , resized)
cv.imshow("original coulour" , img_colour)
cv.imshow("original unchanged" , img_unchanged)
cv.waitKey(0)
cv.destroyAllWindows()
'''
rgb_change = cv.cvtColor(resized , cv.COLOR_BGR2RGB)
plt.imshow(rgb_change)
plt.axis('off')
plt.show()