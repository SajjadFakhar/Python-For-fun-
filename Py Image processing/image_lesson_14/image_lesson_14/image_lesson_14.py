
from turtle import left, right
import cv2 as cv
import numpy as np

# there are several ways to detect the face but in open cv there is this feature if we do not wanna use deep learning  for now
# notice that cascade files are xml and we can find them in the github of the opencv

face_cascade = cv.CascadeClassifier('S:/cascade_files/haarcascade_frontalface_alt.xml')
left_eye_cascade = cv.CascadeClassifier('S:/cascade_files/haarcascade_lefteye_2splits.xml')
right_eye_cascade = cv.CascadeClassifier('S:/cascade_files/haarcascade_righteye_2splits.xml')
smile_cascade = cv.CascadeClassifier('S:/cascade_files/haarcascade_smile.xml')

cap = cv.VideoCapture(0)

while(True):
    rec, frame = cap.read()
    frame_gr = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(frame_gr, 1.3, 5) # here we are gonna find the coordinates of the faces
    
    for (x, y, w, h) in faces: # x,y and Hight and Width of the faces that are detected
        # draw a rectangle around the face
        cv.rectangle(frame, (x,y), (x+w, y+h), (255,255,0), 2) #(desired photo, (x,y), (x+w, y+h (rectangle)), (255,0,255), 2)
        
        # the best way to find the eyes is gonna be looking for the eyes inside the face rectangle
        frame_gr_roi = frame_gr[y:y+h, x:x+w]
        frame_roi = frame[y:y+h, x:x+w]
        left_eyes = left_eye_cascade.detectMultiScale(frame_gr_roi)
        right_eyes = right_eye_cascade.detectMultiScale(frame_gr_roi)
        
        for (lex, ley, lew, leh) in left_eyes:
            cv.rectangle(frame_roi, (lex, ley), (lex+lew, ley+leh), (0,255,0), 2)
        
        for (rex, rey, rew, reh) in right_eyes:
            cv.rectangle(frame_roi, (rex, rey), (rex+rew, rey+reh), (0,255,0), 2)

        smiles = smile_cascade.detectMultiScale(frame_gr_roi, 1.8, 20)

        for (sx, sy, sw, sh) in smiles:
            cv.rectangle(frame_roi, (sx, sy), (sx+sw, sy+sh), (0,0,255), 2)
        
    cv.imshow('frame', frame)

    keyexit = cv.waitKey(5) & 0xFF
    if keyexit == 27:
        break

cv.destroyAllWindows()
cap.release()