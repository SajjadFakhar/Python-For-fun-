import cv2 as cv
import numpy as np
from cvzone.FaceDetectionModule import FaceDetector
from cvzone.FaceMeshModule import FaceMeshDetector

cap = cv.VideoCapture(0)
detector = FaceDetector() # creating the face detector object
meshdetector = FaceMeshDetector(maxFaces=1) # creating the mesh detector object
# maxFaces=1 the number of faces to be detected

while(True):
    rec, frame = cap.read()
    frame, bbox = detector.findFaces(frame) # here it will find the faces (output = frame, box) , the percentage is showing the confidence of detection
    # box is gonna be used to extract the coordinates of the face box
    frame, faces = meshdetector.findFaceMesh(frame)

    if bbox:
        center = bbox[0]["center"]   
        #cv.circle(frame, center, 5, (255, 0, 255), cv.FILLED) # to draw a circle on the center
    
    cv.imshow('frame', frame)
    # cv.imwrite() try to save this video
    keyexit = cv.waitKey(5) & 0xFF
    if keyexit == 27:
        break

cv.destroyAllWindows()
cap.release()