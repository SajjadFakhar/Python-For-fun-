import numpy as np
import cv2 as cv

img1 = cv.imread('S:/Image Detection/Python/Resources/retinalcam1.jpg')
img20 = cv.imread('S:/Image Detection/Python/Resources/retinalcam2.jpg')
img2 = cv.resize(img20 , dsize=(585 , 504))
print(img1.shape,img2.shape)

## The easiest way to photos (not good because it sum up all the colors and give a new value for that so it is  not good)
#added = img1 + img2 # notice that they should have the same size (matrix)

added1 = cv.add(img1, img2) # the code from open cv for summing up
#added = cv.addWeighted(img1, 0.8, img2, 0.2, 0) # here is waited for the colors of each photo so we can have a better resoloution for that
# the sum of the weits must be 1 , 
# 0 A scalar added to each sum (used for brightness adjustment).

# as far as we need beter results so we wanna make a mask from the second pphoto
# Mask is a bynary photo that the desired piccells are White and the rest are black or inverse

img2gray = cv.cvtColor(img2, cv.COLOR_BGR2GRAY)
# There are some elements that are gray so to avoid destroying them we will consider a trheshold for that
ret, maskimg = cv.threshold(img2gray, 50 ,255, cv.THRESH_BINARY) 
mask_inv = cv.bitwise_not(maskimg)

img1_m = cv.bitwise_and(img1, img1, mask=mask_inv)
img2_m = cv.bitwise_and(img2, img2, mask=maskimg)
image_added = cv.add(img1_m , img2_m)

cv.imshow('image 1', img1) 
cv.imshow('Mask', maskimg)
cv.imshow('img1_m', img1_m)
cv.imshow('img2_m', img2_m)
cv.imshow('added1',added1)
cv.imshow('added2', image_added)

cv.waitKey(0)
cv.destroyAllWindows()
