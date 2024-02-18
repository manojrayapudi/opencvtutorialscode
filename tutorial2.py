import cv2
import random
img = cv2.imread('assets/elephant.jpeg',-1)
print(img.shape)

 

tag = img[40:80, 50:100]  
img[100:140, 100:150]	= tag	
cv2.imshow('Image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
