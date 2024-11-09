
import cv2 as cv
import numpy as np

cap = cv.VideoCapture(0) # 0 is only for one camera, for more than one, we can say use which camera

while(True):
    rec, frame = cap.read()
    #cv.imshow("video" , frame)
  
    # colors are different in videos so it is better to consider a range for that
    frame_hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV) 

    lower_red = np.array([100,50,50]) # blue range
    upper_red = np.array([116,255,255]) # blue range

    mask_red = cv.inRange(frame_hsv, lower_red, upper_red)
    frame_masked = cv.bitwise_and(frame, frame, mask = mask_red) #(input , output , mask)

    cv.imshow('frame', frame)
    cv.imshow('mask_red', mask_red)
    cv.imshow('frame_masked', frame_masked)

    
    keyexit = cv.waitKey(5) & 0xFF  # 0xFF is the code of esc key
    if keyexit == 27:
        break

cv.destroyAllWindows()
cap.release()