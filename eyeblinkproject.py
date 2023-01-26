import numpy as np
import cv2

#initializing the face and eye cascade classifiers from xml files
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye_face_eyeglasses.xml')

#variable store execution state
first_read = True
cap = cv2.VideoCapture(0)
ret,img = cap.read()

while(ret):
    ret,img = cap.read()

    #converting the recorded image to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    #applying filter to remove impurities
    gray = cv2.bilateralFilter(gray,5,1,1)

    #Detecting the face for region of Image to be fed to eye classifier
    faces = face_cascade.detectMultiScale(gray, 1.3, 5, minSize = (200,200))

    if (len(faces) > 0 ):
        for(x,y,w,h) in faces:
            img = cv2.rectangle(img, (x,y), (x+w, y+h), (0,255,0),2)   
