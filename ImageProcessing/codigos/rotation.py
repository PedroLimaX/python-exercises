# -*- coding: utf-8 -*-
"""
Created on Tue Feb  7 13:26:31 2023

@author: pedro
"""

import cv2
image = cv2.imread('image.png')
height, width = image.shape[:2]
center = (width/2, height/2)
rotate_matrix = cv2.getRotationMatrix2D(center = center,angle = 90, scale=1)
rotated_image = cv2.warpAffine(src=image, M=rotate_matrix,dsize=(width,height))
cv2.imshow("Original",image)
cv2.imshow("rotated image:", rotated_image)
cv2.imwrite('rotated_image.jpg',rotated_image)

cv2.waitKey(0)
cv2.destroyAllWindows()