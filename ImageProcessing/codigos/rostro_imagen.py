import cv2
import mediapipe as mp

mp_drawing = mp.solutions.drawing_utils
mp_pose = mp.solutions.pose

img2 = cv2.imread('cara.png')
cap = cv2.VideoCapture(1)
w = int(cap.get(3))
h = int(cap.get(4))

    
codo_x= 0
codo_y = 0
ancho=0
orejaL_x=0
orejaL_y = 0
orejaR_x = 0
orejaR_y = 0

with mp_pose.Pose(min_detection_confidence=0.5,min_tracking_confidence=0.5) as pose:
  while cap.isOpened():
    success, image = cap.read()
    if not success:
      print("Ignoring empty camera frame.")

      continue

    image.flags.writeable = False
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    image2 = image
    
    image = cv2.flip(image, 1)
    image2 = cv2.flip(image2, 1)
    
    results = pose.process(image)
    if results.pose_landmarks:
      image.flags.writeable = True
      image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
      mp_drawing.draw_landmarks(image, results.pose_landmarks, mp_pose.POSE_CONNECTIONS)
      lm = results.pose_landmarks
      lmPose  = mp_pose.PoseLandmark
      orejaL_x = int(results.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_EAR].x * w)
      orejaL_y = int(results.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_EAR].y * h)
      orejaR_x = int(results.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_EAR].x * w)
      orejaR_y = int(results.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_EAR].y * w)
      ancho= abs(orejaL_x-orejaR_x)
      emoji=cv2.resize(img2,(ancho+10,ancho+30))
      xx= emoji.shape[1]
      yy =emoji.shape[0]
      
      combine = cv2.addWeighted(emoji,0.5,image2[ (orejaR_y-150):(orejaR_y+yy-150) , orejaR_x:(orejaR_x+xx) ],0.5,0.0)
      
      image[ (orejaR_y-150):(orejaR_y+yy-150) , orejaR_x:(orejaR_x+xx) ] = combine
      
      print("Oreja Izquierda X:",orejaL_x, "Y:", orejaL_y)
      print("Oreja Derecha X:",orejaR_x, "Y:", orejaR_y)

    cv2.imshow('MediaPipe Pose',image)
    if cv2.waitKey(5) & 0xFF == 27:
      break
cap.release()
cv2.destroyAllWindows()
