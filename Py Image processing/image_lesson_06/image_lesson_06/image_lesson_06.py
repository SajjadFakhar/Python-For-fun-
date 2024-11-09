



from cv2 import COLOR_BGR2RGB, MORPH_OPEN, cvtColor
import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt


#original_img = cv.imread("S:/imagedetectionnvideos/Learn_Python_codes-main/Learn_Python_codes-main/Image_processing/Images/Neuron.jpg", 0)
#original_img = cv.imread("S:/imagedetectionnvideos/Learn_Python_codes-main/Learn_Python_codes-main/Image_processing/Images/fingerprint.png", 0)
original_img = cv.imread("S:/imagedetectionnvideos/Learn_Python_codes-main/Learn_Python_codes-main/Image_processing/Images/cells_threshold.png", 0)

_, mask = cv.threshold(original_img, 35, 255, cv.THRESH_BINARY)

# Erosion it will delete the white noises im the photo
kernel1 = np.ones((3,3), np.uint8) # the dimensions of the kernel will explain how much it should erode the phtoto
eroded_img = cv.erode(mask, kernel1, iterations=1)

# Dilation
kernel2 = np.ones((10,10), np.uint8)
delated_img = cv.dilate(mask, kernel1, iterations=1)
#kernel = np.ones((3,3), np.uint8)
#eroded_img = cv.erode(delated_img, kernel, iterations=2)
subtract_img = delated_img - mask

# Closing will close the holes in the photo 
closed_img1 = cv.morphologyEx(mask, cv.MORPH_CLOSE, kernel1)
closed_img2 = cv.morphologyEx(mask, cv.MORPH_CLOSE, kernel2)

# Opening will open the available holes in the photo
# it will be useful after delation when they are sticked together and you can pen them easily
opened_img1 = cv.morphologyEx(mask, MORPH_OPEN, kernel1)
opened_img2 = cv.morphologyEx(mask, MORPH_OPEN, kernel2)


# Gradient is equal to subtracted image

gradient = cv.morphologyEx(mask, cv.MORPH_GRADIENT, kernel2)

ori_img_bgr = cv.cvtColor(original_img , COLOR_BGR2RGB)
mask_img_bgr = cv.cvtColor(mask , COLOR_BGR2RGB)
# cmap specifies the colormap used to map data values to colors in a plot or image.
plt.subplot(3,4,1),plt.imshow(original_img , cmap = 'gray'),plt.title('Original')
plt.axis('off')
plt.subplot(3,4,2),plt.imshow(mask,cmap = 'gray'),plt.title('mask')
plt.axis('off')
plt.subplot(3,4,3),plt.imshow(eroded_img,cmap = 'gray'),plt.title('eroded')
plt.axis('off')
plt.subplot(3,4,4),plt.imshow(delated_img,cmap = 'gray'),plt.title('delated')
plt.axis('off')
plt.subplot(3,4,5),plt.imshow(subtract_img,cmap = 'gray'),plt.title('subtracted')
plt.axis('off')
plt.subplot(3,4,6),plt.imshow(closed_img1,cmap = 'gray'),plt.title('closed image 1')
plt.axis('off')
plt.subplot(3,4,7),plt.imshow(closed_img2,cmap = 'gray'),plt.title('closed image 2')
plt.axis('off')
plt.subplot(3,4,8),plt.imshow(opened_img1,cmap = 'gray'),plt.title('opened_img1')
plt.axis('off')
plt.subplot(3,4,9),plt.imshow(opened_img2,cmap = 'gray'),plt.title('opened_img2')
plt.axis('off')
plt.subplot(3,4,10),plt.imshow(gradient,cmap = 'gray'),plt.title('gradient')
plt.axis('off')


plt.show()
'''
plt.subplot(1,2,1),plt.imshow(img,cmap = 'gray')
plt.title('Original'), plt.xticks([]), plt.yticks([])
plt.subplot(1,2,2),plt.imshow(laplacian,cmap = 'gray')
plt.title('Laplacian'), plt.xticks([]), plt.yticks([])

plt.show()
'''
"""
plt.subplot(2,2,1),plt.imshow(img,cmap = 'gray')
plt.title('Original'), plt.xticks([]), plt.yticks([])
plt.subplot(2,2,2),plt.imshow(laplacian,cmap = 'gray')
plt.title('Laplacian'), plt.xticks([]), plt.yticks([])
plt.subplot(2,2,3),plt.imshow(sobelx,cmap = 'gray')
plt.title('Sobel X'), plt.xticks([]), plt.yticks([])
plt.subplot(2,2,4),plt.imshow(sobely,cmap = 'gray')
plt.title('Sobel Y'), plt.xticks([]), plt.yticks([])

plt.show()
"""
