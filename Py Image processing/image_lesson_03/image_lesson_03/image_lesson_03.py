import numpy as num
import cv2 as cv
import matplotlib.pyplot as plt 

img0  = cv.imread("C:/Users/39334/OneDrive/Desktop/Resources/1.webp",cv.IMREAD_COLOR)
img1 = cv.resize(img0 , None , fx = 2, fy = 2)
imgray = cv.cvtColor(img1 , cv.COLOR_BGR2GRAY)

# seperating a part of the photo
img2 = imgray[100:300 , 250:500]

# change a part of the photo to another color inside of the photo
imgray[100:300 , 250:500] = 255 # 255 is just 1 color because this photohas only 1 channel(gray channel)
#img1 [0:186 , 0:166] = [0 ,0 ,0]

# copy and paste of a part to another
blue_bolb = img1[0:186 , 0:166]
img1[186:372 , 166:332] = blue_bolb
'''
# showing the 3 channls of the photo
# in opencv = BGR[0,1,2]
b = img1[: , : ,0]
g = img1[: , : ,1]
r = img1[: , : ,2]
cv.imshow("img" , img1)
cv.imshow("blue" , b)
cv.imshow("green" , g)
cv.imshow("red" , r)
'''
# Split and mrege the colors by OpenCv(the problem is that it has a lot of computations so it is slower)
[b,g,r] = cv.split(img1)
img1 = cv.merge([b,g,r])

cv.imshow("img" , img1)
cv.imshow("blue" , b)
cv.imshow("green" , g)
cv.imshow("red" , r)

#cv.imshow("img2" , img2)
cv.waitKey(0)

plt.imshow(img1)
plt.show()

piccell_numbers = img1.size
image_shape = img1.shape; #(dimension , dimension , channel)
image_type  =img1.dtype

print(piccell_numbers , image_shape , image_type)