# Código para dibujar un cuadro azul en la parte superior derecha
# Este cuadro marcala zona donde se debe colocar la yema del dedo medio
# para cerrar la ventana emergente de video abierta por la cámara web
# Las herramientas utilizadas son opencv + medipipe hands


import cv2
import mediapipe as mp

mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands
cap = cv2.VideoCapture(0,)
# Obtener ancho y alto del frame para poder obtener la
# posición espacial (x, y) del lanmark de interés
frame_width = int(cap.get(3))
frame_height = int(cap.get(4))
#inicializacion de la variable auxiliar x1
x1 = 1
y1 = 1
with mp_hands.Hands(
    static_image_mode=False,
    max_num_hands=2,
    min_detection_confidence=0.7) as hands:
    while True:
        ret, frame = cap.read()
        # Li�nea de instruccion que sirve para comparar la posicion espacial
        # del lanmark de interés y poder cerrar la ventana/ terminar el despliegue del video
        if ret == False or x1 <= frame_width and x1>=frame_width-45 and y1 <= 45:
            break
            
        height, width, _ = frame.shape
        frame = cv2.flip(frame, 1)
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = hands.process(frame_rgb)
        if results.multi_hand_landmarks is not None:
            for hand_landmarks in results.multi_hand_landmarks:
                mp_drawing.draw_landmarks(
                    frame, hand_landmarks, mp_hands.HAND_CONNECTIONS,
                    mp_drawing.DrawingSpec(color=(0,0,0), thickness=3, circle_radius=4),
                    mp_drawing.DrawingSpec(color=(255,255,255), thickness=2, circle_radius=3))
                # obtener las posiciones espaciales del lanmark de interés
                x1 = int(hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_TIP].x * frame_width)
                y1 = int(hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_TIP].y * frame_height)
                # imprimir las coordenadas espaciales del lanmark de interés 
                print(x1,y1)
                # Dibujar el cuadro en la parte superior derecha del frame              
        cv2.rectangle(frame, (frame_width-40,5) , (frame_width,40), (63, 63, 255 ), 3)
        cv2.imshow('Frame',frame)      
        if cv2.waitKey(1) & 0xFF == 27:
            break 
cap.release()
cv2.destroyAllWindows()
