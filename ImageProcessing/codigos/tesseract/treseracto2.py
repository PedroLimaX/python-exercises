import pytesseract
import cv2
img = cv2.imread('Texto1.jpg')
pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files/Tesseract-OCR/tesseract.exe'
img = cv2.resize(img, (600, 360))
print(pytesseract.image_to_boxes(img))
cv2.imshow('Result', img)
cv2.waitKey(0)
cv2.destroyAllWindows()