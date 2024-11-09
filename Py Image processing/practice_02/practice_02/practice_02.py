#from matplotlib.image import imread
import numpy as num
import cv2 as cv
import matplotlib.pyplot as plt

image = cv.imread("C:/Users/39334/OneDrive/Desktop/Resources/img.png" , cv.IMREAD_GRAYSCALE)
image_color = cv.imread("C:/Users/39334/OneDrive/Desktop/Resources/img.png" , cv.IMREAD_COLOR)

ch_size = cv.resize(image , None , fx = 1.5 , fy = 1.5)

cv.imwrite("C:/Users/39334/OneDrive/Desktop/Resources/img2.png" , image)
'''
cv.imshow("practivce_02" , image)
cv.imshow("practivce_02_color" , image_color)
cv.imshow("practivce_02_size" , ch_size)
cv.waitKey(0)
cv.destroyAllWindows()
'''

rgb_change = cv.cvtColor(image_color , cv.COLOR_RGB2BGR)
plt.imshow( image)
plt.show()
plt.imshow( ch_size)
plt.show()
plt.imshow( rgb_change)
plt.axis('off')
plt.show()
