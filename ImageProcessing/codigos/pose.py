# -*- coding: utf-8 -*-
"""
Created on Tue Feb 14 13:43:51 2023

@author: pedro
"""
import cv2
import mediapipe as mp
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_pose = mp.solutions.pose

# For webcam input:
cap = cv2.VideoCapture(1)
with mp_pose.Pose(
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5) as pose:
  while cap.isOpened():
    success, image = cap.read()
    image_height, image_width, _ = image.shape
    if not success:
      print("Ignoring empty camera frame.")
      # If loading a video, use 'break' instead of 'continue'.
      continue

    # To improve performance, optionally mark the image as not writeable to
    # pass by reference.
    image.flags.writeable = False
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    results = pose.process(image)
    lm = results.pose_landmarks
    lmPose = mp_pose.PoseLandmark
    
    leftShoulderX = int(lm.landmark[lmPose.LEFT_SHOULDER].x * image_width)
    leftShoulderY = int(lm.landmark[lmPose.LEFT_SHOULDER].y * image_height)
    
    leftElbowX = int(lm.landmark[lmPose.LEFT_ELBOW].x * image_width)
    leftElbowY = int(lm.landmark[lmPose.LEFT_ELBOW].y * image_height)
    
    if leftElbowX >= leftShoulderX and leftShoulderY <= leftElbowY:
        cv2.putText(image, 'Codo abajo del hombro', (70,30), fontFace=cv2.FONT_HERSHEY_COMPLEX, fontScale = 1, color=(0,255,255), thickness=2)
    else:
        cv2.putText(image, 'Codo arriba del hombro', (70,30), fontFace=cv2.FONT_HERSHEY_COMPLEX, fontScale = 1, color=(0,255,255), thickness=2)
    if not results.pose_landmarks:
      continue
    #print(
    #    f'Coordenadas del hombro izq: ('
    #    f'{results.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_SHOULDER].x * image_width}, '
    #    f'{results.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_SHOULDER].y * image_height})'
    #)
    
    # Draw the pose annotation on the image.
    image.flags.writeable = True
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
    mp_drawing.draw_landmarks(
        image,
        results.pose_landmarks,
        mp_pose.POSE_CONNECTIONS,
        landmark_drawing_spec=mp_drawing_styles.get_default_pose_landmarks_style())
    # Flip the image horizontally for a selfie-view display.
    cv2.imshow('MediaPipe Pose', image)
    if cv2.waitKey(5) & 0xFF == 27:
      break
cap.release()
cv2.destroyAllWindows()

