# Código que ejecuta el cambio de valor en un slide proporcionado en pantalla
# con respecto a la distancia de separación de las yemas de los dedos pulgar y el dedo indice.
   
import cv2
import mediapipe as mp
import math

salida = cv2.VideoWriter('/act1/manos2.avi',cv2.VideoWriter_fourcc(*'XVID'),20.0,(640,480))

mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands
cap = cv2.VideoCapture(0,)

frame_width = int(cap.get(3))
frame_height = int(cap.get(4))

x1 = 1
y1 = 1
scale=100
distancia = 10;
with mp_hands.Hands(
    static_image_mode=False,
    max_num_hands=2,
    min_detection_confidence=0.7) as hands:
    while True:
        ret, frame = cap.read()
        if ret == False or x1 <= frame_width and x1>=frame_width-45 and y1 <= 45:
            break
            
        height, width, _ = frame.shape
        frame = cv2.flip(frame, 1)

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
                distancia =  math.sqrt(math.pow((x2-x1),2) + math.pow((y2-y1),2))+30

 
            scale = int (distancia*0.23)
            print("Escala: "+str(scale))
            print("Distancia: "+str(distancia))

            if distancia <= 10 or distancia > 200 or scale <5:
                scale = 49
                print("Salio Rango "+ str(scale))
          
        cv2.rectangle(frame, (frame_width-40,5) , (frame_width,40), (63, 63, 255,-1 ), -1)
        cv2.putText(frame, 'X', (frame_width-35,35), fontFace=cv2.FONT_HERSHEY_COMPLEX, fontScale=1, color=(255,255,255),thickness=2)
        cv2.rectangle(frame, (45,20) , (60,260), (255, 255, 255,-1 ), 3)
        cv2.rectangle(frame, (47,260-scale*3) , (58,260), (0, 255, 0,-1 ), -1)
        cv2.putText(frame, str(scale*2), (70, 30), fontFace=cv2.FONT_HERSHEY_SCRIPT_COMPLEX, fontScale=1, color=(0,255,0),thickness=3)
        cv2.imshow('Ventana',frame)
    
        if cv2.waitKey(1) & 0xFF == 27:
            break 
cap.release()
cv2.destroyAllWindows()
