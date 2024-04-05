# -*- coding: utf-8 -*-
"""
Created on Tue Feb 21 13:21:38 2023

@author: pedro
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Feb 14 13:43:51 2023

@author: pedro
"""
import cv2
import mediapipe as mp
import math


mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_pose = mp.solutions.pose

image = cv2.imread('image.png')

imgHeight, imgWidth = image.shape[:2]

imgCenter = (imgHeight/2, imgWidth/2)

# For webcam input:
cap = cv2.VideoCapture(0)
with mp_pose.Pose(
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5) as pose:
  while cap.isOpened():
    success, frame = cap.read()
    frameHeight, frameWidth, _ = frame.shape
    frameCenter = (frameHeight/2, frameWidth/2)
    
    if not success:
      print("Ignoring empty camera frame.")
      # If loading a video, use 'break' instead of 'continue'.
      continue

    # To improve performance, optionally mark the image as not writeable to
    # pass by reference.
    frame.flags.writeable = False
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = pose.process(frame)
    lm = results.pose_landmarks
    lmPose = mp_pose.PoseLandmark
    
    
    #coords de oreja derecha
    rightEarX = int(lm.landmark[lmPose.RIGHT_EAR].x * imgWidth)
    rightEarY = int(lm.landmark[lmPose.RIGHT_EAR].y * imgHeight)
    
    #coords de oreja izquierda
    leftEarX = int(lm.landmark[lmPose.LEFT_EAR].x * imgWidth)
    leftEarY = int(lm.landmark[lmPose.LEFT_EAR].y * imgHeight)
    
    if not results.pose_landmarks:
      continue
    print(
        f'Oreja derecha: ('
        f'{results.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_EAR].x * imgWidth}, '
        f'{results.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_EAR].y * imgHeight})'
        f'\nOreja izquierda: ('
        f'{results.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_EAR].x * imgWidth}, '
        f'{results.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_EAR].y * imgHeight})\n\n'
    )
    
    distancia =  math.sqrt(math.pow((leftEarX-rightEarX),2) + math.pow((leftEarY-rightEarY),2))+30
    
    scale = int (distancia*0.23)
    print("Escala: "+str(scale))
    print("Distancia: "+str(distancia))
    
    print("Oreja Derecha X: "+str(rightEarX))
    print("Oreja Derecha Y: "+str(rightEarY))
    
    print("Oreja Izquerda X: "+str(leftEarX))
    print("Oreja Izquerda Y: "+str(leftEarY))
    
    dsizeW = int(imgWidth/2*scale/100) 
    dsizeH = int(imgHeight/2*scale/100)
    
    dsize = (dsizeW,dsizeH)
    
    print(dsize)
    
    # Draw the pose annotation on the image.
    frame.flags.writeable = True
    frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
    mp_drawing.draw_landmarks(
        frame,
        results.pose_landmarks,
        mp_pose.POSE_CONNECTIONS,
        landmark_drawing_spec=mp_drawing_styles.get_default_pose_landmarks_style())
    # Flip the image horizontally for a selfie-view display.
    #cv2.rectangle(frame, (frameWidth-frameCenter,5) , (frameWidth,40), (255, 255, 255,-1 ), -1)
    #cv2.rectangle(frame, (rightEarX),(leftEarY),(255,255,255,-1),-1)
    #cv2.imshow('Position detector', frame)
    resized = cv2.resize(image, dsize ,interpolation = cv2.INTER_AREA)
    
    overlay = resized
    
    rows,cols,channels = overlay.shape

    overlay=cv2.addWeighted(frame[0:0+rows, 0:0+cols],0.5,overlay,0.5,0)

    frame[dsizeW:dsizeW+rows, dsizeH:dsizeH+cols ] = overlay
    cv2.imshow('Overlayed', frame)
    #cv2.imshow('Image', resized)
    
    if cv2.waitKey(5) & 0xFF == 27:
      break
cap.release()
cv2.destroyAllWindows()

