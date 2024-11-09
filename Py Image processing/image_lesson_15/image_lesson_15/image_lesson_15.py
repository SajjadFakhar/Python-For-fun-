
import cv2 as cv
import numpy as np
from cvzone.HandTrackingModule import HandDetector 
# installing this librry from the prompt

cap = cv.VideoCapture(0)
detector = HandDetector(detectionCon = 0.5, maxHands=2) # HandDetector(0.5 or 0.8 , maxhands #hands)

while(True):
    rec, frame = cap.read()
    hand, frame = detector.findHands(frame)
    
    if hand:
        if len(hand) > 1 :
            hand1 = hand[0]
            hand2 = hand[1]
        
            lmlist1 = hand1["lmList1"]
            lmlist2 = hand2["lmlist2"]
            length, info, frame = detector.findDistance(lmlist1[4][:-1], lmlist1[8][:-1], frame)
            length, info, frame = detector.findDistance(lmlist2[4][:-1], lmlist2[8][:-1], frame)
        if len(hand) < 2 :
            hand = hand[0]
            lmlist = hand["lmList"]
            length, info, frame = detector.findDistance(lmlist[4][:-1], lmlist[8][:-1], frame)
        
        
    cv.imshow('fram1', frame)
    #cv.imshow('frame2', frame)
    keyexit = cv.waitKey(5) & 0xFF
    if keyexit == 27:
        break 

cv.destroyAllWindows()
cap.release()
