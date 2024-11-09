import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt


image = cv.imread("C:/Users/39334/OneDrive/Desktop/Resources/car.jpg", 1)
img_resize = cv.resize(image , dsize= (512 , 512) )
#cv.imwrite("Images/cityscape2.jpg", image)
#cv.IMREAD_GRAYSCALE    0
#cv.IMREAD_COLOR        1
#cv.IMREAD_UNCHANGED    -1

#cv.imshow('IMAGE display', image)
#cv.waitKey(0)

"""
cv.imshow('IMAGE display', image)
cv.waitKey(0)
cv.destroyAllWindows()
"""
to_rbg = cv.cvtColor(image , cv.COLOR_BGR2RGB)
plt.imshow(to_rbg)
plt.axis('off') # or plt.xticks([]),plt.yticks([])
plt.plot([100 , 100 ] , [500 , 100] , 'r' , linewidth = 20) 
plt.show()