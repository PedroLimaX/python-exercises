import cv2
import mediapipe as mp
import math


mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands
cap = cv2.VideoCapture(1,)

frame_width = int(cap.get(3))
frame_height = int(cap.get(4))

#start = (frame_width, frame_height)

image = cv2.imread('image.png')
height, width = image.shape[:2]

center = (frame_width/2, frame_height/2)


x1 = 1
y1 = 1

with mp_hands.Hands(
    static_image_mode=False,
    max_num_hands=1,
    min_detection_confidence=0.7) as hands:
    while True:
        ret, frame = cap.read()
        
        ret, rotated_frame = cap.read()
        
        
        if ret == False or x1 <= frame_width and x1>=frame_width-45 and y1 <= 45:
            break
            
        height, width, _ = frame.shape
        frame = cv2.flip(frame, 1)
        
        rotated_frame = cv2.flip(rotated_frame,1)
        
        copia=rotated_frame

        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        
        results = hands.process(frame_rgb)
        if results.multi_hand_landmarks is not None:
            for hand_landmarks in results.multi_hand_landmarks:
				#imprimir en el frame los ejes de la mano
                mp_drawing.draw_landmarks(
                    frame, hand_landmarks, mp_hands.HAND_CONNECTIONS,
                    mp_drawing.DrawingSpec(color=(0,0,0), thickness=3, circle_radius=4),
                    mp_drawing.DrawingSpec(color=(255,255,255), thickness=2, circle_radius=3))
                x1 = int(hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP].x * frame_width)
                y1 = int(hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP].y * frame_height)
                x2 = int(hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].x * frame_width)
                y2 = int(hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].y * frame_height)
                
                pulgar =  (x1,y1)
                
                indice = (x2,y2)
                
                print ("center", center)
                print ("pulgar", pulgar)
                print ("indice", indice)
                
                
                if x1 < x2:
                    rotate_matrix = cv2.getRotationMatrix2D(center = center,angle = -90, scale=1)
                    #copia = cv2.warpAffine(src=frame, M=rotate_matrix,dsize=(width,height))
                    rotated_image = cv2.warpAffine(src=image, M=rotate_matrix,dsize=(width,height))
                    cv2.imshow('Rotated', rotated_image)
                    
                if x1 > x2 & y1 < y2:
                    rotate_matrix = cv2.getRotationMatrix2D(center = center,angle = 90, scale=1)
                    #copia = cv2.warpAffine(src=frame, M=rotate_matrix,dsize=(width,height))
                    rotated_image = cv2.warpAffine(src=image, M=rotate_matrix,dsize=(width,height))
                    cv2.imshow('Rotated', rotated_image)
                
        cv2.imshow('Ventana',frame)
        #cv2.imshow('Rotated',copia)
        
    
        if cv2.waitKey(1) & 0xFF == 27:
            break 
cap.release()
cv2.destroyAllWindows()
