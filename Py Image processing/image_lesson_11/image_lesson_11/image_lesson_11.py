from email.mime import image
import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

# this part of the pode is related to features 
# it will be used when we wanna use a part of the photo that include important info
# here we also inspect the Feature matching it will help to find a photo from another photo 
# Consider a big photo a small photo
# The use of this action can be in segmentaion later 

#image1 = cv.imread("S:/imagedetectionnvideos/Learn_Python_codes-main/Learn_Python_codes-main/Image_processing/Images/jumbo.jpg")# tosee the sift ,orb
image1 = cv.imread("S:/imagedetectionnvideos/Learn_Python_codes-main/Learn_Python_codes-main/Image_processing/Images/book1.png") # what we are looking for
image2 = cv.imread("S:/imagedetectionnvideos/Learn_Python_codes-main/Learn_Python_codes-main/Image_processing/Images/book2.png") # what we are looking for

# SIFT by use of sift we will make an object in this class
#feat_sift = cv.xfeatures2d.SIFT_create() # making the object
# notice that sift now is in the main of the opencv so we could use it directly
feat_sift = cv.SIFT_create() # making the object
sift_keypoints, descriptors1 = feat_sift.detectAndCompute(image1 , None) #(input , mask)
# sift_keypoints = will find the keypoints 
# descriproes = explanation of this point
image_sift = cv.drawKeypoints(image1, sift_keypoints,None) #(input , points to conect , OutImage)
# as you can see after the running this features are shown in the photo
#cv.SIFT_create()
# SURF
#feat_surf = cv.SURF_create() # this action is not longer aavailable in opencv
# JUST TO NOW : it wil detect more features and edges with respect to sift
#surf_keypoints, descriptors2 = feat_surf.detectAndCompute(image1 , None)
#image_surf = cv.drawKeypoints(image1, surf_keypoints,None)
'''
plt.subplot(2,2,1)
plt.imshow(image_sift)

plt.subplot(2,2,2)
plt.imshow(image_surf)

'''

#ORB
feat_orb = cv.ORB_create(nfeatures=1000)


orb_keypoints1, descriptors1 = feat_orb.detectAndCompute(image1, None)
orb_keypoints2, descriptors2 = feat_orb.detectAndCompute(image2, None)
'''
image_orb = cv.drawKeypoints(image1,orb_keypoints1,None)
plt.imshow(image_orb)
plt.show()
'''


bf = cv.BFMatcher(cv.NORM_HAMMING, crossCheck= True) #BRUTE Force Matching , to see which feature of one photo matches another photo 

matches = bf.match(descriptors1, descriptors2) # to find the matches between the descriptors1 and 2
# here it will rate the matches

matches = sorted(matches, key= lambda x:x.distance) # here it will sort the matches based on their distances

image_matches = cv.drawMatches(image1, orb_keypoints1, image2, orb_keypoints2, matches[:100], None, flags=2) # None =OUTPUT IMAGE

plt.imshow(image_matches)

plt.show()
