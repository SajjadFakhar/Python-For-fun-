
import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt


image = cv.imread('S:/imagedetectionnvideos/Learn_Python_codes-main/Learn_Python_codes-main/Image_processing/Images/Road_in_Norway.jpg', 0)
# for edge detection its reall useful to decrease the noise and blur will be one of the options
image_noise_removed = cv.GaussianBlur(image, (3,3),0) # kernel size

# Laplacian
laplacian = cv.Laplacian(image_noise_removed, cv.CV_64F) #cv.CV_64F data type

# sobelx
sobelx= cv.Sobel(image_noise_removed, cv.CV_64F, 1, 0, ksize=5) # sobel x = 1, 0 it will detect the vertical edges

# sobely
sobely= cv.Sobel(image_noise_removed, cv.CV_64F, 0, 1, ksize=5) # sobel x = 1, 0 it will detect the horizontal edges


# Canny Edge Detection
canny = cv.Canny(image_noise_removed, 100, 200) # 100 and 200 are minimum and maximum threshold
'''
https://www.bogotobogo.com/python/OpenCV_Python/python_opencv3_Image_Gradient_Sobel_Laplacian_Derivatives_Edge_Detection.php#google_vignette
https://learnopencv.com/edge-detection-using-opencv/
'''

"""
plt.subplot(1,2,1),plt.imshow(image,cmap = 'gray')
plt.title('Original'), plt.xticks([]), plt.yticks([])
plt.subplot(1,2,2),plt.imshow(canny,cmap = 'gray')
plt.title('Canny'), plt.xticks([]), plt.yticks([])

plt.show()

"""
plt.subplot(2,2,1),plt.imshow(image,cmap = 'gray')
plt.title('Original'), plt.xticks([]), plt.yticks([])
plt.subplot(2,2,2),plt.imshow(canny,cmap = 'gray')
plt.title('Canny'), plt.xticks([]), plt.yticks([])
plt.subplot(2,2,3),plt.imshow(sobelx,cmap = 'gray')
plt.title('Sobel X'), plt.xticks([]), plt.yticks([])
plt.subplot(2,2,4),plt.imshow(sobely,cmap = 'gray')
plt.title('Sobel Y'), plt.xticks([]), plt.yticks([])

plt.show()
