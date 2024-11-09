import numpy as np
import cv2 as cv

img = cv.imread("C:/Users/39334/OneDrive/Desktop/Resources/car.jpg", cv.IMREAD_COLOR)



cv.line(img, (5,5), (200,150), (200,200,0), 10) #()

cv.rectangle(img,(5,5), (200,150), (255,255,255), 8)

cv.circle(img, (200,150), 50, (0,255,255), 20)

points = np.array([[30,5], [300,200],[100,70],[40,100]], np.int32) # int32 is teh type of the points or numbers
cv.polylines(img, [points], True, (255,0,0), 5) # true here means connect the beggining and end point of the poligone

font = cv.FONT_HERSHEY_SIMPLEX
cv.putText(img, 'Salam be hame',(500,100), font, 1, (255,255,255), 2, cv.LINE_AA)
# (20,20) = the beginning of the text
# font, 1 notice that  1 is the size of the font
# 2 is the thickness of the text
# cv.LINE_AA = is the hardness of the text
cv.imshow('image',img)
cv.waitKey(0)
cv.destroyAllWindows()