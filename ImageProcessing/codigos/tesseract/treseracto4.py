import pytesseract
import cv2
from gtts import gTTS
import os
img = cv2.imread('Texto1.jpg')
pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files/Tesseract-OCR/tesseract.exe'
img = cv2.resize(img, (600, 360))
hImg, wImg, _ = img.shape

boxes = pytesseract.image_to_boxes(img)
xy = pytesseract.image_to_string(img)
for b in boxes.splitlines():
  b = b.split(' ')

  x, y, w, h = int(b[1]), int(b[2]), int(b[3]), int(b[4])
  cv2.rectangle(img, (x, hImg-y), (y, hImg-h), (50, 205, 205), 2)
  cv2.putText(img, b[0], (x, hImg -y - 5), cv2.FONT_HERSHEY_COMPLEX, 2, (205, 205, 50), 5)

cv2.imshow('Detected text', img)

audio = gTTS(text = xy, lang = 'en', slow = False)
audio.save("saved_audio.mp3")
os.system("saved_audio.mp3")
cv2.waitKey(0)
cv2.destroyAllWindows()