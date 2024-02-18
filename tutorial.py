import cv2 

img = cv2.imread('assets/elephant.jpeg',-1)
img = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)
cv2.imwrite('new_img.jpg', img)
cv2.imshow('Image',img)
cv2.waitKey(3000)
cv2.destroyAllWindows()