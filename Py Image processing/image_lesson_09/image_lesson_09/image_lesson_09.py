from unittest import result
import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt

# notice that in the places that objects are too much and close to each other it will be good to use them

# Here we are gonna work on Template Matching that could be use as a simple exapmple of the object detection
# The use of template matching will be where that One object (one shape) is repeated too much
# it the resemblance will include the shape , color and so on.
# here in template it will convolut the smal photo on the big one and if there is any better matches it will lighten those piccelss
'''
image = cv.imread("Images/building1.jpg", 0)

template = cv.imread("Images/building1_temp.jpg", 0)
w, h = template.shape
result = cv.matchTemplate(image, template, cv.TM_CCOEFF_NORMED)
'''
image = cv.imread("S:/imagedetectionnvideos/Learn_Python_codes-main/Learn_Python_codes-main/Image_processing/Images/planes.jpeg",0)
print(image.size)
#resize = cv.resize(image ,None , fx = 0.5 , fy = 0.5)
template = cv.imread("S:/imagedetectionnvideos/Learn_Python_codes-main/Learn_Python_codes-main/Image_processing/Images/plane.jpeg",0)
w, h = template.shape # here it's gonna give the width and the length of the template
result = cv.matchTemplate(image, template, cv.TM_CCOEFF_NORMED)

# now we wanna define the bounding box so if there is any matches more than the specified threshold just show them

threshold = 0.4 # with the threshold we could decrease or increase the detection of the object but if we decrease it too much it wont wok perfectly

locations = np.where(result >= threshold) # where the matches are found
# Now for showing the locations we need to find the start and the ending points of the points that we found
# the start point is gonna be related to the location that we found

# * this will work on coordinates one by one
for point in zip(*locations[::-1]): # zip will invers the dimension of an array
    cv.rectangle(image, point, (point[0]+ h, point[1]+w), (255,255,0), 2)
    
    print('template.shape : ',template.shape,'point [0] : ' , point[0] ,'point [1] : ' , point[1] ,'Hight : ',(point[0]+ h),'width : ',( point[1]+w)  )


cv.imshow("planes" , image)
#cv.imshow("result" , result)
cv.waitKey(0)
#plt.imshow(image)
#plt.show()