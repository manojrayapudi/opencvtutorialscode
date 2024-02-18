import numpy as np 
import cv2 

cap=cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    width = int(cap.get(3))
    height  = int(cap.get(4))

    img = cv2.line(frame,(0,0),(width,height),(255,0,0),10)
    img = cv2.line(img,(0,height),(width,0),(0,0,255),10)
    img = cv2.rectangle(img,(100,100),(200,200),(0,255,0),10)
    img = cv2.circle(img,(100,100),200,(128,128,0),1)
    font = cv2.FONT_HERSHEY_SIMPLEX
    img = cv2.putText(img,'AMMU CHINNU', (10,height -10),font,2,(0,0,0),5,cv2.LINE_AA)
    



    cv2.imshow('frame',img)

    if cv2.waitKey(1)==ord('a'):
        break 
 
cv2.release()
cv2.destroyAllWindows()         