# Código para colocar una palabra en la parte superior de la yema del deo
# medio con las herramientas utilizadas son opencv + medipipe hands


import cv2
import mediapipe as mp

mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands
cap = cv2.VideoCapture(0,)

font = cv2.FONT_HERSHEY_PLAIN

# Obtener ancho y alto del frame para poder obtener la
# posición espacial (x, y) del lanmark de interés
frame_width = int(cap.get(3))
frame_height = int(cap.get(4))
#inicialización de la variable auxiliar x1
x1 = 1
y1 = 1
with mp_hands.Hands(
    static_image_mode=False,
    max_num_hands=2,
    min_detection_confidence=0.7) as hands:
    while True:
        ret, frame = cap.read()
        # Línea de instrucción que sirve para comparar la posición espacial
        # del lanmark de interés y poder cerrar la ventana/ terminar el despliegue del video
        if ret == False or x1 <= frame_width and x1>=frame_width-45 and y1 <= 45:
            break
            
        height, width, _ = frame.shape
        frame = cv2.flip(frame, 1)
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = hands.process(frame_rgb)
        if results.multi_hand_landmarks is not None:
            for hand_landmarks in results.multi_hand_landmarks:
                x1 = int(hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].x * frame_width)
                y1 = int(hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].y * frame_height)
                # imprimir las coordenadas espaciales del lanmark de interés 
                print(x1,y1)
                # Dibujar el cuadro en la parte superior derecha del frame              
        cv2.putText(frame, "Indice", (x1,y1), font, 5, (224,0,96), 3, cv2.LINE_AA)
        cv2.imshow('Frame',frame)      
        if cv2.waitKey(1) & 0xFF == 27:
            break 
cap.release()
cv2.destroyAllWindows()
